# time O(n^2)
# space O(n)

import math

def max_sliding_window(arr, k):
    max_windows = []
    for i in range(len(arr)-k+1):
        max_window = -math.inf
        for j in range(k):
            max_window = max(max_window, arr[i + j])
        max_windows.append(max_window)
    return max_windows                             



# time O(n * k * logk)
# space O(n + k)
import heapq

def max_sliding_window(arr, k):
    max_windows = []
    for i in range(len(arr)-k+1):
        heap = arr[i:i+k]
        heap = [-h for h in heap]
        heapq.heapify(heap)
        max_windows.append(-heapq.heappop(heap))
    return max_windows                             




# time O(n)
# space O(n + k)

from collections import deque

def max_sliding_window(arr, k):
    max_windows = []
    d = deque()
    for i in range(len(arr)):
        if i > k - 1:
            if d[0] == arr[i-k]:
                d.popleft()
        while d and d[-1] <= arr[i]:
            d.pop()
        d.append(arr[i])
        if i >= k - 1:
            max_windows.append(d[0])
    return max_windows                             
