# O(n^3)

# import math

# def main():
#     N = 1000
#     for a in range(1, N + 1):
#         for b in range(1, N + 1):
#             for c in range(1, N + 1):
#                 d = mypow(a**3 + b**3 - c**3, 1/3)
#                 if a**3 + b**3 == c**3 + d**3:
#                     print(f'{a, b, c, d}')

# def mypow(base, exp):
#     if base < 0:
#         result = -((-base) ** exp)
#     else:
#         result = base ** exp
#     return math.floor(result)


# if __name__ == "__main__":
#     main()

import math

def main():
    N = 1000
    hash_map = {}
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            hash_map.setdefault(a**3 + b**3, []).append((a, b))
    for item in hash_map.values():
        print(f'{item}')

def mypow(base, exp):
    if base < 0:
        result = -((-base) ** exp)
    else:
        result = base ** exp
    return math.floor(result)


if __name__ == "__main__":
    main()
