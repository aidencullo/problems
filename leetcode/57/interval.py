from functools import total_ordering
from dataclasses import dataclass

    
@total_ordering
@dataclass(frozen=True, slots=True)
class Interval:
    lower: int
    upper: int

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return ((self.lower, self.upper)
                < (other.lower, other.upper))
