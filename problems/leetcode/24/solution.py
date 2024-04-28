from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0, head)
        runner = new_head
        while runner.next and runner.next.next:
            removed = self.remove_next(runner)
            runner = runner.next
            self.insert_next(runner, removed)
            runner = runner.next
        self.print(new_head)
        return new_head.next

    def remove_next(self, node) -> ListNode:
        tmp = node.next
        node.next = node.next.next
        return tmp

    def insert_next(self, node, target_node) -> None:
        target_node.next = node.next
        node.next = target_node
