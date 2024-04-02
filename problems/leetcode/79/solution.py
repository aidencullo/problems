# time: O(n * m * 4^s) where n is the number of rows, m is the number of columns, and s is the length of the word
# space: O(s + n * m)

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, word_index): # O(4^s)
            if (r, c) in seen:
                return False
            if board[r][c] != word[word_index]:
                return False
            if word_index == len(word) - 1:
                return True
            seen.add((r, c)) # O(1), O(m*n) worst case
            for dr, dc in directions:
                if 0 <= r + dr < n and 0 <= c + dc < m:
                    if dfs(r + dr, c + dc, word_index + 1):
                        return True
            seen.remove((r, c)) # same O as add


        start_indices = [] # O(1)
        first_letter = word[0] # O(1)
        n = len(board) # O(1)
        m = len(board[0]) # O(1)
        for i in range(n): # O(n)
            for j in range(m): # O(m)
                if board[i][j] == first_letter:
                    start_indices.append((i, j)) # O(1)
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row, col in start_indices: # O(n*m)
            if dfs(row, col, 0):
                return True
        return False
