# /g/ Challenge - 1-2 Player Tic-Tac-Toe
# Paul Sypnowich
# February 26 2015
# Version 0.1 for Python 3.2

from random import randint
print("TicTacToe v0.1 by Paul Sypnowich")

#board generation and display methods
def board_reset():
	board = []
	for none in range(3):		
		board.append(["+"] * 5)
	return board

def board_printer(board):
	print("\n    1   2   3  ")
	print("  +-----------+")
	for row in range(3):
		print(row+1,"|",board[row][0],"|",board[row][1],"|",board[row][2],"|")
		if ((row+1) % 3 != 0):
			print("  |---+---+---|")
		elif ((row+1) % 3 == 0):
			print("  +-----------+\n")

#guess randomiser
def random_guess_row():
	return randint(0,2)
def random_guess_col():
	return randint(0,2)

#unit kill detection 
#statuscode 1 = X ; 2 = O
#returncode 1 = death ; 2 = nodeath
def detect_board_death(board, statuscode):
	if (statuscode == 1):
		unit = "X"
	elif (statuscode == 2):
		unit = "O"
	returncode = 2

	for r in range(3):
		for c in range(3):
			#horizontal collision test
			if ((board[0][c] == unit) and (board[1][c] == unit)):
				if (board[2][c] == unit):
					returncode = 1
			#vertical collision test
			if ((board[r][0] == unit) and (board[r][1] == unit)):
				if (board[r][2] ==unit):
					returncode = 1
			#diagonal collision test
			if ((board[0][0] == unit) and (board[1][1] == unit)):
				if (board[2][2] == unit):
					returncode = 1
			elif ((board[0][2] == unit) and (board[1][1] == unit)):
				if (board[2][0] == unit):
					returncode = 1
	return returncode

#board fill detection
#statuscode 1 = death; 2 = nodeath
def detect_board_fill(board):
	statuscode = 2
	plus_counter = 0
	plus_sign = "+"
	for r in range(3):
		for c in range(3):
			if (board[r][c] == plus_sign):
				plus_counter = plus_counter+1
	if (plus_counter == 0):
		statuscode = 1
	return statuscode

#1 player game mode
def single_player():
	print("Welcome to 1p tic-tac-toe.")
	whois_p = input("What is your name?: ")
	print("Hello, ", str(whois_p) + "!\n")

	board = []
	board = board_reset()	
	game_flag = 1
	while (game_flag != 0):
		#player turn 
		print("It's your turn.")
		print("Here is the board. You are X, computer is O.")
		board_printer(board)
		
		guessFlag = 1
		while (guessFlag != 0):
			player_guess_row = int(input("Enter row: ")) - 1
			player_guess_col = int(input("Enter col: ")) - 1
			if (board[player_guess_row][player_guess_col] == "+"):
				guessFlag = 0
			else:
				print("ERROR: Invalid location! Pick an empty location, marked with a +. Trying again...")

		board[player_guess_row][player_guess_col] = "X"
		p_deathstatus = detect_board_death(board, 1)
		if (p_deathstatus == 1):
			print("GAME OVER -- YOU WIN!")
			print("Here is the winning board.")
			board_printer(board)
			game_flag = 0
			break
		b_fillstatus = detect_board_fill(board)
		if (b_fillstatus == 1):
			print("GAME OVER -- DRAW! The board is full. \nHere is the full board.")
			board_printer(board)
			game_flag = 0
			break

		#computer turn
		print("\nIt's the computer's turn.")		
		computerFlag = 1
		while (computerFlag != 0):
			computer_guess_row = random_guess_row()
			computer_guess_col = random_guess_col()
			if (board[computer_guess_row][computer_guess_col] == "+"):
				computerFlag = 0
		print("The computer has taken it's turn.")

		board[computer_guess_row][computer_guess_col] = "O"
		c_deathstatus = detect_board_death(board, 2)
		if (c_deathstatus == 1):
			print("GAME OVER -- COMPUTER WINS\nHere is the winning board.")
			board_printer(board)
			game_flag = 0
			break
		b_fillstatus = detect_board_fill(board)
		if (b_fillstatus == 1):
			print("GAME OVER -- DRAW! The board is full. \nHere is the full board.")
			board_printer(board)
			game_flag = 0
			break

def two_player():
	print("\nWelcome to 2p tic-tac-toe.")
	whois_p1 = input("\nWhat is p1's name?: ")
	whois_p2 = input("What is p2's name?: ")
	print("\nHello " + whois_p1 + ", hello " + whois_p2 + "!")

	board = []
	board = board_reset()
	game_flag = 1
	while (game_flag != 0):
		#player 1's turn
		print("\nIt's " + whois_p1 + "'s turn.")
		print("Here is the board. You are X, " + whois_p2 + " is O.")
		board_printer(board)

		guessFlag = 1
		while (guessFlag != 0):
			player1_guess_row = int(input("Enter row: ")) -1
			player1_guess_col = int(input("Enter col: ")) -1
			if (board[player1_guess_row][player1_guess_col] == "+"):
				guessFlag=0
			else:
				print("ERROR: Invalid location! Pick an empty location, marked with a +. Trying again...")

		board[player1_guess_row][player1_guess_col] = "X"
		p1_deathstatus = detect_board_death(board, 1)
		if (p1_deathstatus == 1):
			print("GAME OVER -- ",whois_p1," WINS!\nHere is the winning board.")
			board_printer(board)
			game_flag = 0
			break
		b_fillstatus = detect_board_fill(board)
		if (b_fillstatus == 1):
			print("GAME OVER -- DRAW! The board is full. \nHere is the full board.")
			board_printer(board)
			game_flag = 0
			break

		#player 2's turn
		print("\nIt's " + whois_p2 + "'s turn.")
		print("Here is the board. You are O, " + whois_p1 + " is X.")
		board_printer(board)

		guessFlag = 1
		while (guessFlag != 0):
			player2_guess_row = int(input("Enter row: ")) -1
			player2_guess_col = int(input("Enter col: ")) -1
			if (board[player2_guess_row][player2_guess_col] == "+"):
				guessFlag=0
			else:
				print("ERROR: Invalid location! Pick an empty location, marked with a +. Trying again...")

		board[player2_guess_row][player2_guess_col] = "O"
		p2_deathstatus = detect_board_death(board, 2)
		if (p2_deathstatus == 1):
			print("GAME OVER -- ",whois_p2," WINS!\nHere is the winning board.")
			board_printer(board)
			game_flag = 0
			break
		b_fillstatus = detect_board_fill(board)
		if (b_fillstatus == 1):
			print("GAME OVER -- DRAW! The board is full. \nHere is the full board.")
			board_printer(board)
			game_flag = 0
			break

### END ###

#game mode chooser
flagVar1 = 0;
while (flagVar1 != 1):
	gameMode = int(input("\nWelcome to Tic-Tac-Toe! Do you want to play 1p or 2p? (1/2):"))
	if (gameMode == 1):
		print(single_player)
		single_player()
		flagVar = 1
	elif (gameMode == 2):
		two_player()
		flagVar = 1
	else:
		print("ERROR: Invalid input entered! Enter either 1 or 2.")
		print("Running again...")

