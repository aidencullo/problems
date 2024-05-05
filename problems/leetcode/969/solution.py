from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr) - 1, -1, -1):
            largest_pancake = float('-inf')
            for j in range(i, -1, -1):
                if arr[j] > largest_pancake:
                    largest_pancake = arr[j]
                    largest_pancake_index = j
            if largest_pancake_index == i:
                continue
            arr[:largest_pancake_index + 1] = arr[:largest_pancake_index + 1][::-1]
            arr[:i + 1] = arr[:i + 1][::-1]
            res.append(largest_pancake_index + 1)
            res.append(i + 1)
        return res
