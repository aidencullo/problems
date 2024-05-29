class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        stack = []
        for i, __ in enumerate(words):
            while stack and groups[stack[-1]] == groups[i]:
                stack.pop()
            stack.append(i)
        return [words[i] for i in stack]
