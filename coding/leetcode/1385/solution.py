class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def search(target, arr): #O(logm)
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        def search2(target, arr): #O(logm)
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        arr1.sort() #O(nlogn)
        arr2.sort() #O(mlogm)
        cnt = 0
        for x in arr1: #O(n)
            upper = search(x + d, arr2) #O(logm)
            lower = search2(x - d, arr2) #O(logm)
            if upper < lower:
                cnt += 1
        return cnt
