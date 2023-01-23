from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        currentMax=0
        for index, value  in enumerate(height):
            if(index == 0):
                continue
            currentMax = max(self.maxAreaHelper(height[:index + 1]), currentMax)
        return currentMax
    def maxAreaHelper(self, height: List[int]) -> int:
        currentMax=0
        for index, value in enumerate(height):
            currentMax = max(currentMax, self.getArea(index, height))
        return currentMax

    def getArea(self, start, array):
        height = min(array[start], array[len(array) - 1])
        return height * (len(array) - 1 - start)

tests = []
test1 = [1,8,6,2,5,4,8,3,7]
test2 = [1, 1]
tests.append(test1)
tests.append(test2)
answers = []
answer1 = 49
answer2 = 1
answers.append(answer1)
answers.append(answer2)

s=Solution()
for e in enumerate(tests):
    ans = s.maxArea(e[1])
    print("test %d: %r, expected: %d given: %d" % (e[0], ans == answers[e[0]], answers[e[0]], ans))
