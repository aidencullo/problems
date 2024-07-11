class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        buckets = []
        for num in nums:
            idx = search(buckets, num)
            if idx == len(buckets):
                buckets.append(num)
            else:
                buckets[idx] = num
        return len(buckets)
