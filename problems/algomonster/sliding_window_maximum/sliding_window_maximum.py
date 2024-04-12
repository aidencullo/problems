import math

def max_sliding_window(arr, k):
    max_windows = []
    for i in range(len(arr)-k+1):
        max_window = -math.inf
        for j in range(k):
            max_window = max(max_window, arr[i + j])
        max_windows.append(max_window)
    return max_windows                             
