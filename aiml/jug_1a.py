
from collections import deque

jug1 = 4
jug2 = 3

queue = deque([(0,0)])
visited = set()

while queue:
    x, y = queue.popleft()

    if (x,y) in visited:
        continue

    visited.add((x,y))
    print((x,y))

    states = [
        (jug1, 0),
        (0, jug2),
        (x, jug2),
        (jug1, y),
        ((x - min(x, jug2-y)), y + min(x, jug2-y)),
        ((x + min(y, jug1-x)), y - min(y, jug1-x))
    ]

    for state in states:
        if state not in visited:
            queue.append(state)

# Amount = min(
#     water available in Jug 1,
#     empty space in Jug 2
# )
# Source losses water and destonation gains water