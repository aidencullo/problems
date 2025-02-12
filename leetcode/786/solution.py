class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        piles = dict.fromkeys(arr, len(arr)-1)
        for i in range(k):
            k = min(piles, key=lambda x: x/arr[piles[x]])
            piles[k] -= 1
            smallest = k
        return [smallest, arr[piles[smallest] + 1]]
