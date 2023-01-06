import bisect
import math
from collections import defaultdict
from itertools import pairwise

import graphviz

from algorithms.task4.binary_heap import BinaryHeap
from algorithms.task4.graph import Graph


class TimeGraph(Graph):

    def __init__(self, graph, departure_times):
        super().__init__(graph)
        self._departure_times = departure_times

    @classmethod
    def from_list_of_edges(cls, list_of_edges):
        graph = {}
        departure_times = {}

        for left_node, right_node, edge, *departures in list_of_edges:
            graph[left_node] = graph.get(left_node, {}) | {right_node: int(edge)}
            departure_times[(left_node, right_node)] = departures

        return cls(graph, departure_times)

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
                label=f"{label} {self._departure_times[(left_node, right_node)]}",
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

                    new_distance += next(
                        (
                            diff
                            for dep_time in self._departure_times[(current_node, other_node)]
                            if (diff := dep_time - current_distance) > 0
                        ),
                        math.inf
                    )

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