import pytest
from solution import Solution

def test_defangIPaddr():
    solution = Solution()
    assert solution.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert solution.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
    assert solution.defangIPaddr("192.168.0.1") == "192[.]168[.]0[.]1"
    assert solution.defangIPaddr("0.0.0.0") == "0[.]0[.]0[.]0"
    assert solution.defangIPaddr("127.0.0.1") == "127[.]0[.]0[.]1"
