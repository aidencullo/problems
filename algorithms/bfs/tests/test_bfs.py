import pytest

from src.bfs import bfs
from graph import NodeGraph
from node import Node


@pytest.mark.bfs
class TestBFS:

    @pytest.mark.parametrize(
        ('test_input', 'expected'),
        [
            ({
                1: [2,],
                2: [3,],
                3: [],
            }, [1, 2, 3]),
            ({
                1: [2,],
                2: [3,],
                3: [1,],
            }, [1, 2, 3]),
            ({
                1: [2, 3, 4],
                2: [1, 3, 4],
                3: [1, 2, 4],
                4: [1, 2, 3],
            }, [1, 2, 3, 4]),
        ]
    )
    def test_bfs(self, test_input, expected):
        ng = NodeGraph(test_input)
        assert bfs(ng.get_root()) == expected
