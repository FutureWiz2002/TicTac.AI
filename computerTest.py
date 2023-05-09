from tictac import *

grid2 = [
    ["-", "-", "-"], 
    ["-", "-", "-"],
    ["-", "-", "-"] ]

def computer(grid):
    status = True
    while status:
        turn = whoseTurn(grid)
        print(f"It's {turn}'s turn now")
        if turn == "X":
            print("Computer is thinking...")
            score, move = minimax(grid, 0, True)
            # print(f"Computer chooses ({move[0]}, {move[1]}) with {score}")
            grid = takeInput(grid, move[0], move[1], turn)
        else:
            print("Computer is thinking...")
            score, move = minimax(grid, 0, True)
            # print(f"Computer chooses ({move[0]}, {move[1]}) with {score}")
            grid = takeInput(grid, move[0], move[1], turn)
        for i in range(len(grid)):
            print(grid[i])
        if logic(grid, turn): 
            print(f"{turn} wins!")
            break
        elif occurances(grid) == 0:
            print("It's a draw!")
            break

# computer(grid2) # To initialize computer vs computer
# Since Tic Tac Toe is a simple game, the output board is always the 
def fromHere(grid):
    status = True 
    turn = whoseTurn(grid)
    # x = int(input("X: "))
    # y = int(input("Y: "))
    # grid = takeInput(grid, x, y, turn)
    while status:
        turn = whoseTurn(grid)
        if turn == "X":
            print("Computer is thinking...")
            score, move = minimax(grid, 0, True)
            print(f"Computer chooses ({move[0]}, {move[1]}) with {score}")
            grid = takeInput(grid, move[0], move[1], turn)
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
exampleGrid = [
    ["O", "-", "-"], 
    ["-", "X", "-"],
    ["O", "-", "X"] ]

fromHere(exampleGrid)