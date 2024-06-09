from solution import Solution, Node


def test_solution():
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert Solution().printBoundaryView(tree) == [1, 2, 4, 5, 3]

# def test_solution_1():
#     tree = Node(1, Node(2, Node(4, Node(6), Node(5)), Node(9, right=Node(3, Node(7), Node(8)))))
#     assert Solution().printBoundaryView(tree) == [1, 2, 4, 6, 5, 7, 8]


