DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def dfs(g):
    m = len(g)
    n = len(g[0])
    
    def traverse(r, c):
        if not g[r][c]:
            return

        process(r, c)
        visit(r, c)

        for dr, dc in DIRECTIONS:
            if is_valid(r + dr, c + dc):
                traverse(r + dr, c + dc)

    def visit(r, c):
        g[r][c] = 0

    def is_valid(r, c):
        return (0 <= r < m
                and 0 <= c < n)

    def visited(r, c):
        return not g[r][c]

    def process(r, c):
        print(g[r][c], end='')

    for i in range(m):
        for j in range(n):
            traverse(i, j)











            
from collections import deque
            
def bfs(g):
    m = len(g)
    n = len(g[0])
    
    def traverse(r_src, c_src):
        q = deque()
        q.append((r_src, c_src))

        while q:
            r, c = q.popleft()
            if visited(r, c): continue
            process(r, c)
            visit(r, c)

            for dr, dc in DIRECTIONS:
                if is_valid(r + dr, c + dc):
                    q.append((r + dr, c + dc))

    def visit(r, c):
        g[r][c] = 0

    def process(r, c):
        print(g[r][c], end='')

    def visited(r, c):
        return not g[r][c]

    def is_valid(r, c):
        return (0 <= r < m
                and 0 <= c < n)

    for i in range(m):
        for j in range(n):
            traverse(i, j)
            










def dfs_with_stack(g):
    m = len(g)
    n = len(g[0])
    
    def traverse(r_src, c_src):
        q = []
        q.append((r_src, c_src))

        while q:
            r, c = q.pop()
            if visited(r, c): continue
            process(r, c)
            visit(r, c)

            for dr, dc in DIRECTIONS:
                if is_valid(r + dr, c + dc):
                    q.append((r + dr, c + dc))

    def visit(r, c):
        g[r][c] = 0

    def is_valid(r, c):
        return (0 <= r < m
                and 0 <= c < n)

    def visited(r, c):
        return not g[r][c]

    def process(r, c):
        print(g[r][c], end='')

    for i in range(m):
        for j in range(n):
            traverse(i, j)
            







graph = [
    [1,2],
    [4,3],
]

print()
dfs_with_stack(graph) # 1,2,3,4
print()
