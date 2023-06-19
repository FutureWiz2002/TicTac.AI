grid1 = [
    ["-", "-", "-"], 
    ["-", "-", "-"],
    ["-", "-", "-"] ]
print(grid1)
# whose-turn takes in a grid and determines the player's turn. 

def whoseTurn(grid):
    counterO = 0
    counterX = 0
    turn = ""
    for i in grid:
        for j in i:
            if j == "X":
                counterX += 1
            elif j == "O":
                counterO += 1
    # print(counterX, counterO)
    if counterX == counterO:
        turn = "X"
    else: 
        turn = "O"
    return turn

#gridReference takes in a grid coords and produces the value in that coord

def gridReference(grid, x, y):
    columnX = grid[x]
    return columnX[y]

#getCol takes a grid gives the column

def getCol(grid, number):
    final = []
    for i in (range(3)):
        final.append(gridReference(grid, i, number))
    return final

#takeInput takes a grid row and determines if someone has won or not
def takeInput(grid, row, column, turn):
    newGrid = [row[:] for row in grid]
    newGrid[row][column] = turn
    return newGrid


# print(takeInput(grid1, 0, 0, "O"))
    
def logic(grid, turn): 
    for i in range(3):
        x = getCol(grid, i)
        if x[0] == turn and x[1] == turn and x[2] == turn:
            return True
    for i in range(3):
        y = grid[i]
        if  y[0] == turn and  y[1] == turn and y[2] == turn:
            return True
    if grid[0][0] == turn and grid[1][1] == turn and grid[2][2]  == turn:
        return True
    elif grid[0][2] == turn and grid[1][1] == turn and grid[2][0]  == turn:
        return True
    return False

    
def occurances(grid): #Takes in a grid and returns the number of empty squares
    count = 0
    for sublist in grid:
        for element in sublist:
            if element == "-":
                count += 1
    return count  

# print(occurances(grid1))

print("starts here")

def minimax(grid, depth, Maximizing):
    # Check if the game is over (terminal state)
    if logic(grid, "X"):
        return -10 + depth, None
    if logic(grid, "O"):
        return 10 - depth, None
    if occurances(grid) == 0:
        return 0, None

    # If we're maximizing, we want to find the move with the highest score
    if Maximizing:
        bestScore = -float('inf')
        bestMove = None
        for i in range(3):
            for j in range(3):
                if grid[i][j] == "-":
                    newGrid = takeInput(grid, i, j, "O")
                    print(newGrid)
                    score, move = minimax(newGrid, depth+1, False)
                    # print(i, j, score, move)
                    if score > bestScore:
                        bestScore = score
                        bestMove = [i, j]
        return bestScore, bestMove

    # If we're minimizing, we want to find the move with the lowest score, i.e. the opposite
    else:
        bestScore = float('inf')
        bestMove = None
        for i in range(3):
            for j in range(3):
                if grid[i][j] == "-":
                    newGrid = takeInput(grid, i, j, "X")
                    # print(newGrid)
                    score, move = minimax(newGrid, depth+1, True)
                    # print(i, j, score, move)
                    if score < bestScore:
                        bestScore = score
                        bestMove = move
        return bestScore, bestMove

    

def main(grid):
    status = True
    while status:
        turn = whoseTurn(grid)
        print(f"It's {turn}'s turn now")
        if turn == "X":
            x = int(input("X: "))
            y = int(input("Y: "))
            grid = takeInput(grid, x, y, turn)
        else:
            print("Computer is thinking...")
            score, move = minimax(grid, 0, True)
            print(f"Computer chooses ({move[0]}, {move[1]}) with {score}")
            grid = takeInput(grid, move[0], move[1], turn)
        for i in range(len(grid)):
            print(grid[i])
        if logic(grid, turn): 
            print(f"{turn} wins!")
            break
        elif occurances(grid) == 0:
            print("It's a draw!")
            break


main(grid1) #initializing the main function