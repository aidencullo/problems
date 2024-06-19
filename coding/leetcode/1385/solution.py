class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                distance += 1
        return distance
