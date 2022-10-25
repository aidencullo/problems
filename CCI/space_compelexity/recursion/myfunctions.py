import time

def summ(n):
    if n <= 0:
        return 0
    else:
        return 1 + summ(n-1)

def take_time(k):
    start = time.time()
    summ(k)
    end = time.time()
    print("Time ", k, ": ", end - start)
