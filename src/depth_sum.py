"""
Лабораторна робота 4, Рівень 2, Варіант 2.

Завдання: для бінарного дерева знайти суму глибин усіх вузлів.
"""

from typing import Optional


class TreeNode:
    """Вузол бінарного дерева."""

    def __init__(
        self,
        value=0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(root: Optional[TreeNode]) -> int:
    """Повернути суму глибин усіх вузлів у дереві."""
    return _accumulate(root, depth=0)


def _accumulate(node: Optional[TreeNode], depth: int) -> int:
    """Накопичити суму глибин у поддереві з коренем node."""
    if node is None:
        return 0
    return (
        depth
        + _accumulate(node.left, depth + 1)
        + _accumulate(node.right, depth + 1)
    )