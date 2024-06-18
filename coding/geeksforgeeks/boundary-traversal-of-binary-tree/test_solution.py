from solution import Solution, Node


def test_solution():
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert Solution().printBoundaryView(tree) == [1, 2, 4, 5, 3]
