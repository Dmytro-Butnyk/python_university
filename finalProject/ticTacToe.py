import random

def draw(board):
    print("+-------"*3, "|", sep='')
    for row in range(3):
        print("|       "*3, "|", sep='')
        for col in range(3):
            print("|   "+str(board[row][col]) + "   ", end='')
        print("|")
        print("|       "*3, "|", sep='')
        print("+-------"*3, "|", sep='')

def check_free(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['0', 'X']:
                free.append((row, col))
    return free

def move(board):
    while True:
        move_input = int(input("Your move: ")) - 1
        row = move_input // 3
        col = move_input % 3
        if board[row][col] not in ['0', 'X']:
            board[row][col] = '0'
            break
        else:
            print("This cell is already occupied. Try again.")

def comp_move(board):
    free_cells = check_free(board)
    move_input = random.randrange(len(free_cells))
    row, col = free_cells[move_input]
    board[row][col] = 'X'

def win(board, sign):
    if sign == 'X':
        player = "X"
    elif sign == "0":
        player = "0"
    else:
        player = None
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return player
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return player
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return player
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return player
    return None


board = [[j * 3 + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = "X"
draw(board)

free = check_free(board)
human_turn = True

while len(free) > 0:
    if human_turn:
        move(board)
        vict = win(board, "0")
    else:
        print("Computer's turn")
        comp_move(board)
        vict = win(board, "X")
    if vict is not None:
        break

    draw(board)

    human_turn = not human_turn
    free = check_free(board)



if vict == "0":
    print("You win!")
elif vict == "X":
    print("Computer wins")
else:
    print("Draw")
