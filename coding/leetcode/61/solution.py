class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def next_node(node):
            while node:
                yield node
                node = node.next
        
        def count(node):
            return sum(1 for x in next_node(node))

        if not head or head.next is None:
            return head

        n = count(head)
        k %= n

        if k == 0:
            return head

        fast = slow = head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast, slow = fast.next, slow.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
