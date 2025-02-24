# def user_choice():
#     acceptable_range =range(0,10)
#     within_range=False
#     number="one"
#     while number.isdigit() == False or within_range==False:
#         number=input("enter number(0,10):")
#
#         if number.isdigit() == False:
#             print("that iss not digit.")
#
#         if number.isdigit() == True:
#             if int(number) in acceptable_range:
#                 within_range = True
#             else:
#                 print("out of range")
#                 within_range =False
#     return int(number)
#
# user_choice()


from IPython.display import clear_output

def display_board(board):
    clear_output()
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
display_board(test_board)


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player_input()