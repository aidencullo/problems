class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(height, i) for i, height in enumerate(heights)]
        people.sort(reverse=True)
        return [names[i] for height, i in people]
