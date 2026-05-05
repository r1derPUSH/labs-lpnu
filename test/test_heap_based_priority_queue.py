"""Тести для HeapBasedPriorityQueue (Лабораторна 5, Варіант 1)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from heap_based_priority_queue import HeapBasedPriorityQueue


class TestHeapBasedPriorityQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue: HeapBasedPriorityQueue = HeapBasedPriorityQueue()

    def test_new_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            self.queue.pop()

    def test_peek_empty_raises(self):
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_single_insert_and_pop(self):
        self.queue.insert("only", priority=42)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.peek(), ("only", 42))
        self.assertEqual(self.queue.pop(), "only")
        self.assertTrue(self.queue.is_empty())

    def test_pop_in_priority_order(self):
        self.queue.insert("a", priority=1)
        self.queue.insert("b", priority=5)
        self.queue.insert("c", priority=3)
        self.queue.insert("d", priority=10)
        self.queue.insert("e", priority=2)

        self.assertEqual(self.queue.pop(), "d")
        self.assertEqual(self.queue.pop(), "b")
        self.assertEqual(self.queue.pop(), "c")
        self.assertEqual(self.queue.pop(), "e")
        self.assertEqual(self.queue.pop(), "a")
        self.assertTrue(self.queue.is_empty())

    def test_stable_for_equal_priorities(self):
        self.queue.insert("first", priority=5)
        self.queue.insert("second", priority=5)
        self.queue.insert("third", priority=5)

        self.assertEqual(self.queue.pop(), "first")
        self.assertEqual(self.queue.pop(), "second")
        self.assertEqual(self.queue.pop(), "third")

    def test_mixed_priorities_stable(self):
        self.queue.insert("low-1", priority=1)
        self.queue.insert("high-1", priority=10)
        self.queue.insert("low-2", priority=1)
        self.queue.insert("high-2", priority=10)
        self.queue.insert("mid", priority=5)

        self.assertEqual(self.queue.pop(), "high-1")
        self.assertEqual(self.queue.pop(), "high-2")
        self.assertEqual(self.queue.pop(), "mid")
        self.assertEqual(self.queue.pop(), "low-1")
        self.assertEqual(self.queue.pop(), "low-2")

    def test_peek_does_not_modify(self):
        self.queue.insert("x", priority=3)
        self.queue.insert("y", priority=7)

        self.assertEqual(self.queue.peek(), ("y", 7))
        self.assertEqual(self.queue.peek(), ("y", 7))
        self.assertEqual(len(self.queue), 2)

    def test_view_does_not_modify(self):
        self.queue.insert("x", priority=3)
        self.queue.insert("y", priority=7)
        self.queue.insert("z", priority=5)

        snapshot = self.queue.view()
        self.assertEqual(len(snapshot), 3)
        self.assertEqual(len(self.queue), 3)

        snapshot.clear()
        self.assertEqual(len(self.queue), 3)

    def test_interleaved_inserts_and_pops(self):
        self.queue.insert("a", 2)
        self.queue.insert("b", 8)
        self.assertEqual(self.queue.pop(), "b")
        self.queue.insert("c", 5)
        self.queue.insert("d", 1)
        self.assertEqual(self.queue.pop(), "c")
        self.assertEqual(self.queue.pop(), "a")
        self.assertEqual(self.queue.pop(), "d")
        self.assertTrue(self.queue.is_empty())


if __name__ == "__main__":
    unittest.main()