from collections import deque

start = (1,2,3,
        4,5,6,
        7,0,8)

goal = (1,2,3,
        4,5,6,
        7,8,0)

queue = deque([start])
visited = set()

moves = [-3,3,-1,1]

while queue:
    state = queue.popleft()
    if state in visited:
        continue
    visited.add(state)
    print(state)

    if state == goal:
        print('Goal reached')
        break

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    for move in moves:
        new_pos = zero + move

        if new_pos < 0 or new_pos > 8:
            continue
        if col == 0 and move == -1:
            continue
        if col == 2 and move == 1: 
            continue

        new_state = list(state)
        new_state[zero], new_state[new_pos] = (
            new_state[new_pos], new_state[zero]
        ) 
        new_state = tuple(new_state)

        if new_state not in visited:
            queue.append(new_state)

print(len(visited))