import pytest

def compare_bin_hex(binary: str, hexadecimal: str):
    hex_base_10 = convert_from_base(hexadecimal, 16)
    bin_base_10 = convert_from_base(binary, 2)
    return hex_base_10 == bin_base_10


def convert_from_base(hexadecimal: str, base: int):
    total = 0
    for i, digit in enumerate(hexadecimal):
        value = digit_to_value(digit)
        total += base ** (len(hexadecimal) - 1 - i) * value
    return total

        
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

def digit_to_value(num):
    if num not in digits_to_values:
        raise ValueError(f"Invalid digit: {num}")
    return digits_to_values[num]


test_input = [
    ("10", "2", True),
    ("10000", "10", True),
    ("10001", "10", False),
    ("0001000100010001", "1111", True),
]

def test(binary, hexadecimal, expected):
    print(f"Testing: {binary}, {hexadecimal}, {expected}")
    assert compare_bin_hex(binary, hexadecimal) == expected

for binary, hexadecimal, expected in test_input:
    test(binary, hexadecimal, expected)
