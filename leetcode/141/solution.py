from typing import Optional

from util import ListNode

# O(n) time, O(1) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        runner = head
        skipper = head
        while skipper:
            if not skipper.next:
                return False
            skipper = skipper.next
            if not skipper.next:
                return False
            skipper = skipper.next
            runner = runner.next
            if runner == skipper:
                return True
        return False
