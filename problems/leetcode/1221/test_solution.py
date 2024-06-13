import pytest
from solution import Solution  # Assuming your solution is in a file named solution.py

sol = Solution()

def test_balancedStringSplit():
    assert sol.balancedStringSplit("RLRRLLRLRL") == 4
    assert sol.balancedStringSplit("RLLLLRRRLR") == 3
    assert sol.balancedStringSplit("LLLLRRRR") == 1
    assert sol.balancedStringSplit("") == 0
    assert sol.balancedStringSplit("RL") == 1
    assert sol.balancedStringSplit("RRRLLLRLRRLR") == 3
    assert sol.balancedStringSplit("RLRRRLLRLL") == 2

if __name__ == "__main__":
    pytest.main()
