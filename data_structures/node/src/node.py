from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Node:
    val: int = 0
    left: Node = None
    right: Node = None
