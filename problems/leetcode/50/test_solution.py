import math
import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((2.00000, -2147483648), 0.00000),
    ((2.00000, 10), 1024.00000),
    ((2.10000, 3), 9.26100),
    ((2.00000, -2), 0.25000),
    ((2.00000, 0), 1.00000),
    ((2.00000, 1), 2.00000),
    ((2.00000, -1), 0.50000),
    ((2.00000, 2), 4.00000),
    ((2.00000, 3), 8.00000),
    ((2.00000, 4), 16.00000),
    ((2.00000, 5), 32.00000),
    ((2.00000, 6), 64.00000),
    ((2.00000, 7), 128.00000),
    ((2.00000, 8), 256.00000),
    ((2.00000, 9), 512.00000),
    ((2.00000, 10), 1024.00000),
    ((2.00000, 11), 2048.00000),
    ((2.00000, 12), 4096.00000),
    ((2.00000, 13), 8192.00000),
    ((2.00000, 14), 16384.00000),
    ((2.00000, 15), 32768.00000),
    ((2.00000, 16), 65536.00000),
    ((2.00000, 17), 131072.00000),
    ((2.00000, 18), 262144.00000),
    ((2.00000, 19), 524288.00000),
    ((2.00000, 20), 1048576.00000),
    ((2.00000, 21), 2097152.00000),
    ((2.00000, 22), 4194304.00000),
    ((2.00000, 23), 8388608.00000),
    ((2.00000, 24), 16777216.00000),
])
def test_solution(test_input, expected):
    assert math.isclose(Solution().myPow(*test_input), expected, rel_tol=1e-9)
