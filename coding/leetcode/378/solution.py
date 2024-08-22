def print_double_list(double_list):
    for row in double_list:
        print(row)

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        def count(m):
            i = n - 1
            j = 0
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= m:
                    j += 1
                    cnt += i + 1
                else:
                    i -= 1
            return cnt


        def bisect(m):
            i = n - 1
            j = 0
            kth = float('-inf')
            while i >= 0 and j < n:
                if matrix[i][j] <= m:
                    kth = max(kth, matrix[i][j])
                    j += 1
                else:
                    i -= 1
            return kth


        n = len(matrix)
        lower = matrix[0][0]
        upper = matrix[-1][-1]

        while lower <= upper:
            mid = (upper + lower) // 2
            if count(mid) == k:
                return bisect(mid)
            if count(mid) < k:
                lower = mid + 1
            if count(mid) > k:
                upper = mid - 1
        return lower
