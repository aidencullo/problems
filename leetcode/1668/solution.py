class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        pass

    def create_prefix_table(self, pattern: str) -> list:
        m = len(pattern)
        prefix = [0] * m
        for i in range(m):
            if i > 0:
                last = pattern[prefix[i - 1]]
                if pattern[i] == last:
                    prefix[i] = prefix[i - 1] + 1
                else:
                    if prefix[prefix[i - 1]] > 0:
                        prefix[i] = prefix[prefix[i - 1]] - 1
        return prefix

def test_prefix_table():
    test_cases = [
        ("aabaab", [0, 1, 0, 1, 2, 3]),
        ("abcabc", [0, 0, 0, 1, 2, 3]),
        ("aaaaa", [0, 1, 2, 3, 4]),
        ("ababab", [0, 0, 1, 2, 3, 4]),
        ("aabaabaaa", [0, 1, 0, 1, 2, 3, 4, 5, 2]),
        ("", []),
        ("a", [0]),
        ("abcde", [0, 0, 0, 0, 0])
    ]
    
    s = Solution()
    for pattern, expected in test_cases:
        result = s.create_prefix_table(pattern)
        assert result == expected, f"Failed for pattern '{pattern}': expected {expected}, got {result}"
        print(f"Test passed for pattern '{pattern}': {result}")

def test_maxRepeating():
    test_cases = [
        ("aaaa", "a", 4),
        ("abababab", "ab", 4),
        ("ababc", "ab", 2),
        ("ababc", "ba", 1),
        ("ababc", "ac", 0),
        ("", "abc", 0),
        ("abc", "", 0)
    ]
    
    s = Solution()
    for sequence, word, expected in test_cases:
        result = s.maxRepeating(sequence, word)
        assert result == expected, f"Failed for sequence='{sequence}', word='{word}': expected {expected}, got {result}"
        print(f"Test passed for sequence='{sequence}', word='{word}': {result}")

if __name__ == "__main__":
    print("Testing prefix table creation:")
    test_prefix_table()
    print("\nTesting maxRepeating function:")
    # test_maxRepeating() 

