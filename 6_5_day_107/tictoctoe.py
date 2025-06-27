grid = []
line = []

for i in range(3):
    for j in range(3):
        line.append(" ")
    grid.append(line)
    line = []


def print_grid():
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(grid[i][j], '|', end='')
        print('')


print(grid)
print(line)


def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False
        print(f"It's {player2}'s turn!")
    else:
        turn_player1 = True
        print(f"It's {player1}'s turn!")
    return turn_player1


def write_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j = cell % 3
    if turn_player1 == True:
        grid[i][j] = symbol1
    else:
        grid[i][j] = symbol2
    return grid


def free_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j = cell % 3
    if grid[i][j] == symbol1 or grid[i][j] == symbol2:
        print(" that cell is already filled. ")
        return False
    return True


def win_check(grid, symbol1, symbol2):
    full_grid = True
    player1_symbol_count = 0
    player2_symbol_count = 0
    # rows
    for i in range(3):
        for j in range(3):
            if grid[i][j] == symbol1:
                player1_symbol_count += 1
                player2_symbol_count = 0
                if player1_symbol_count == 3:
                    game = False
                    winner = player1
                    return game, winner
            if grid[i][j] == symbol2:
                player2_symbol_count += 1
                player1_symbol_count = 0
                if player2_symbol_count == 3:
                    game = False
                    winner = player2
                    return game, winner
            if grid[i][j] == ' ':
                full_grid = False
        player1_symbol_count = 0
        player2_symbol_count = 0
    # columns
    player1_symbol_count = 0
    player2_symbol_count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i + k <= 2:
                    if grid[i + k][j] == symbol1:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j] == symbol2:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
                    if grid[i + k][j] == ' ':
                        full_grid = False
            player1_symbol_count = 0
            player2_symbol_count = 0
    # diagonals
    player1_symbol_count = 0
    player2_symbol_count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i + k <= 2 and j + k <= 2:
                    if grid[i + k][j + k] == symbol1:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j + k] == symbol2:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
                    if grid[i + k][j + k] == ' ':
                        full_grid = False
            player1_symbol_count = 0
            player2_symbol_count = 0

    player1_symbol_count = 0
    player2_symbol_count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i + k <= 2 and j - k >= 0:
                    if grid[i + k][j - k] == symbol1:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j - k] == symbol2:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
                    if grid[i + k][j - k] == ' ':
                        full_grid = False
            player1_symbol_count = 0
            player2_symbol_count = 0

    if full_grid == True:
        game = False
        winner = ""
        return game, winner
    else:
        game = True
        winner = ""
        return game, winner


print("welcome to Tic Tac Toe!!")
print_grid()
player1 = input("enter the player1 name:")
symbol1 = input("enter symbol (O/X):").upper()
player2 = input('enter the player2 name:')
symbol = ['X', 'O']
if symbol1 == symbol[0]:
    symbol2 = symbol[1]
else:
    symbol2 = symbol[0]
print(f'player 2 symbol :{symbol2}')
game = True
full_grid = False
turn_player1 = False
winner = ''

while game:
    turn_player1 = player_turn(turn_player1)
    free_box = False
    while free_box == False:
        cell = int(input('please enter number from 1 to 9:'))
        free_box = free_cell(cell)
    grid = write_cell(cell)
    print(grid)
    print_grid()
    game, winner = win_check(grid, symbol1, symbol2)

if winner == player1:
    print(f'Winner is {player1}!!')
elif winner == player2:
    print(f'Winner is {player2}!!')
else:
    print('grid is full!!')
