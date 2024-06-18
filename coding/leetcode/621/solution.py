# time: O(N)
# space: O(1)

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = [0] * 26
        for task in tasks:
            task_count[ord(task) - ord('A')] += 1
        task_count.sort()
        max_val = task_count[-1] - 1
        idle_slots = max_val * n
        for i in range(24, -1, -1):
            idle_slots -= min(task_count[i], max_val)
        return max(idle_slots, 0) + sum(task_count)
