class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        j = 0
        res = []
        for i in range(1, n + 1):
            if target[j] == i:
                res.append("Push")
                j += 1
            else:
                res.append("Push")
                res.append("Pop")
            if j == len(target):
                break
        return res
            
