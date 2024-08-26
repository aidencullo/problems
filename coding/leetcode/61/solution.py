class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def count(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        if not head:
            return None
        n = count(head)
        k %= n
        m = n - k
        m %= n

        runner = head
        for _ in range(m - 1):
            runner = runner.next

        new_head = runner.next
        runner.next = None

        runner = new_head

        while runner.next:
            runner = runner.next

        runner.next = head

        return new_head
