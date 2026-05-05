"""
Лабораторна робота 5, Рівень 2, Варіант 1.

Реалізація черги з пріоритетами на основі бінарної max-купи (binary heap).
"""

from typing import List, Tuple


class Node:
    """Вузол черги: значення + пріоритет + порядок вставки."""

    def __init__(self, value, priority: int, insertion_order: int) -> None:
        self.value = value
        self.priority = priority
        self.insertion_order = insertion_order

    def is_higher_than(self, other: "Node") -> bool:
        """Чи має цей вузол вищий пріоритет за other."""
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.insertion_order < other.insertion_order


class HeapBasedPriorityQueue:
    """Черга з пріоритетами на масиві-купі."""

    def __init__(self) -> None:
        self._heap: List[Node] = []
        self._counter: int = 0

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return not self._heap

    def insert(self, value, priority: int) -> None:
        """Додати елемент. Складність: O(log n)."""
        node = Node(value, priority, self._counter)
        self._counter += 1
        self._heap.append(node)
        self._sift_up(len(self._heap) - 1)

    def pop(self):
        """Видалити та повернути значення з найвищим пріоритетом."""
        if not self._heap:
            raise IndexError("pop from empty priority queue")

        top = self._heap[0]
        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            self._sift_down(0)
        return top.value

    def peek(self) -> Tuple:
        """Подивитись на (значення, пріоритет) на вершині без зміни черги."""
        if not self._heap:
            raise IndexError("peek from empty priority queue")
        head = self._heap[0]
        return head.value, head.priority

    def view(self) -> List[Tuple]:
        """Повернути копію вмісту купи у вигляді списку (значення, пріоритет)."""
        return [(node.value, node.priority) for node in self._heap]

    def _sift_up(self, index: int) -> None:
        """Підняти елемент угору, доки він порушує властивість купи."""
        while index > 0:
            parent = (index - 1) // 2
            if self._heap[index].is_higher_than(self._heap[parent]):
                self._heap[index], self._heap[parent] = (
                    self._heap[parent],
                    self._heap[index],
                )
                index = parent
            else:
                break

    def _sift_down(self, index: int) -> None:
        """Опустити елемент униз, доки він порушує властивість купи."""
        size = len(self._heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            best = index

            if left < size and self._heap[left].is_higher_than(
                self._heap[best]
            ):
                best = left
            if right < size and self._heap[right].is_higher_than(
                self._heap[best]
            ):
                best = right

            if best == index:
                break

            self._heap[index], self._heap[best] = (
                self._heap[best],
                self._heap[index],
            )
            index = best