from solution import Solution


def test_check_if_pangram():
    assert Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
    assert not Solution().checkIfPangram("leetcode")
