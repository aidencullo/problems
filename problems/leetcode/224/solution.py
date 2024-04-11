class Solution:
    def calculate(self, s: str) -> int:
        while s:
            cur = self.next_expression(s)
