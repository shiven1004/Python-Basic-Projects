from queue import Queue

initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
goal_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]


def is_goalState(state):
    return state == goal_state


def possible_moves(state):
    moves = []
    zero_index = state.index(0)

    if zero_index % 3 != 0:
        moves.append('left')

    if zero_index % 3 != 2:
        moves.append('right')

    if zero_index // 3 != 0:
        moves.append('up')

    if zero_index // 3 != 2:
        moves.append('down')

    return moves


def move_zeroTile(state, move):
    zero_index = state.index(0)
    new_state = list(state)

    if move == 'left':
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]

    elif move == 'right':
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]

    elif move == 'up':
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]

    elif move == 'down':
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]

    return new_state


def bfs():
    open_set = Queue()
    open_set.put((initial_state, []))
    closed_set = set()

    while not open_set.empty():
        current_state, current_moves = open_set.get()

        if is_goalState(current_state):
            return current_moves

        closed_set.add(tuple(current_state))

        for move in possible_moves(current_state):
            new_state = move_zeroTile(current_state, move)
            if tuple(new_state) not in closed_set:
                open_set.put((new_state, current_moves + [move]))

    return None


def dfs():
    stack = [(initial_state, [])]
    closed_set = set()

    while stack:
        current_state, current_moves = stack.pop()

        if is_goalState(current_state):
            return current_moves

        closed_set.add(tuple(current_state))

        for move in reversed(possible_moves(current_state)):
            new_state = move_zeroTile(current_state, move)
            if tuple(new_state) not in closed_set:
                stack.append((new_state, current_moves + [move]))

    return None


def display_state(state, move=None):
    if move:
        print("After Move: ", move)
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def display_path(m):
    state = initial_state
    for move in m:
        state = move_zeroTile(state, move)
        display_state(state, move)


moves = dfs()
print("Initial State:")
for i in range(0, 9, 3):
    print(initial_state[i:i+3])
print()
if moves:
    print("Shortest Path: ", moves)
    display_path(moves)

else:
    print("No Solution Found!")



