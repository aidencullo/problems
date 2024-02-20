import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('anagram', 'nagaram'), True),
        (('rat', 'car'), False),
        (('rat', 'tar'), True),
    ],
)
def test_(test_input, expected):
    # Arrange

    # Act
    result = Solution().isAnagram(*test_input)

    # Assert    
    assert result == expected
