#Ryan Liu ID: 73638562


NONE = 0
BLACK = 1
WHITE = 2
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


class InputError(Exception):
	pass



class GameState:
	def __init__(self, rows: int, columns: int, startingPlayer: str, orientation: str, normalWin: str) -> None:
		'''
		Initializes the class object and stores player's inputs into variables
		'''
		self.rows = rows
		self.columns = columns
		if startingPlayer == 'B':
			self.turn = BLACK
		else:
			self.turn = WHITE
		self.orientation = orientation
		self.winType = normalWin
		self.winner = NONE
	
	def createBoard(self) -> None:
		'''
		Creates a new game board
		'''
		self.board = []

		if self.rows%2 == 0 and self.rows >= 4 and self.rows <= 16:
			for num in range(self.rows):
				self.board.append([])
				
		for boardRow in self.board:
			if self.columns%2 == 0 and self.columns >= 4 and self.columns <= 16:
				for num in range(self.columns):
					boardRow.append(0)

		if self.orientation == 'B':
			self.board[(self.rows//2)][self.columns//2] = BLACK
			self.board[(self.rows//2) - 1][(self.columns//2) - 1] = BLACK

			self.board[(self.rows//2)][(self.columns//2) - 1] = WHITE
			self.board[(self.rows//2) - 1][(self.columns//2)] = WHITE
		if self.orientation == 'W':
			self.board[(self.rows//2)][self.columns//2] = WHITE
			self.board[(self.rows//2) - 1][(self.columns//2) - 1] = WHITE

			self.board[(self.rows//2)][(self.columns//2) - 1] = BLACK
			self.board[(self.rows//2) - 1][(self.columns//2)] = BLACK


			
			
	def isMoveValid(self, row: int, column: int) -> bool:
		'''
		Checks if the player's move is on the board
		'''

		if row-1 in range(self.rows):
			if column-1 in range(self.columns):
				if self.board[row-1][column-1] == NONE:
					return True

		


	def possibleDirectionsToFlip(self, row: int, column: int) -> list:
		'''
		Returns a list of directions for the directions that tiles will be flipped if a piece
		is placed in that cell
		'''
		possibleDirections = []

		for i in DIRECTIONS:
			if self.checkDirection(row, column, i) == True:
				possibleDirections.append(i)
		return possibleDirections



	def flipPieces(self, row: int, column: int) -> None:
		'''
		Flips pieces in legal directions
		'''
		otherPlayer = self.getOtherPlayer()
		possibleCoordinates = self.possibleDirectionsToFlip(row, column)
		for coordinate in possibleCoordinates:
			nextRow = row-1 + coordinate[1]
			nextColumn = column-1 + coordinate[0]
			adjacentCell = self.board[nextRow][nextColumn]
			if adjacentCell == otherPlayer:
				while adjacentCell == otherPlayer:
					self.board[nextRow][nextColumn] = self.turn
					nextRow += coordinate[1]
					nextColumn += coordinate[0]
					adjacentCell = self.board[nextRow][nextColumn]
##					if adjacentCell == self.turn:
##						break




	def checkDirection(self, row: int, column: int, direction: tuple) -> bool:
		'''
		Checks if a direction is a legal move
		'''
		otherPlayer = self.getOtherPlayer()
		
		nextRow = row-1 + direction[1]
		nextColumn = column-1 + direction[0]
		if nextRow in range(self.rows) and nextColumn in range(self.columns):
			adjacentCell = self.board[nextRow][nextColumn]
			if adjacentCell == otherPlayer:
				while adjacentCell == otherPlayer:
					nextRow += direction[1]
					nextColumn += direction[0]
					if nextRow in range(self.rows) and nextColumn in range(self.columns):
						adjacentCell = self.board[nextRow][nextColumn]
						if adjacentCell == self.turn:
							return True
					else:
						return False


			
			
	def getOtherPlayer(self) -> int:
		'''
		Returns the other player
		'''
		if self.turn == BLACK:
			otherPlayer = WHITE
		else:
			otherPlayer = BLACK
		return otherPlayer


		

	def addMoveToState(self, row: int, column: int) -> bool:
		'''
		Adds player's move into the game state
		'''
		if self.isMoveValid(row, column):
			if self.possibleDirectionsToFlip(row, column) != []:
				self.board[row-1][column-1] = self.turn
				self.flipPieces(row, column)
				return True



	def anyPossibleMoves(self) -> list:
		'''
		Check for all possible coordinates that a player can input
		'''
		allMoves = []
		for row in range(len(self.board)):
			for column in range(len(self.board[row])):
				valid = self.isMoveValid(row+1, column+1)
				if valid == True:
					coordinates = self.possibleDirectionsToFlip(row+1, column+1)
					if coordinates != []:
						allMoves.append((row+1,column+1))
		return allMoves
						


	def isGameOver(self) -> bool:
		'''
		Checks if the game is over
		'''
		if self.isBoardFull() != False:
			return True
		elif self.anyPossibleMoves() == []:
			self.changeTurn()
			if self.anyPossibleMoves() == []:
				return True




	def isBoardFull(self) -> bool:
		'''
		Check if the board is full
		'''
		for row in range(self.rows):
			for column in range(self.columns):
				if self.board[row][column] == NONE:
					return False




	def changeTurn(self) -> None:
		'''
		Changes the turn between players
		'''
		if self.turn == BLACK:
			self.turn = WHITE
		else:
			self.turn = BLACK




	def checkNumTiles(self) -> None:
		'''
		Checks the number of tiles each player has on the board
		'''
		self.blackPieces = 0
		self.whitePieces = 0
		for row in self.board:
			for cell in row:
				if cell != 0:
					if cell == 1:
						self.blackPieces += 1
					if cell == 2:
						self.whitePieces += 1



	def checkWinnerMost(self) -> int:
		'''
		Checks the winner of the game mode where player with most pieces wins
		'''
		if self.blackPieces > self.whitePieces:
			winner = BLACK
		elif self.blackPieces < self.whitePieces:
			self.winner = WHITE
		else:
			self.winner = NONE
		return self.winner



	def checkWinnerLeast(self) -> int:
		'''
		Checks the winner of the game mode where player with least pieces wins
		'''
		if self.blackPieces < self.whitePieces:
			self.winner = BLACK
		elif self.blackPieces > self.whitePieces:
			self.winner = WHITE
		else:
			self.winner = NONE
		return self.winner


	def printBoard(self) -> None:
		'''
		Prints the board
		'''
		for row in range(self.rows):
			eachRow = ''
			for column in range(self.columns):
				if self.board[row][column] == NONE:
					eachRow += '. '
				elif self.board[row][column] == BLACK:
					eachRow += 'B '
				elif self.board[row][column] == WHITE:
					eachRow += 'W '
			print(eachRow)		
