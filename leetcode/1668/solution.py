class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # Time: O(1), Space: O(1)
        n = len(sequence)
        
        # Time: O(1), Space: O(1)
        repeating = 0
        
        # Time: O(n), Space: O(1)
        for i in range(n + 1):
            # Time: O(i * m) where m is len(word), Space: O(i * m)
            current = i * word
            
            # Time: O(n), Space: O(m) - need space for pattern matching
            if current in sequence:
                # Time: O(1), Space: O(1)
                repeating = i
        
        # Time: O(1), Space: O(1)
        return repeating

    # Overall Time Complexity: O(n * m * n) = O(mn^2)
    # - Outer loop runs n times
    # - For each iteration, we create a string of length i*m
    # - String search operation takes O(n)
    # Overall Space Complexity: O(n * m)
    # - Maximum space used is when i = n, creating a string of length n*m

    