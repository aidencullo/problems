from solution import minimumDistance


def test_minimumDistance():
    assert minimumDistance([[1,0,0],[1,0,0],[1,9,1]]) == 3
    assert minimumDistance([
        [1,1,1,1],
        [0,1,1,1],
        [0,1,0,1],
        [1,1,9,1],
        [0,0,1,1]
    ]) == 5
