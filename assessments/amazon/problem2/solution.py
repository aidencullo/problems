from collections import deque

def minimumDistance(area):
    q = deque()
    q.append((0,0,0))
    visited = set()
    visited.add((0,0))
    while q:
        qlen = len(q)
        for i in range(qlen):
            x, y, steps = q.popleft()
            if x < 0 or y < 0 or x >= len(area) or y >= len(area[0]) or area[x][y] == 0:
                continue
            if area[x][y] == 9:
                return steps
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                if (x+dx, y+dy) not in visited:
                    q.append((x+dx, y+dy, steps+1))
                    visited.add((x+dx, y+dy))
    return -1
            
