# problem: how many possible ways are there to get to stair x = 7, with 1 or 2 steps

def climb(n=7):
    if (n == 0):
        return 0;
    if (n == 1):
        return 1;
    if (n == 2):
        return 2;
    return climb(n-1) + climb(n-2);

print(climb())
