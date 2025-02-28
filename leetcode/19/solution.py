from typing import Optional



def getLength(node):
    n = 0
    while node:
        n += 1
        node = node.next
    return n
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length_of_list = getLength(head)
        k = length_of_list - n
        pre_head = ListNode(next=head)
        runner = pre_head
        for x in range(k):
            runner = runner.next
        
        if runner.next is None:
            pre_head = pre_head.next
        else:
            runner.next = runner.next.next

        return pre_head.next
    