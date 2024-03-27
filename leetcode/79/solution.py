from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, word_index):
            if (r, c) in seen:
                return False
            if board[r][c] != word[word_index]:
                return False
            if word_index == len(word) - 1:
                return True
            seen.add((r, c))
            for dr, dc in directions:
                if 0 <= r + dr < n and 0 <= c + dc < m:
                    if dfs(r + dr, c + dc, word_index + 1):
                        return True
            seen.remove((r, c))

        start_indices = []
        first_letter = word[0]
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == first_letter:
                    start_indices.append((i, j))
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row, col in start_indices:
            seen.clear()
            if dfs(row, col, 0):
                return True
        return False
