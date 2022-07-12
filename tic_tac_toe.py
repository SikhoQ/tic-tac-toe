from sys import argv
from random import randint

win = False
winner = ''
board = []

def still_space():
    for row in board:
        if '_' in row:
            return True
    return False

def check_user_near_win():
    b = board
    if (b[0][0] == '_' and b[0][1] == b[0][2] == b[1][0] == b[2][0] == 'X') or\
        (b[1][0] == '_' and b[1][1] == b[1][2] == b[0][0] == b[2][0] == 'X') or\
         (b[2][0] == '_' and b[2][1] == b[2][2] == b[0][0] == b[1][0] == 'X') or\
          (b[0][1] == '_' and b[0][0] == b[0][2] == b[1][1] == b[2][1] == 'X') or\
           (b[1][1] == '_' and b[1][0] == b[1][2] == b[0][1] == b[2][1] == b[0][0]\
            == b[2][2] == b[0][2] == b[2][0] == 'X') or\
            (b[2][1] == '_' and b[2][0] == b[2][2] == b[0][1] == b[1][1] == 'X') or\
             (b[0][2] == '_' and b[0][0] == b[0][1] == b[1][2] == b[2][2] == 'X') or\
              (b[1][2] == '_' and b[1][0] == b[1][1] == b[0][2] == b[2][2] == 'X') or\
               (b[2][2] == '_' and b[2][0] == b[2][1] == b[0][2] == b[1][2] == 'X'):
                    return True    
    return False

def turn_result():
    global win, winner
    b = board
    if b[1][1] != '_' and (b[0][1] == b[1][1] == b[2][1]
                            or b[1][0] == b[1][1] == b[1][2]
                            or b[0][0] == b[1][1] == b[2][2]
                            or b[0][2] == b[1][1] == b[2][0]):
        win = True
        winner = b[1][1]
    elif b[0][0] != '_' and (b[0][0] == b[0][1] == b[0][2]
                            or b[0][0] == b[1][0] == b[2][0]):
        win = True
        winner = b[0][0]
    elif b[2][2] != '_' and (b[0][2] == b[1][2] == b[2][2]
                            or b[2][0] == b[2][1] == b[2][2]):
        win = True
        winner = b[2][2]

def display_board():
    for row in board:
        print(' '.join(row))

def user_play():
    global board
    cell = input("enter cell to play in: ")
    while len(cell) != 2:
        cell = input("enter cell to play in: ")
    r = int(cell[0])
    c = int(cell[1])
    while board[r][c] != '_':
        cell = input("enter another cell to play in: ")
        r = int(cell[0])
        c = int(cell[1])
    board[r][c] = 'X'

def comp_play():
    global board
    r = randint(0,2)
    c = randint(0,2)
    while board[r][c] != '_':
        r = randint(0,2)
        c = randint(0,2)
    board[r][c] = 'O'

def check_win():
    if win:
        if winner == 'X':
            print('User wins!\n>>> CONGRATULATIONS!! <<<')
        elif winner == 'O':
            print("Computer wins.\n>> SORRY :( <<")

def play_game():
    global board, win
    board = [['_']*3 for n in range(3)]
    display_board()
    while not win and still_space():
        user_play()
        display_board()
        input(">>>>>>>>>>>> Press Enter <<<<<<<<<<<<")
        turn_result()
        if not win and still_space():
            comp_play()
            display_board()
        turn_result()
        check_win()
        if win:
            return
        elif not still_space():
            print("It's A Tie!")

if __name__ == "__main__":
    play_game()
