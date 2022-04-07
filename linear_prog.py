from pulp import *
import random

def getNeighbours(r, c, width, height, choices):
    r = int(r)
    c = int(c)
    acc = []

    # left
    if r > 0:
        r_str = str(r - 1)
        c_str = str(c)
        acc.append(choices[r_str][c_str])
    # right
    if r < width - 1:
        r_str = str(r + 1)
        c_str = str(c)
        acc.append(choices[r_str][c_str])
    # up
    if c > 0:
        r_str = str(r)
        c_str = str(c - 1)
        acc.append(choices[r_str][c_str])
    # down
    if c < height - 1:
        r_str = str(r)
        c_str = str(c + 1)
        acc.append(choices[r_str][c_str])
    # up-left
    if r > 0 and c > 0:
        r_str = str(r - 1)
        c_str = str(c - 1)
        acc.append(choices[r_str][c_str])
    # up-right
    if r > 0 and c < height - 1:
        r_str = str(r - 1)
        c_str = str(c + 1)
        acc.append(choices[r_str][c_str])
    # down-left
    if r < width - 1 and c > 0:
        r_str = str(r + 1)
        c_str = str(c - 1)
        acc.append(choices[r_str][c_str])
    #down-right
    if r < width - 1 and c < height - 1:
        r_str = str(r + 1)
        c_str = str(c + 1)
        acc.append(choices[r_str][c_str])

    return acc

def solution_to_string(choices, width, height):
    rows = [str(i) for i in range(width)]
    cols = [str(i) for i in range(height)]
    acc = ""
    for c in cols:
        acc += "\n"
        for r in rows:
            val = value(choices[r][c])
            acc += " # " if (val == 1) else " . "
    return acc

def board_to_string(board):
    acc = ""
    for row in board:
        acc += "\n"
        for item in row:
            acc += " # " if (item == 1) else " . "
    return acc

def gen_rand_board(width, height):
    acc = []
    for h in range(height):
        row = [random.randint(0,2) for i in range(width)]
        acc.append(row)
    return acc
        
def get_solution(width, height):
    
    board = gen_rand_board(width, height)
    rows = [str(i) for i in range(width)]
    cols = [str(i) for i in range(height)]

    choices = LpVariable.dicts("is_alive", (rows, cols), 0, 1, cat="Binary")
    or_variables = LpVariable.dicts("OR_variable", (rows, cols), 0, 1, cat="Binary")
    if_variables = LpVariable.dicts("IF_variable", (rows, cols), 0, 1, cat="Binary")

    prob = LpProblem("Game_of_Life_reversal", LpMinimize)
    prob += 0, "Arbitary Objective Function"

    for r in rows:
        for c in cols:
            cell = choices[r][c]
            neighbours = getNeighbours(r,c, width, height, choices)
            if board[int(c)][int(r)] == 1:
                #If it's alive, and it was previously alive, then it must've had 2 or 3 neighbours
                #If it's alive, and it was previously dead, then it must've had 3 neighbours
                prob += lpSum(neighbours) >= 3 - cell
                prob += lpSum(neighbours) <= 3

            else:
                #If it's dead, and was previously alive, then it must've had 0, 1 or 4+ neighbours
                #If it's dead, and was previously dead, then it must've had 0, 1, 2 or 4+ neighbours
                if len(neighbours) == 3:
                    #if you're on the corner
                    prob += lpSum(neighbours) >= 0
                    prob += lpSum(neighbours) <= 2 - cell
                else:
                    or_var = or_variables[r][c] # 1 if max is 1 or 2,
                                                # 0 if max = 9

                    if_var = if_variables[r][c] # 1 if or_var implies cell
                                                # 0 otherwise
                    
                    prob += if_var <= 1 - or_var + cell
                    prob += if_var >= 1 - or_var
                    prob += if_var >= cell

                    prob += lpSum(neighbours) >= 4 * (1 - or_var)
                    prob += lpSum(neighbours) <= 1 + (1 - if_var) + (len(neighbours) - 1) * (1 - or_var)


    prob.solve(PULP_CBC_CMD(msg=0))
    status = LpStatus[prob.status] == "Optimal"

    if status:
        return choices
    else:
        return None
    
if __name__ == "__main__":
    w = 5
    h = 6
    sol = get_solution(w, h)
    if sol:
        print(solution_to_string(sol, w, h))
    else:
        print("No solution found")
