"""Тести для post_order_traversal (Лабораторна 3, Варіант 2)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from post_order import BinaryTree, post_order_traversal


class TestPostOrderTraversal(unittest.TestCase):
    def test_example_from_task(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        self.assertEqual(post_order_traversal(root), [5, 2, 6, 7, 3, 1])

    def test_empty_tree(self):
        self.assertEqual(post_order_traversal(None), [])

    def test_single_node(self):
        self.assertEqual(post_order_traversal(BinaryTree(42)), [42])

    def test_only_left_chain(self):
        root = BinaryTree(1, left=BinaryTree(2, left=BinaryTree(3)))
        self.assertEqual(post_order_traversal(root), [3, 2, 1])

    def test_only_right_chain(self):
        root = BinaryTree(1, right=BinaryTree(2, right=BinaryTree(3)))
        self.assertEqual(post_order_traversal(root), [3, 2, 1])

    def test_balanced_tree(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5, left=BinaryTree(3), right=BinaryTree(7))
        root.right = BinaryTree(15, left=BinaryTree(12), right=BinaryTree(20))

        self.assertEqual(
            post_order_traversal(root), [3, 7, 5, 12, 20, 15, 10]
        )


if __name__ == "__main__":
    unittest.main()
