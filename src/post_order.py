"""
Лабораторна робота 3, Рівень 1, Варіант 2.

Завдання: реалізувати зворотній (post-order) обхід бінарного дерева.
"""

from typing import List, Optional


class BinaryTree:
    """Вузол бінарного дерева."""

    def __init__(
        self,
        value,
        left: "Optional[BinaryTree]" = None,
        right: "Optional[BinaryTree]" = None,
        parent: "Optional[BinaryTree]" = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def post_order_traversal(root: Optional[BinaryTree]) -> List:
    """Повернути значення вузлів дерева у порядку post-order обходу."""
    if root is None:
        return []

    result: List = []
    _traverse(root, result)
    return result


def _traverse(node: Optional[BinaryTree], result: List) -> None:
    """Допоміжна рекурсивна функція для накопичення значень."""
    if node is None:
        return
    _traverse(node.left, result)
    _traverse(node.right, result)
    result.append(node.value)
