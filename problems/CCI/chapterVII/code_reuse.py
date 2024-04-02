import pytest

def  compare_bin_hex(binary: str, hexadecimal: str) -> bool:
    n1: int = bin_to_dec(binary)
    n2: int = hex_to_dec(hexadecimal)
    if n1 < 0 or n2 < 0:
        return False
    return n1 == n2

def bin_to_dec(num: str) -> int:
    return to_dec(num, 2)

def hex_to_dec(num: str) -> int:
    return to_dec(num, 16)

def to_dec(num: str, base: int) -> int:
    if base not in [2, 16]:
        return -1
    result = 0
    size = len(num)
    for i, el in enumerate(num):
        result += to_digit(el) * base ** (size - i - 1)
    return result

def to_digit(num):
    digits_to_values = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    return digits_to_values[num]
    

@pytest.mark.parametrize(
    ("binary", "hexadecimal", "expected",),
    [
        ("10", "2", True),
        ("10000", "10", True),
        ("10001", "10", False),
    ],
)
def test(binary, hexadecimal, expected):
    assert compare_bin_hex(binary, hexadecimal) == expected
