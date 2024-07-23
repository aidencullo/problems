from solution import Solution


def test_bst_from_preorder():
    sol = Solution()

    # Test case 1
    preorder = [8,5,1,7,10,12]
    result = sol.bstFromPreorder(preorder)
    expected = [8,5,10,1,7,None,12]
    assert result == expected

    # Test case 2
    preorder = [1,3]
    result = sol.bstFromPreorder(preorder)
    expected = [1,None,3]
    assert result == expected
