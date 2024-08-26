class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def count(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        def get_tail(node):
            while node.next:
                node = node.next
            return node

        if not head:
            return None

        n = count(head)
        tail = get_tail(head)
        tail.next = head

        k %= n
        m = n - k

        runner = head
        for _ in range(m - 1):
            runner = runner.next

        new_head = runner.next
        runner.next = None
        return new_head
