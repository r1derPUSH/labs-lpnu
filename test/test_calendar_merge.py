"""Тести для функції merge_intervals (Лабораторна 2, Варіант 2)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from calendar_merge import merge_intervals


class TestMergeIntervals(unittest.TestCase):
    def test_example_from_task(self):
        intervals = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_empty_input(self):
        self.assertEqual(merge_intervals([]), [])

    def test_single_interval(self):
        self.assertEqual(merge_intervals([(2, 5)]), [(2, 5)])

    def test_no_overlap(self):
        intervals = [(7, 9), (1, 3), (4, 5)]
        expected = [(1, 3), (4, 5), (7, 9)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_full_overlap(self):
        intervals = [(1, 10), (2, 5), (3, 7)]
        expected = [(1, 10)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_touching_intervals(self):
        intervals = [(1, 3), (3, 5), (5, 7)]
        expected = [(1, 7)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_all_identical(self):
        intervals = [(2, 4), (2, 4), (2, 4)]
        expected = [(2, 4)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_already_sorted(self):
        intervals = [(0, 1), (2, 3), (4, 5)]
        expected = [(0, 1), (2, 3), (4, 5)]
        self.assertEqual(merge_intervals(intervals), expected)


if __name__ == "__main__":
    unittest.main()