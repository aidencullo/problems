from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Node:
    val: int = 0
    left: Optional[Node] = None
    right: Optional[Node] = None
