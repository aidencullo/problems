from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def distributeCookiesHelper(bags: List[int], cookie_index: int) -> int:
            if cookie_index == len(cookies):
                self.unfairness = min(max(bags), self.unfairness)
                return
            cookie = cookies[cookie_index]
            for j in range(k):
                bags[j] += cookie
                distributeCookiesHelper(bags, cookie_index + 1)
                bags[j] -= cookie
        if k == len(cookies):
            return max(cookies)
        bags = [0] * k
        self.unfairness = float('inf')
        distributeCookiesHelper(bags, 0)
        return self.unfairness
