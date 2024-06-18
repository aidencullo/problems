class Solution:
    def removeDuplicates(self, head):
        if not head:
            return None
        runner = head
        hash_set = set()
        while runner.next:
            hash_set.add(runner.data)
            if runner.next.data in hash_set:
                runner.next = runner.next.next
            else:
                runner = runner.next
        return head
