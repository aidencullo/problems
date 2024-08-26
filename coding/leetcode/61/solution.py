class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def next_node(node):
            while node:
                yield node
                node = node.next
        
        def count(node):
            return sum(1 for x in next_node(node))

        if not head:
            return None

        n = count(head)
        k %= n

        leader = head
        for i in range(k):
            leader = leader.next
        follower = head

        while leader.next:
            leader = leader.next
            follower = follower.next
        leader.next = head
        new_head = follower.next
        follower.next = None
        return new_head
