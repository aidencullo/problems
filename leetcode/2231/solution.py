import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        even_heap = []
        odd_heap = []
        digits = [-int(digit) for digit in  str(num)]

        for digit in digits:
            if digit % 2 == 0:
                heapq.heappush(even_heap, digit)
            else:
                heapq.heappush(odd_heap, digit)

        res = 0
        for digit in digits:
            if digit % 2 == 0:
                optimal_digit = -heapq.heappop(even_heap)
            else:
                optimal_digit = -heapq.heappop(odd_heap)
            res *= 10
            res += optimal_digit
        return res
