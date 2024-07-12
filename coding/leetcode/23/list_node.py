class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    # def __le__(self, other):
    #     return self.val <= other.val

    # def __eq__(self, other):
    #     return self.val == other.val

    # def __ne__(self, other):
    #     return self.val != other.val

    # def __gt__(self, other):
    #     return self.val > other.val

    # def __ge__(self, other):
    #     return self.val >= other.val
