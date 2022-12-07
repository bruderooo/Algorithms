from algorithms.task4.graph import Graph


def test_dijkstra():
    graph = Graph.from_list_of_edges(
        [
            ("1", "2", 20),
            ("1", "3", 15),
            ("1", "4", 50),
            ("2", "3", 8),
            ("2", "5", 20),
            ("2", "6", 10),
            ("3", "2", 1),
            ("3", "6", 12),
            ("4", "2", 14),
            ("5", "6", 10),
            ("5", "2", 25),
            ("5", "4", 19),
            ("6", "2", 8),
            ("6", "3", 10),
            ("6", "5", 2),
        ]
    )

    path, distance = graph.dijkstra("1", "4")

    assert 47 == distance
    assert ["1", "3", "2", "6", "5", "4"] == path