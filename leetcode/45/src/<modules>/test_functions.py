import time
import json
from solution import Solution

def test(input, output):
    s = Solution()
    result = s.jump(input)
    if result == output:
        print("input ", input)
        print("SUCCESS")
    else:
        print("input ", input)
        print("FAILED: Expected: %d, Given: %d" % (output, result))

def test_suite():
    with open('tests.txt','r') as file:
        for line in file:
            words=line.split()
            arg1=json.loads(words[0])
            arg2=int(words[1])
            start = time.time()
            test(arg1, arg2)
            end = time.time()
            print("Time: ",end - start)
