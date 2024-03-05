import pytest

from src.bfs import bfs
from graph import NodeGraph


test_data = [
    pytest.param({
        1: [2,],
        2: [3,],
        3: [],
    }, [1, 2, 3], id="linear"),
    pytest.param({
        1: [2,],
        2: [3,],
        3: [1,],
    }, [1, 2, 3], id="cyclic"),
    pytest.param({
        1: [2, 3, 4],
        2: [4, 3, 1],
        3: [1, 2, 4],
        4: [2, 3, 1],
    }, [1, 2, 3, 4], id="complete"),
    pytest.param({
        1: [2, 3],
        2: [4],
        3: [],
        4: [],
    }, [1, 2, 3, 4], id="simple"),
    pytest.param({
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: [],
    }, [1, 2, 3, 4, 5], id="tree"),
]


class TestBFS:

    @pytest.mark.parametrize(
        ('test_input', 'expected'),
        test_data,
    )
    def test_bfs(self, test_input, expected):
        ng = NodeGraph(test_input)
        assert bfs(ng.get_root()) == expected
