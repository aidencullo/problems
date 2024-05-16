from collections import Counter

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_counter = Counter(students)
        stack = sandwiches[::-1]
        while stack and students_counter[stack[-1]]:
            students_counter[stack.pop()] -= 1
        return students_counter.total()
        

"""
how do we use stack?
or queue?

first off, constraints

1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.


best time complexity ?
certainly m + n

can we get that? why or why not?

APPROACH

run through students, count how many 0s and 1s
run through sandwiches, count how many 0s and 1s
return the difference

may i implement this?
"""
