from unittest import TestCase

from Node import Node
from main import findLowestCommonAncestor, getPathToNodeFromRoot

class Test(TestCase):
    def test_find_lowest_common_ancestor(self):
        # Hard Coded Binary Tree
        root = Node(0)
        root.l = Node(1)
        root.r = Node(2)
        root.l.l = Node(3)
        root.l.r = Node(4)
        root.r.l = Node(5)
        root.r.r = Node(6)
        root.l.l.l = Node(7)
        root.l.l.r = Node(8)
        root.l.r.l = Node(9)
        root.l.r.r = Node(10)
        root.r.l.l = Node(11)
        root.r.l.r = Node(12)
        root.r.r.l = Node(13)
        root.r.r.r = Node(14)

        # LCA Assertions
        self.assertEqual(findLowestCommonAncestor(root, 11, 13), 2)
        self.assertEqual(findLowestCommonAncestor(root, 9, 10), 4)
        self.assertEqual(findLowestCommonAncestor(root, 3, 4), 1)
        self.assertEqual(findLowestCommonAncestor(root, 7, 8), 3)
        self.assertEqual(findLowestCommonAncestor(root, 11, 12), 5)

        print("LCA Tests Passed")

    def test_get_path_to_node_from_root(self):
        #Hard Coded Binary Tree
        root = Node(0)
        root.l = Node(1)
        root.r = Node(2)
        root.l.l = Node(3)
        root.l.r = Node(4)
        root.r.l = Node(5)
        root.r.r = Node(6)
        root.l.l.l = Node(7)
        root.l.l.r = Node(8)
        root.l.r.l = Node(9)
        root.l.r.r = Node(10)
        root.r.l.l = Node(11)
        root.r.l.r = Node(12)
        root.r.r.l = Node(13)
        root.r.r.r = Node(14)

        path = []
        getPathToNodeFromRoot(root, path, 13)
        self.assertEqual(path, [0, 2, 6, 13])

        path = []
        getPathToNodeFromRoot(root, path, 5)
        self.assertEqual(path, [0, 2, 5])

        path = []
        getPathToNodeFromRoot(root, path, 11)
        self.assertEqual(path, [0, 2, 5, 11])

        path = []
        getPathToNodeFromRoot(root, path, 7)
        self.assertEqual(path, [0, 1, 3, 7])

        print("GetPath test passed")