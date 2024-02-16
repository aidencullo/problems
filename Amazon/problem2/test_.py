import pytest

from solution import distinct_words

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (('xyz',), 4),
        (('abaa',), 4),
        (('aaaa',), 1),
        (('a',), 1),
        (('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',), 1),
        (('abcdefghijk',), 56),
        (('abcd',), 7),
        (('abcde',), 11),
        (('abcda',), 10),
        (('abcad',), 10),
        (('acbad',), 10),
        (('acabd',), 10),
        (('aacbd',), 10),
        (('aaabd',), 8),
        (('abca',), 6),
        (('bbabcbbbbbca',), 37),
        (('cbccabbabcbbabbbaaabacccacbbabbaabbcabbccababacbcbaabacbccabcbacbacbbcaabcaabbcccbbacbbbcacaaabbcbacaaabbbcacccacabccbcbbbbccaaacabbcbaccbbcbcbabbc',), 7141),
        (('bbabcbbbbbcacabaacbcccabacacbbcabbbccacbbcbacaacbcccacbbacbcaacaaacbaabcbabcbcacbcacccbbacbbcabaaaaccbbaacaaaacccbccbcaaccbcbbbcccbabcabccbaaacbacababbaaacaacccccaaacaccababaacaaacabacacacbcabaaacbbbaacbacacbabbcbcaccaacaabcbacbcaabcbccbcbbcbaccabcabcacbaabbcbcbcccacbbcbcaacacbaaacbbcccbabccbccaababcabcbccaabbbbabaccacaabcbbaaacacccaaaccabbcaabbcaabbabaccccbaabaaaacbcbbcaccccbccbcbbcaabcbaaabbbbcabcaabaacbbbcababcaabaccabbbbbaacbbbbabacbbabbccaaccbcaaaacaabaabccbbbcccabababcababaacacbcaabbbacaacaaabbbcaacbacbccbcbcbbbccaccaabccbbacabcabcbccbaacaaaaababbaacbbcbccacacccacbabccbbbccaacacabccbbabbbbbbaacaabcbaabbabccaccabbacbbbaabaaaccacbacccbabbaaccbccbcacccbabbccacaabbbabbcaaabbaccccaaaccccbcbaabcbaabaabacabbcbabbcbabaabcabbaaabacaaaacccacabbcacaaababbcbaaabbbbbccbacaaccbabaaabcaaabbbcaacabacaabbcbcacbbcbaabcbccabbabcbbabbbaaabacccacbbabbaabbcabbccababacbcbaabacbccabcbacbacbbcaabcaabbcccbbacbbbcacaaabbcbacaaabbbcacccacabccbcbbbbccaaacabbcbaccbbcbcbabbc',), 309640),
    ],
)
def test(test_input, expected):
    assert distinct_words(*test_input) == expected
