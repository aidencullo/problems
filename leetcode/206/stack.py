from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Stack:
    items: list[int] = field(default_factory=list)

    def __len__(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()
        
    def push(self, item):
        return self.items.append(item)
