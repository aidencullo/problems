class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if target >= arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        arr1.sort()
        arr2.sort()
        cnt = 0
        for x in arr1:
            upper = binary_search(arr2, x + d)
            lower = binary_search(arr2, x - d)
            if upper == lower:
                if lower > -1 and arr2[lower] == x - d:
                    continue
                cnt += 1
        return cnt
