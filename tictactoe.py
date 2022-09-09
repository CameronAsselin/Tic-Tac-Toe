# Intialize board and set the win condition to False
board = {'a1':' ','a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ','c2':' ','c3':' '}
win = False

# Prints the board to the console
def write_board(board,move=None,player=None):
	if move != None:
		if player == 1:
			board[move] = 'X'
		else:
			board[move] = 'O'	
	print('  A B C')
	print(f"1 {board['a1']}|{board['b1']}|{board['c1']}")
	print('  -+-+-')
	print(f"2 {board['a2']}|{board['b2']}|{board['c2']}")
	print('  -+-+-')
	print(f"3 {board['a3']}|{board['b3']}|{board['c3']}")

# Checks if a move is on the grid and not already claimed
def check_valid(board,move,player):
	while move not in board:
		move = input('**That space is out of range, please try again: ')
	while board[move] != ' ':
		move = input('**That space is already taken, please try again: ')
		while move not in board:
			move = input('**That space is out of range, please try again: ')	
	board = write_board(board,move,player)
	return move

# Checks to see if either X or O has reached one of the 8 win conditions. If all spaces are full and no winner, calls a tie
def check_win(board):
	if board['a1'] == 'X' and board['a2'] == 'X' and board['a3'] == 'X':
		return True
	elif board['b1'] == 'X' and board['b2'] == 'X' and board['b3'] == 'X':
		return True
	elif board['c1'] == 'X' and board['c2'] == 'X' and board['c3'] == 'X':
		return True
	elif board['a1'] == 'X' and board['b1'] == 'X' and board['c1'] == 'X':
		return True
	elif board['a2'] == 'X' and board['b2'] == 'X' and board['c2'] == 'X':
		return True
	elif board['a3'] == 'X' and board['b3'] == 'X' and board['c3'] == 'X':
		return True
	elif board['a1'] == 'X' and board['b2'] == 'X' and board['c3'] == 'X':
		return True
	elif board['a3'] == 'X' and board['b2'] == 'X' and board['c1'] == 'X':
		return True
	elif board['a1'] == 'O' and board['a2'] == 'O' and board['a3'] == 'O':
		return True
	elif board['b1'] == 'O' and board['b2'] == 'O' and board['b3'] == 'O':
		return True
	elif board['c1'] == 'O' and board['c2'] == 'O' and board['c3'] == 'O':
		return True
	elif board['a1'] == 'O' and board['b1'] == 'O' and board['c1'] == 'O':
		return True
	elif board['a2'] == 'O' and board['b2'] == 'O' and board['c2'] == 'O':
		return True
	elif board['a3'] == 'O' and board['b3'] == 'O' and board['c3'] == 'O':
		return True
	elif board['a1'] == 'O' and board['b2'] == 'O' and board['c3'] == 'O':
		return True
	elif board['a3'] == 'O' and board['b2'] == 'O' and board['c1'] == 'O':
		return True
	else:	
		win = False
		if board['a1'] != ' ' and board['a2'] != ' ' and board['a3'] != ' ' and board['b1'] != ' ' and board['b2'] != ' ' and board['b3'] != ' ' and board['c1'] != ' ' and board['c2'] != ' ' and board['c3'] != ' ' and win == False:
			win = 'tie'
		return win

# Print the starting board to the console and play until someone wins
write_board(board)
while win == False: 
	p1 = input('**Player1 - Pick a spot: ')
	move = check_valid(board,p1,1)
	win = check_win(board)
	if win == True:
		print('**Player 1 wins!**')
		break
	elif win == 'tie':
		print('**TIE!**')
		break	
	p2 = input('**Player2 - Pick a spot: ')
	move = check_valid(board,p2,2)
	win = check_win(board)
	if win == True:
		print('**Player 2 wins!**')
