# from IPython.display import clear_output
import random
# def clear_output():
#     print("\n"*100)
def display_board(board):
    print('   |   |')
    print(' ' +board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[4]+' | '+ board[5]+' | '+ board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[1]+' | '+ board[2]+' | '+ board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



def place_marker(board,marker,position):
    board[position]=marker

# place_marker(test_board,'$',1)
# display_board(test_board)

def win_check(board,mark):
    return ((board[7]== mark and board[8]==mark and board[9]==mark)or
            (board[4]== mark and board[5]==mark and board[6]==mark)or
            (board[1]== mark and board[2]==mark and board[3]==mark)or
            (board[8]== mark and board[5]==mark and board[2]==mark)or
            (board[9]== mark and board[6]==mark and board[3]==mark)or
            (board[7]== mark and board[5]==mark and board[3]==mark)or
            (board[9]== mark and board[5]==mark and board[1]==mark))

# print(win_check(test_board,'X'))

def choose_first():
    flip=random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):
    position =0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose position:(1-9)"))

    return position

def replay():
    choice=input("Play again ? Enter 'YES' or 'NO':").upper()
    return choice=='YES'

print("Welcome to tic-tac-toe.")

while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()

    turn=choose_first()
    print(turn +" will go first")

    play_game=input("ready to play? y or n?").lower()

    if play_game=='y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn =='Player 1':
            display_board(the_board)

            position =player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 in won.")
                game_on=False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on=False
                else:
                    turn ='Player 2'

        else:
            display_board(the_board)

            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 in won.")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break





