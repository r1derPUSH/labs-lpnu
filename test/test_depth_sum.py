"""Тести для sum_of_depths (Лабораторна 4, Варіант 2)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from depth_sum import TreeNode, sum_of_depths


class TestSumOfDepths(unittest.TestCase):
    def test_example_from_task(self):
        root = TreeNode(1)
        root.left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
        root.right = TreeNode(3)

        self.assertEqual(sum_of_depths(root), 6)

    def test_empty_tree(self):
        self.assertEqual(sum_of_depths(None), 0)

    def test_single_node(self):
        self.assertEqual(sum_of_depths(TreeNode(7)), 0)

    def test_left_chain(self):
        root = TreeNode(
            1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4)))
        )
        self.assertEqual(sum_of_depths(root), 6)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
        root.right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))

        self.assertEqual(sum_of_depths(root), 10)

    def test_right_chain(self):
        root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
        self.assertEqual(sum_of_depths(root), 3)


if __name__ == "__main__":
    unittest.main()