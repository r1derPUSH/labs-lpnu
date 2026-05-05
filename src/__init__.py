"""
Лабораторна робота 2, Рівень 1, Варіант 2.

Завдання: спростити вивід інформації про зайнятість команди в календарі.
"""

from typing import List, Tuple


def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Об'єднати суміжні та перекривні інтервали зайнятості."""
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda pair: pair[0])
    merged: List[Tuple[int, int]] = [sorted_intervals[0]]

    for current_start, current_end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged