from collections import deque

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and \
           (m == 0 or m >= c) and \
           (3-m == 0 or 3-m >= 3-c)

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    q = deque([(start, [start])])
    seen = {start}

    while q:
        (m,c,b), path = q.popleft()

        if (m,c,b) == goal:
            return path

        for dm,dc in moves:
            if b == 0:
                s = (m-dm, c-dc, 1)
            else:
                s = (m+dm, c+dc, 0)

            if valid(s[0],s[1]) and s not in seen:
                seen.add(s)
                q.append((s, path+[s]))

path = solve()

for i, s in enumerate(path):
    print(i, s)