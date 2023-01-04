import math
from collections import defaultdict
from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path

import graphviz

from algorithms.task4.binary_heap import BinaryHeap


class Graph:
    def __init__(self, graph):
        self._graph = graph

    @property
    def nodes(self) -> list[str]:
        return self._graph.keys()

    @property
    def edges(self) -> dict[tuple[str, str], int]:
        edges = {}

        for nodes_first, sub_graph in self._graph.items():
            for other_node, distance in sub_graph.items():
                edges[(nodes_first, other_node)] = distance

        return edges

    @classmethod
    def from_list_of_edges(cls, list_of_edges):
        graph = {}

        for left_node, right_node, edge in list_of_edges:
            graph[left_node] = graph.get(left_node, {}) | {right_node: int(edge)}

        return cls(graph)

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
                color="red" if (left_node, right_node) in validator else "black",
            )

        return dot

    def dijkstra(self, start_node: str, end_node: str):
        distances = defaultdict(lambda: math.inf)
        distances[start_node] = 0
        previous_nodes = {}
        heap = BinaryHeap()
        heap.push((0, start_node))

        while heap:
            current_distance, current_node = heap.pop()
            if current_distance <= distances[current_node]:
                for other_node, edge in self._graph[current_node].items():
                    new_distance = current_distance + edge
                    if new_distance < distances[other_node]:
                        distances[other_node] = new_distance
                        previous_nodes[other_node] = current_node
                        heap.push((new_distance, other_node))

        path = []
        current_node = end_node

        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes.get(current_node)

        return path[::-1], distances[end_node]
