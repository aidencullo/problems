import sys

class Solution:
    min_global = sys.maxsize
    min_local = 0
    def jump(self, nums: list[int]) -> int:
#        print("jump")
#        print("min_global: ", self.min_global)
#        print("min_local: ", self.min_local)
        nlen = len(nums)
        if nlen == 1:
            self.min_global = min(self.min_global, self.min_local)
            return 0
        if nums[0] == 0:
            return sys.maxsize
        if self.min_local == self.min_global-1:
            return sys.maxsize
        current = nums[0]
        min_of_min = sys.maxsize
        self.min_local = self.min_local + 1
#        print("nlen", nlen)
        for x in reversed(range(1, current + 1)):
            #print(x)
    # check if the jump is too long
            if x < nlen-1:
                min_of_min = min(min_of_min, self.jump(nums[x:]))
            else:
                # here we have found another path
                self.min_global = min(self.min_global, self.min_local)
                min_of_min = self.min_local
                break
        self.min_local = self.min_local - 1
#        print("num: ",current)
#        print("min_of_min: ", min_of_min)
        return min_of_min
