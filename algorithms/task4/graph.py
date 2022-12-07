from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path
from collections import defaultdict
import graphviz

from algorithms.task4.binary_heap import BinaryHeap


@dataclass
class Graph:
    nodes: list[str]
    edges: dict[tuple[str, str], int]

    @classmethod
    def from_list_of_edges(cls, list_of_edges):
        nodes = set()
        edges = {}
        for left_node, right_node, edge in list_of_edges:
            nodes.add(left_node)
            nodes.add(right_node)
            edges[(left_node, right_node)] = int(edge)
        return cls(list(sorted(nodes)), edges)

    @classmethod
    def from_file(cls, file_name):
        return cls.from_list_of_edges(
            map(lambda line: line.strip().split(" "), (Path(__file__).parent / file_name).open().readlines())
        )

    def image(self, start_node: str | None = None, end_node: str | None = None):
        dot = graphviz.Digraph()

        validator = []
        if start_node and end_node:
            path, distance = self.dijkstra(start_node, end_node)
            validator = list(pairwise(path))
            dot.attr(label=" \u2192 ".join(path) + f"\nDistance: {distance}", size="10,10")

        for node in self.nodes:
            dot.node(node, node)

        for (left_node, right_node), label in self.edges.items():
            dot.edge(
                left_node,
                right_node,
                label=str(label),
                color="red" if (left_node, right_node) in validator else "black"
            )

        return dot

    def dijkstra(self, start_node: str, end_node: str):
        distances = defaultdict(lambda: float("inf"))
        distances[start_node] = 0
        previous_nodes = {}
        heap = BinaryHeap()
        heap.push((0, start_node))

        while heap:
            current_distance, current_node = heap.pop()
            if current_distance <= distances[current_node]:
                for (left_node, right_node), edge in self.edges.items():
                    if left_node == current_node:
                        new_distance = current_distance + edge
                        if new_distance < distances[right_node]:
                            distances[right_node] = new_distance
                            previous_nodes[right_node] = current_node
                            heap.push((new_distance, right_node))

        path = []
        current_node = end_node

        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes.get(current_node)

        return path[::-1], distances[end_node]
