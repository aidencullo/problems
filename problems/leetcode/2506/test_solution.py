import pytest
from solution import Solution

def test_similar_pairs_case1():
    words = ["aba", "aabb", "abcd", "bac", "aabc"]
    assert Solution().similarPairs(words) == 2

def test_similar_pairs_case2():
    words = ["aabb", "ab", "ba"]
    assert Solution().similarPairs(words) == 3

def test_similar_pairs_case3():
    words = ["nba", "cba", "dba"]
    assert Solution().similarPairs(words) == 0

def test_similar_pairs_edge_case1():
    words = ["a"]
    assert Solution().similarPairs(words) == 0

def test_similar_pairs_edge_case2():
    words = ["abc", "bca", "cab"]
    assert Solution().similarPairs(words) == 3

def test_similar_pairs_edge_case3():
    words = ["a", "b", "c", "d", "e"]
    assert Solution().similarPairs(words) == 0
