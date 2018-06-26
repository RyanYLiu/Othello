#Ryan Liu ID: 73638662

import Othello_logic


def runUserInterface() -> None:
	'''
	Runs user interface
	'''
	print('FULL')
	rows = int(input())
	columns = int(input())
	startingPlayer = input()
	startingOrientation = input()
	wayToWin = input()
	othello = Othello_logic.GameState(rows, columns, 
		startingPlayer, startingOrientation, wayToWin)
	othello.createBoard()
	while True:
		playerTiles = othello.checkNumTiles()
		print('B: {}  W: {}'.format(othello.blackPieces, othello.whitePieces))
		othello.printBoard()
		if othello.turn == 1:
			turn = 'B'
			print('TURN: {}'.format(turn))
		else:
			turn = 'W'
			print('TURN: {}'.format(turn))
		playerMove(othello)
		if othello.isGameOver() == True:
			break
	determineWinner(othello)





def playerMove(othello: 'GameState') -> None:
	'''
	Allows the player to make a move and will check whether the move is legal
	'''
	while True:
		move = input()
		moveCoordinate = (int(move[0]), int(move[2]))
		if othello.addMoveToState(moveCoordinate[0], moveCoordinate[1]):
			print('VALID')
			othello.changeTurn()
			break
		else:
			print('INVALID')

def determineWinner(othello: 'GameState') -> None:
	'''
	Checks which player is the winner and prints out the winner
	'''
	if othello.winType == '>':
		playerTiles = othello.checkNumTiles()
		print('B: {}  W: {}'.format(othello.blackPieces, othello.whitePieces))
		othello.printBoard()
		if othello.winner == 1:
			print('WINNER: {}'.format('B'))
		elif othello.winner == 2:
			print('WINNER: {}'.format('W'))
		else:
			print('WINNER: {}'.format('NONE'))






if __name__ == '__main__':
	runUserInterface()
