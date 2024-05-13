class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j = 0
        result = []
        stack = []
        for el in arr:
            if stack:
                result.append(stack.pop())
                continue
            if arr[j] == 0:
                result.append(0)
                stack.append(0)
                j += 1
                continue
            if arr[j] != 0:
                result.append(arr[j])
                j += 1
                continue
        arr[:] = result


"""
[0,1,2,3,4,5,6,7]
[0,1,7,6,0,2,0,7]
[0,0,1,7,6,0,2,0]
"""
                    
"""
constraints

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""

"""
COMMENTS

ints are only digits 0-9
we could use a constant mem array to store ints? -- not sure how that would help
"""

"""
APPROACH

brute-force:
1. iterate over list
2. if we encounter a 0, shift all the elements to the right of the zero down 1
	a. until we get to the last index which we cannot shift anymore
3. assign a zero to the position right of the last zero
4. look for another zero

this has O(n^2) complexity
"""
