from heapq import heappush, heappop
from itertools import chain

n = 3  # Size of the grid
row = [1, 0, -1, 0]  # Row movements: down, left, up, right
col = [0, -1, 0, 1]  # Column movements: down, left, up, right

def calculateManhattanCost(flattened_mat, flattened_final) -> int:
    """Calculate the Manhattan Distance."""
    cost = 0
    for i in range(len(flattened_mat)):
        if flattened_mat[i] != 0:
            # Find the goal position of the current tile in the final state
            target_index = flattened_final.index(flattened_mat[i])
            current_x, current_y = divmod(i, n)
            target_x, target_y = divmod(target_index, n)
            cost += abs(current_x - target_x) + abs(current_y - target_y)
    return cost

def isSafe(x, y):
    """Check if the new position is within bounds."""
    return 0 <= x < n and 0 <= y < n

def printMatrix(mat):
    """Print the 2D matrix."""
    for row in mat:
        print(' '.join(map(str, row)))
    print()

def printSolutionPath(steps):
    """Print each step in the solution path."""
    for step in steps:
        printMatrix(step)

def solve(initial, empty_tile_pos, final):
    """Solve the 8-puzzle problem using an optimized A* algorithm and print every step."""
    
    pq = []
    
    start_state = tuple(chain.from_iterable(initial))  # Flatten initial
    goal_state = tuple(chain.from_iterable(final))     # Flatten final

    visited = set()
    
    state_to_steps = {start_state: [initial]}  # Start state and initial steps
    
    cost = calculateManhattanCost(start_state, goal_state)
   
    heappush(pq, (cost, 0, 0, start_state, empty_tile_pos))
    while pq:

        total_cost, curr_cost, level, current_state, empty_pos = heappop(pq)
 
        if current_state == goal_state:
            print("Solution found! Steps to solve:")
            printSolutionPath(state_to_steps[current_state])
            return
         
        if current_state in visited:
            continue
         
        visited.add(current_state)
         
        for i in range(4):
            new_empty_x = empty_pos[0] + row[i]
            new_empty_y = empty_pos[1] + col[i]
             
            if isSafe(new_empty_x, new_empty_y):
                # Swap the empty tile with the target tile
                new_state_list = list(current_state)
                new_empty_index = new_empty_x * n + new_empty_y
                old_empty_index = empty_pos[0] * n + empty_pos[1]
                new_state_list[old_empty_index], new_state_list[new_empty_index] = new_state_list[new_empty_index], new_state_list[old_empty_index]  
                new_state = tuple(new_state_list)
                 
                if new_state not in visited: 
                    new_cost = calculateManhattanCost(new_state, goal_state)
                     
                    new_state_matrix = [list(new_state[i:i + n]) for i in range(0, len(new_state), n)]
                   
                    new_steps = state_to_steps[current_state] + [new_state_matrix]
                    state_to_steps[new_state] = new_steps
                    
                    heappush(pq, (new_cost + level + 1, new_cost, level + 1, new_state, [new_empty_x, new_empty_y]))
    print("No solution exists.")

initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

empty_tile_pos = [1, 2]

solve(initial, empty_tile_pos, final)
