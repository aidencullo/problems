from typing import List, Optional
import heapq

from list_node import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [lst for lst in lists if lst]
        k_heap = Heap(lists)
        merged = ListNode(0)
        runner = merged
        while k_heap:
            runner.next = k_heap.delete_min()
            runner = runner.next
        return merged.next

class Heap:

    def __init__(self, lists: List[Optional[ListNode]]):
        self.heap = []
        self.heapify(lists)

    def heapify(self, lists) -> None:
        for node in lists:
            self.insert(node)            
    
    def insert(self, node: ListNode):
        self.heap.append(node)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, child_index: int) -> None:
        if child_index == 0:
            return
        parent_index = (child_index-1) // 2
        parent = self.heap[parent_index]
        child = self.heap[child_index]
        if parent.val > child.val:
            self.swap(parent_index, child_index)
            self.heapify_up(parent_index)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def delete_min(self) -> ListNode:
        self.swap(0, len(self.heap)-1)
        min_node = self.heap[-1]
        del self.heap[-1]
        if self.heap:
            self.heapify_down(0)
        if min_node.next:
            self.insert(min_node.next)
        min_node.next = None
        return min_node        

    def heapify_down(self, parent_index: int) -> None:
        left_child_index = parent_index * 2 + 1
        if left_child_index >= len(self.heap):
            return
        right_child_index = parent_index * 2 + 2
        parent = self.heap[parent_index]
        if right_child_index < len(self.heap):
            min_child_index = min(left_child_index, right_child_index, key=lambda x: self.heap[x].val)
        else:
            min_child_index = left_child_index
        min_child = self.heap[min_child_index]
        if parent.val > min_child.val:
            self.swap(parent_index, min_child_index)
            self.heapify_down(min_child_index)

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str([node.val for node in self.heap])

# nodes = [ListNode(10), ListNode(200, ListNode(1000)), ListNode(30)]
# h = Heap(nodes)
# while h:
#     n = h.delete_min()
#     print(n.val)
