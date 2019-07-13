from random import randint

board = []
for i in range(5):
    board.append('0' * 5)
#makes a list with 5 o's for the map

def show_board(x):
    for i in range(5):
        print(x)
#to see the board or the seamap

r_row = randint(0,len(board)-1)
r_column = randint(0,len(board)-1)

x_ship = r_row
y_ship = r_column

#Main code exceution
show_board(board)
print(x_ship)
print(y_ship)
guess_row = int(input('Enter the row number : '))
guess_column = int(input('Enter the column number : '))
if guess_column > 4 or guess_row > 4:
    print('Enter a valid position because the position that you gave is outside the map')
else:
    no_of_guesses = 0
    if guess_row == x_ship and guess_column == y_ship:
        print('Daaaaamn... You won!!!')
        print('The number of guess that you made are : {}'.format(no_of_guesses+1))
    else:
        board[guess_row][guess_column] = "X"
        print('Awww... Nice try :( \nYou can try again!! \nHere is the map' )
        show_board(board)
