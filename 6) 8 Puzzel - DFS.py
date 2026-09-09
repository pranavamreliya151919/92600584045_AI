#Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

#Function to print the puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print (state[i:i+3])
    print()

#Generate possible moves
# Order: Up -> Down -> Left -> Right
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves= [(-1 , 0), (1, 0), (0, -1), (0, 1)] #Up, Down, Right, Left

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors

#BFS Algorithm
def bfs(start):
    stack = [(start, [])] #Simple Queue
    visited = {start}

    while stack:
        state, path = stack.pop() #remove first item

        if state == goal:
            return path + [state]

        neighbors = get_neighbors(state)

        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [state]))

    return None

#Example start state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = bfs(start)

if solution:
    print("Solution found in",len(solution)-1, "Mves:\n")

    for step in solution:
        print_board(step)
else:
    print("NO Solution Found")
