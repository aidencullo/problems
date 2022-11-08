import time
import json
from solution import Solution

def test(input1, input2, output):
    s = Solution()
    result = s.coinChange(input1, input2)
    # only print if failed
    if result != output:
        print("array ", input1)
        print("amt: ", input2)
        print("FAILED: Expected: %d, Given: %d" % (output, result))

def test_suite(file):
    with open(file,'r') as file:
        for line in file:
            words=line.split()
            arg1=json.loads(words[0])
            arg2=int(words[1])
            arg3=int(words[2])
            start = time.time()
            test(arg1, arg2, arg3)
            end = time.time()
            print("Time: ",end - start)
