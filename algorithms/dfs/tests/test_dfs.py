import pytest

from src.dfs import dfs
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
    }, [1, 2, 4, 3], id="complete"),
    pytest.param({
        1: [2, 3],
        2: [4],
        3: [],
        4: [],
    }, [1, 2, 4, 3], id="simple"),
    pytest.param({
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: [],
    }, [1, 2, 4, 5, 3], id="tree"),
]


class TestDFS:

    @pytest.mark.parametrize(
        ('test_input', 'expected'),
        test_data,
    )
    def test_dfs(self, test_input, expected):
        ng = NodeGraph(test_input)
        assert dfs(ng.get_root()) == expected
