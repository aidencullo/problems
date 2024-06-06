class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            weight1 = -heapq.heappop(stones)
            weight2 = -heapq.heappop(stones)
            if weight1 != weight2:
                heapq.heappush(stones, -(weight1 - weight2))
        return -stones[0] if stones else 0
