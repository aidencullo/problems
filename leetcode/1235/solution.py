from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        profit = sort_by(endTime, profit)
        startTime = sort_by(endTime, startTime)
        endTime.sort()
        dp = [0] * len(endTime)
        for i in range(len(endTime)):
            target_start = startTime[i]
            j = search_end(endTime, target_start)
            max_profit = dp[j] if j >= 0 else 0
            if i == 0:
                dp[i] = profit[i]
            else:
                dp[i] = max(dp[i - 1], max_profit + profit[i])
        return dp[-1]

def sort_by(Y, X):
        return [x for _, x in sorted(zip(Y, X), key=lambda pair: pair[0])]

def search_end(items, target):
    return search(items, target, 0, len(items) - 1)

def search(lst, target, left, right):
    if left > right:
        return right
    k = (left + right) // 2
    middle = lst[k]
    if middle <= target:
        return search(lst, target, k + 1, right) 
    if middle > target:
        return search(lst, target, left, k - 1)
