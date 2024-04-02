class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, el) -> None:
        self.heap.append(el)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        self.swap(0, -1)
        min_el = self.heap.pop()
        self._heapify_down(0)
        return min_el

    def peek(self) -> int:
        return None if not self.heap else self.heap[0]

    def _heapify_up(self, index) -> None:
        parent_index = (index - 1) // 2
        if parent_index < 0:
            return
        if self.heap[parent_index] > self.heap[index]:
            self.swap(index, parent_index)
            self._heapify_up(parent_index)

    def swap(self, i, j) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def _heapify_down(self, index) -> None:
        left_child_index = index * 2 + 1
        if left_child_index >= len(self.heap):
            return
        right_child_index = index * 2 + 2
        if right_child_index >= len(self.heap):
            min_child_index = left_child_index
        else:
            min_child_index = min((left_child_index, right_child_index),
                              key=lambda x: self.heap[x])
        if self.heap[min_child_index] < self.heap[index]:
            self.swap(index, min_child_index)
            self._heapify_down(min_child_index)
