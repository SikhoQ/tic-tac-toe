from random import randint

won = False
winner = ''
board = []


def still_space():
    for row in board:
        if '_' in row:
            return True
    return False


def turn_result():
    global won, winner
    b = board
    if b[0][0] != '_' and (b[0][0] == b[0][1] == b[0][2]
                           or b[0][0] == b[1][0] == b[2][0]):
        won = True
        winner = b[0][0]
    elif b[1][1] != '_' and (b[0][1] == b[1][1] == b[2][1]
                             or b[1][0] == b[1][1] == b[1][2]
                             or b[0][0] == b[1][1] == b[2][2]
                             or b[0][2] == b[1][1] == b[2][0]):
        won = True
        winner = b[1][1]
    elif b[2][2] != '_' and (b[0][2] == b[1][2] == b[2][2]
                             or b[2][0] == b[2][1] == b[2][2]):
        won = True
        winner = b[2][2]


def display_board():
    for row in board:
        print(' '.join(row))


def user_play():
    global board
    cell = input("enter cell to play in [rc]: ")
    while not valid_cell(cell):
        cell = input("enter a valid cell to play in [rc]: ")
    board[int(cell[0])][int(cell[1])] = 'X'


def valid_cell(cell):
    if len(cell) != 2 or board[int(cell[0])][int(cell[1])] != '_':
        return False
    return True


def comp_play():
    global board
    b = board
    while True:
        # PC play for win
        if ((b[0][1] == b[0][2] == 'O') or (b[1][0] == b[2][0] == 'O') or (b[1][1] == b[2][2] == 'O')) and b[0][0] == '_':
            r, c = 0, 0
        elif (b[0][0] == b[0][2] == 'O') or (b[1][1] == b[2][1] == 'O') and b[0][1] == '_':
            r, c = 0, 1
        elif ((b[0][0] == b[0][1] == 'O') or (b[1][2] == b[2][2] == 'O') or (b[1][1] == b[2][0] == 'O')) and b[0][2] == '_':
            r, c = 0, 2
        elif ((b[0][0] == b[2][0] == 'O') or (b[1][1] == b[1][2] == 'O')) and b[1][0] == '_':
            r, c = 1, 0
        elif ((b[1][0] == b[1][2] == 'O') or (b[0][1] == b[2][1] == 'O') or (b[0][0] == b[2][2] == 'O') or (b[0][2] == b[2][0] == 'O')) and b[1][1] == '_':
            r, c = 1, 1
        elif ((b[1][0] == b[1][1] == 'O') or (b[0][2] == b[2][2] == 'O')) and b[1][2] == '_':
            r, c = 1, 2
        elif ((b[0][0] == b[1][0] == 'O') or (b[2][1] == b[2][2] == 'O') or (b[0][2] == b[1][1] == 'O')) and b[2][0] == '_':
            r, c = 2, 0
        elif ((b[2][0] == b[2][2] == 'O') or (b[0][1] == b[1][1] == 'O')) and b[2][1] == '_':
            r, c = 2, 1
        elif ((b[2][0] == b[2][1] == 'O') or (b[0][2] == b[1][2] == 'C') or (b[0][0] == b[1][1] == 'O')) and b[2][2] == '_':
            r, c = 2, 2
        # PC defense
        elif ((b[0][1] == b[0][2] == 'X') or (b[1][0] == b[2][0] == 'X') or (b[1][1] == b[2][2] == 'X')) and b[0][0] == '_':
            r, c = 0, 0
        elif ((b[0][0] == b[0][2] == 'X') or (b[1][1] == b[2][1] == 'X')) and b[0][1] == '_':
            r, c = 0, 1
        elif ((b[0][0] == b[0][1] == 'X') or (b[1][2] == b[2][2] == 'X') or (b[1][1] == b[2][0] == 'X')) and b[0][2] == '_':
            r, c = 0, 2
        elif ((b[0][0] == b[2][0] == 'X') or (b[1][1] == b[1][2] == 'X')) and b[1][0] == '_':
            r, c = 1, 0
        elif ((b[1][0] == b[1][2] == 'X') or (b[0][1] == b[2][1] == 'X') or (b[0][0] == b[2][2] == 'X') or (b[0][2] == b[2][0] == 'X')) and b[1][1] == '_':
            r, c = 1, 1
        elif ((b[1][0] == b[1][1] == 'X') or (b[0][2] == b[2][2] == 'X')) and b[1][2] == '_':
            r, c = 1, 2
        elif ((b[0][0] == b[1][0] == 'X') or (b[2][1] == b[2][2] == 'X') or (b[0][2] == b[1][1] == 'X')) and b[2][0] == '_':
            r, c = 2, 0
        elif ((b[2][0] == b[2][2] == 'X') or (b[0][1] == b[1][1] == 'X')) and b[2][1] == '_':
            r, c = 2, 1
        elif ((b[2][0] == b[2][1] == 'X') or (b[0][2] == b[1][2] == 'X') or (b[0][0] == b[1][1] == 'X')) and b[2][2] == '_':
            r, c = 2, 2
        # PC offense (random play for now :/)
        else:
            r, c = randint(0, 2), randint(0, 2)
            while b[r][c] != '_':
                r, c = randint(0, 2), randint(0, 2)
        break
    b[r][c] = 'O'


def check_for_win():
    if won:
        if winner == 'X':
            print('User wins!\n>>> CONGRATULATIONS!! <<<')
        else:
            print("Computer wins.\n>> SORRY :( <<")


def play_game():
    global board, won
    board = [['_']*3 for n in range(3)]
    display_board()
    while not won and still_space():
        user_play()
        display_board()
        input(">>>>>>>>>>>> Press Enter <<<<<<<<<<<<")
        turn_result()
        if not won and still_space():
            comp_play()
            display_board()
        turn_result()
        check_for_win()
        if not still_space() and not won:
            print("It's A Tie!")


if __name__ == "__main__":
    play_game()
