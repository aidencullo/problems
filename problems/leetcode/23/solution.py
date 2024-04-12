# time O(n*k)
# space O(k)

from typing import List, Optional
import math
import heapq

from list_node import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = ListNode(0)
        current = merged
        lists = [node for node in lists if node]
        while lists:
            min_num = math.inf
            for i, node in enumerate(lists):
                if node.val < min_num:
                    min_num = node.val
                    min_i = i
            current.next = ListNode(min_num)
            current = current.next
            lists[min_i] = lists[min_i].next
            lists = [node for node in lists if node]
        return merged.next
    
#         k_heap = Heap(lists)
#         merged_list = []
#         while k_heap:
#             merged_list.append(k_heap.pop())
#         return ListNode()

# class Heap:

#     def __init__(self, lists: List[Optional[ListNode]]):
#         self.heap = lists
#         self.heapify()

#     def heapify(self):

#     def insert(self, node: ListNode)
        
#     def pop(self):
#         pass

#     def __len__(self):
#         return len(self.heap)

#     def print_heap(self):
#         pass
