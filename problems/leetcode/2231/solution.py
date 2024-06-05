import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        even_heap = []
        odd_heap = []
        digits = [int(letter) for letter in  str(num)]
        for digit in digits:
            if digit % 2 == 0:
                even_heap.append(-digit)
            else:
                odd_heap.append(-digit)
        heapq.heapify(even_heap)
        heapq.heapify(odd_heap)
        res = []
        for digit in digits:
            if digit % 2 == 0:
                res.append(-heapq.heappop(even_heap))
            else:
                res.append(-heapq.heappop(odd_heap))
        return int("".join(map(str, res)))
