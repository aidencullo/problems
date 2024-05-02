from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        before_head = ListNode(0)
        before_head.next = head

        runner = self.move_to_left(before_head, left)
        self.remove_nodes(stack, runner, left, right)
        self.insert_nodes(stack, runner)

        return before_head.next

    def insert_nodes(self, stack, runner):
        while stack:
            self.insert_right(runner, stack.pop())
            runner = runner.next

    def remove_nodes(self, stack, runner, left, right):
        i = left
        while i <= right:
            stack.append(self.delete_right(runner))
            i += 1
            
    def move_to_left(self, node, left):
        i = 1
        runner = node
        while i < left:
            runner = runner.next
            i += 1
        return runner

    def delete_right(self, node):
        tmp = node.next
        node.next = node.next.next
        tmp.next = None
        return tmp

    def insert_right(self, head, node):
        node.next = head.next
        head.next = node

    def print(self, head):
        runner = head
        while runner:
            print(runner.val)
            runner = runner.next
