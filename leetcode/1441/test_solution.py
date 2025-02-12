from solution import Solution


def test_bst_from_preorder():
    sol = Solution()
    assert sol.buildArray([1, 3], 3) == ["Push", "Push", "Pop", "Push"]



# Example 1:

# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: Initially the stack s is empty. The last element is the top of the stack.
# Read 1 from the stream and push it to the stack. s = [1].
# Read 2 from the stream and push it to the stack. s = [1,2].
# Pop the integer on the top of the stack. s = [1].
# Read 3 from the stream and push it to the stack. s = [1,3].
# Example 2:

# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]
# Explanation: Initially the stack s is empty. The last element is the top of the stack.
# Read 1 from the stream and push it to the stack. s = [1].
# Read 2 from the stream and push it to the stack. s = [1,2].
# Read 3 from the stream and push it to the stack. s = [1,2,3].
# Example 3:

# Input: target = [1,2], n = 4
# Output: ["Push","Push"]
# Explanation: Initially the stack s is empty. The last element is the top of the stack.
# Read 1 from the stream and push it to the stack. s = [1].
# Read 2 from the stream and push it to the stack. s = [1,2].
# Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
# The answers that read integer 3 from the stream are not accepted.
