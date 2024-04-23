class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, item: int) -> None:
        self.heap.append(item)
        self.heapify_up()
    
    def delete(self, data) -> None:
        data_index = self.heap.index(data)
        self.swap(data_index, len(self.heap) - 1)
        self.heap.pop()
        self.heapify_down(data_index)
    
    def get_min(self) -> int:
        return self.heap[0]

    def extract_min(self) -> int:
        data = self.heap[0]
        self.delete(self.heap[0])
        return data
    
    def heapify_up(self):
        index = len(self.heap) - 1
        while self.has_parent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)
    
    def heapify_down(self, index: int=0) -> None:
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if (self.has_right_child(index)
                and self.right_child(index) < self.heap[smaller_child_index]):
                smaller_child_index =  self.get_right_child_index(index)
            if self.heap[index] < self.heap[smaller_child_index]:
                break
            self.swap(index, smaller_child_index)
            index = smaller_child_index

    def swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, index: int) -> bool:
        return self.heap[self.get_parent_index(index)]

    def left_child(self, index: int) -> bool:
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index: int) -> bool:
        return self.heap[self.get_right_child_index(index)]

    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) > -1

    def has_left_child(self, index: int) -> bool:
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index: int) -> bool:
        return self.get_right_child_index(index) < len(self.heap)

    def get_parent_index(self, index: int) -> int:
        return (index-1) // 2

    def get_left_child_index(self, index: int) -> int:
        return index * 2 + 1

    def get_right_child_index(self, index: int) -> int:
        return index * 2 + 2

    def is_empty(self) -> int:
        return not self.heap
