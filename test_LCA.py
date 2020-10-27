from unittest import TestCase
from main import findLowestCommonAncestor
import networkx as nx

class Test(TestCase):
    def test_find_lowest_common_ancestor(self):
        # Hard Coded Binary Tree
        graph = nx.DiGraph()
        graph_objects = [   ("root", 0),
                            (0, 1),
                            (0, 2),
                            (1, 3),
                            (1, 4),
                            (2, 5),
                            (2, 6),
                            (3, 7),
                            (3, 8),
                            (4, 9),
                            (4, 10),
                            (5, 11),
                            (5, 12),
                            (6, 13),
                            (6, 14),
                            (7, 18),
                            (9, 15),
                            (11, 15),
                            (12, 16),
                            (14, 16),
                            (15, 17),
                            (16, 17),
                            (17, 18)]

        graph.add_edges_from(graph_objects)

        # LCA Assertions
        self.assertEqual(findLowestCommonAncestor(graph, 11, 13), 2)
        self.assertEqual(findLowestCommonAncestor(graph, 9, 10), 4)
        self.assertEqual(findLowestCommonAncestor(graph, 3, 4), 1)
        self.assertEqual(findLowestCommonAncestor(graph, 7, 8), 3)
        self.assertEqual(findLowestCommonAncestor(graph, 11, 12), 5)
        self.assertEqual(findLowestCommonAncestor(graph, 17, 7), 1)
        self.assertEqual(findLowestCommonAncestor(graph, 16, 15), 5)
        self.assertEqual(findLowestCommonAncestor(graph, 17, 14), 14)

        print("LCA Tests Passed")