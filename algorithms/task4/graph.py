from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path

import graphviz

from algorithms.task4.binary_heap import BinaryHeap


@dataclass
class Graph:
    nodes: list[str]
    edges: dict[tuple[str, str], float]

    @classmethod
    def from_list_of_edges(cls, list_of_edges):
        nodes = set()
        edges = {}
        for left_node, right_node, edge in list_of_edges:
            nodes.add(left_node)
            nodes.add(right_node)
            edges[(left_node, right_node)] = float(edge)
        return cls(list(sorted(nodes)), edges)

    @classmethod
    def from_file(cls, file_name):
        return cls.from_list_of_edges(
            map(lambda line: line.strip().split(" "), (Path(__file__).parent / file_name).open().readlines())
        )

    def save_to_file(self, start_node: str | None = None, end_node: str | None = None):
        dot = graphviz.Digraph()

        validator = []
        if start_node and end_node:
            path, _ = self.dijkstra(start_node, end_node)
            validator = list(pairwise(path))
            dot.attr(label=" \u2192 ".join(path), size="10,10")

        for node in self.nodes:
            dot.node(node, node)
        for (left_node, right_node), label in self.edges.items():
            if (left_node, right_node) in validator:
                dot.edge(left_node, right_node, label=str(label), color="red")
            else:
                dot.edge(left_node, right_node, label=str(label))

        dot.render()

    def dijkstra(self, start_node: str, end_node: str):
        """
        Returns the shortest path (with all nodes) and the distance between start_node and end_node. This implementation
        uses heapq (binary heap).
        """
        from collections import defaultdict

        distances = defaultdict(lambda: float("inf"))
        distances[start_node] = 0
        previous_nodes = defaultdict(lambda: None)
        heap = BinaryHeap()
        heap.push((0, start_node))

        while heap:
            current_distance, current_node = heap.pop()
            if current_distance > distances[current_node]:
                continue
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
            current_node = previous_nodes[current_node]
        path.reverse()
        return path, distances[end_node]


if __name__ == "__main__":
    graph = Graph.from_file("sample.graph")
    # print(graph.dijkstra("1", "5"))
    graph.save_to_file("1", "5")
