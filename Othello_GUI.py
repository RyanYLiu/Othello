#Ryan Liu ID: 73638562

import tkinter
import point
import Othello_logic


FONT = 'Helvetica'

class GameSpecDialog:
	def __init__(self):
		self._dialog_window = tkinter.Toplevel()

		game_specs = tkinter.Label(master = self._dialog_window)


		row_label = tkinter.Label(
			master = self._dialog_window, text = 'Number of rows:', font = (FONT, 10))
		row_label.grid(
			row = 0, column = 0, padx = 5, pady = 5, sticky = tkinter.W)


		self._row_entry = tkinter.Entry(
			master = self._dialog_window, width = 5, font = (FONT, 10))
		self._row_entry.grid(
			row = 0, column = 1, padx = 5, pady = 5, sticky = tkinter.W + tkinter.E)


		column_label = tkinter.Label(
			master = self._dialog_window, text = 'Number of columns:', font = (FONT, 10))
		column_label.grid(
			row = 1, column = 0, padx = 5, pady = 5, sticky = tkinter.W)

		self._column_entry = tkinter.Entry(
			master = self._dialog_window, width = 5, font = (FONT, 10))
		self._column_entry.grid(
			row = 1, column = 1, padx = 5, pady = 5, sticky = tkinter.W + tkinter.E)


		starting_player_label = tkinter.Label(
			master = self._dialog_window, text = 'Starting Player:', font = (FONT, 10))
		starting_player_label.grid(
			row = 2, column = 0, padx = 5, pady = 5, sticky = tkinter.W)


		starting_player_frame = tkinter.LabelFrame(
			master = self._dialog_window)
		starting_player_frame.grid(
			row = 2, column = 1, padx = 5, pady = 5, sticky = tkinter.E + tkinter.W)


		self._start_player_str = tkinter.StringVar()

		self._black_player_radio = tkinter.Radiobutton(
			master = starting_player_frame, text = 'Black', font = (FONT,10),
			variable = self._start_player_str, value = 'B')
		self._black_player_radio.grid(row = 0, column = 0)


		self._white_player_radio = tkinter.Radiobutton(
			master = starting_player_frame, text = 'White', font = (FONT, 10),
			variable = self._start_player_str, value = 'W')
		self._white_player_radio.grid(row = 0, column = 1, sticky = tkinter.E)

		self._black_player_radio.select()


		starting_position_label = tkinter.Label(
			master = self._dialog_window, text = 'Starting Position:', font = (FONT, 10))
		starting_position_label.grid(
			row = 3, column = 0, padx = 5, pady = 5, sticky = tkinter.W)

		starting_position_frame = tkinter.LabelFrame(
			master = self._dialog_window)
		starting_position_frame.grid(
			row = 3, column = 1, sticky = tkinter.E + tkinter.W, padx = 5, pady = 5)


		self._start_position_str = tkinter.StringVar()
		
		self._black_position_radio = tkinter.Radiobutton(
			master = starting_position_frame, text = 'Black', font = (FONT, 10),
			variable = self._start_position_str, value = 'B')
		self._black_position_radio.grid(row = 0, column = 0)
		

		self._white_position_radio = tkinter.Radiobutton(
			master = starting_position_frame, text = 'White', font = (FONT, 10),
			variable = self._start_position_str, value = 'W')
		self._white_position_radio.grid(row = 0, column = 1)

		self._black_position_radio.select()

		win_type_label = tkinter.Label(
			master = self._dialog_window, text = 'Way to win:', font = (FONT, 10))
		win_type_label.grid(
			row = 4, column = 0, padx = 5, pady = 5, sticky = tkinter.W)


		self._win_str = tkinter.StringVar()

		win_frame = tkinter.LabelFrame(
			master = self._dialog_window)
		win_frame.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = tkinter.W + tkinter.E)

		win_less_radio = tkinter.Radiobutton(
			master = win_frame, text = 'Least', font = (FONT, 10), variable = self._win_str,
			value = '<')
		win_less_radio.grid(row = 0, column = 0)
		
		win_more_radio = tkinter.Radiobutton(
			master = win_frame, text = 'Most', font = (FONT, 10), variable = self._win_str, value = '>')
		win_more_radio.grid(row = 0, column = 1)

		win_less_radio.select()

		button_frame = tkinter.Frame(
			master = self._dialog_window)
		button_frame.grid(row = 6, column = 1, sticky = tkinter.S + tkinter.E)

		ok_button = tkinter.Button(
			master = button_frame, text = 'OK', font = (FONT, 10), command = self._on_ok_clicked)
		ok_button.grid(row = 0, column = 0, padx = 5, pady = 5)

		cancel_button = tkinter.Button(
			master = button_frame, text = 'Cancel', font = (FONT, 10), command = self._on_cancel_clicked)
		cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5)

		self._dialog_window.rowconfigure(5, weight = 1)
		self._dialog_window.columnconfigure(1, weight = 1)


		self._rows = 0
		self._columns = 0
		self._starting_player = ''
		self._starting_position = ''
		self._win_type = ''
		self._ok_clicked = False

	def run(self):
		self._dialog_window.grab_set()
		self._dialog_window.wait_window()

	def _was_ok_clicked(self):
		return self._ok_clicked


	def _get_num_rows(self):
		return self._rows

	def _get_num_columns(self):
		return self._columns

	def _get_starting_player(self):
		return self._starting_player

	def _get_starting_position(self):
		return self._starting_position

	def _get_way_to_win(self):
		return self._win_type


	def _on_ok_clicked(self):
		self._ok_clicked = True

		self._rows = self._row_entry.get()
		self._columns = self._column_entry.get()
		self._starting_player = self._start_player_str.get()
		self._starting_position = self._start_position_str.get()
		self._win_type = self._win_str.get()

		self._dialog_window.destroy()


	def _on_cancel_clicked(self):
		self._dialog_window.destroy()



class Othello:
	def __init__(self):
		self._othello_state = None
		self._root_window = tkinter.Tk()

		self._black_pieces = tkinter.StringVar()
		self._black_pieces.set('Black: 0')

		self._white_pieces = tkinter.StringVar()
		self._white_pieces.set('White: 0')

		self._turn = tkinter.StringVar()
		self._turn.set('No game in progress')

		pieces_frame = tkinter.Frame(
			master = self._root_window)
		pieces_frame.grid(
			row = 0, column = 0, sticky = tkinter.N + tkinter.E + tkinter.W + tkinter.S)
		

		

		self.black_label = tkinter.Label(
			master = pieces_frame, textvariable = self._black_pieces, font = (FONT, 20))
		self.black_label.grid(
			row = 0, column = 0, sticky = tkinter.W, padx = 10)



		self.white_label = tkinter.Label(
			master = pieces_frame, textvariable = self._white_pieces, font = (FONT, 20))
		self.white_label.grid(
			row = 0, column = 1, sticky = tkinter.E, padx = 10)




		self._canvas = tkinter.Canvas(
			master = self._root_window, background = 'green', width = 500, height = 500)
		self._canvas.grid(
			row = 1, column = 0, padx = 5, pady = 10, sticky = tkinter.N + tkinter.E + tkinter.W + tkinter.S)
		self._canvas.bind('<Configure>', self._on_canvas_resize)

		

		bottom_frame = tkinter.Frame(
			master = self._root_window)
		bottom_frame.grid(row = 2, column = 0, sticky = tkinter.N + tkinter.E + tkinter.W + tkinter.S)

		button_text = tkinter.StringVar()
		button_text.set('Start New Game')

		start_button = tkinter.Button(
			master = bottom_frame, textvariable = button_text, command = self._on_start_press)

		start_button.grid(row = 0, column = 0, sticky = tkinter.W, padx = 10, pady = 10)

		full_label = tkinter.Label(
			master = bottom_frame, text = 'FULL', font = (FONT, 20))
		full_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.E)


		self._turn_label = tkinter.Label(
			master = self._root_window, textvariable = self._turn, font = (FONT, 20))
		self._turn_label.grid(row = 1, column = 1, padx = 10)

		
		self._root_window.columnconfigure(0, weight = 1)
		self._root_window.rowconfigure(1, weight = 1)
		pieces_frame.columnconfigure(0, weight = 1)
		pieces_frame.columnconfigure(1, weight = 1)
		bottom_frame.columnconfigure(0, weight = 1)
		bottom_frame.columnconfigure(1, weight = 1)

		self._canvas.bind('<Button-1>', self._add_move_circle)




	def start(self):
		self._root_window.mainloop()

	def _on_start_press(self) -> None:
		dialog = GameSpecDialog()
		dialog.run()
		if dialog._was_ok_clicked() == True:
			self._canvas.delete(tkinter.ALL)
			rows = int(dialog._get_num_rows())
			columns = int(dialog._get_num_columns())
			starting_player = dialog._get_starting_player()
			starting_orientation = dialog._get_starting_position()
			win_type = dialog._get_way_to_win()

			self._othello_state = Othello_logic.GameState(
				rows, columns, starting_player, starting_orientation, win_type)
			self._othello_state.createBoard()
			self._draw_board()
			self._show_turn()
			self._show_pieces()
			self._draw_circles()
			
		

	def _on_canvas_resize(self, event: tkinter.Event):
		if self._othello_state != None:
			self._canvas.delete(tkinter.ALL)
			self._draw_board()
			self._draw_circles()

	def _draw_board(self):

		self.canvas_width = self._canvas.winfo_width()
		self.canvas_height = self._canvas.winfo_height()
		self.column_spacing = self.canvas_width/self._othello_state.columns
		self.row_spacing = self.canvas_height/self._othello_state.rows
		self.point_row_spacing = point.from_pixel(
			0, self.row_spacing, self.canvas_width, self.canvas_height)
		self.point_col_spacing = point.from_pixel(
			self.column_spacing, 0, self.canvas_width, self.canvas_height)
		each_row = 0
		each_col = 0
		for row in range(1, self._othello_state.rows):
			each_row += self.point_row_spacing._frac_y
			self._canvas.create_line(
				0, each_row * self.canvas_height, self.canvas_width, each_row * self.canvas_height)

		for column in range(1, self._othello_state.columns):
			each_col += self.point_col_spacing._frac_x
			self._canvas.create_line(
				each_col * self.canvas_width, 0, each_col * self.canvas_width, self.canvas_height)

		

	def _clicked_cell(self, event: tkinter.Event):
		start_row = 1
		start_col = 1
		click_point = point.from_pixel(event.x, event.y, self.canvas_width, self.canvas_height)
		for row in range(1, self._othello_state.rows + 1):
			if start_row*self.point_row_spacing._frac_y < click_point._frac_y:
				start_row += 1
			else:
				player_move_row = row
				break
		for column in range(1, self._othello_state.columns + 1):
			if start_col*self.point_col_spacing._frac_x < click_point._frac_x:
				start_col += 1
			else:
				player_move_col = column
				break

		return (player_move_row, player_move_col)

		
	def _add_move_circle(self, event: tkinter.Event):
		if self._othello_state != None:
			if self._othello_state.isGameOver() != True:
				player_move = self._clicked_cell(event)
				if self._othello_state.addMoveToState(player_move[0], player_move[1]):
					self._draw_circles()
					self._othello_state.changeTurn()
					if self._othello_state.isGameOver() == True:
						self._show_pieces()
						self._show_winner()
					else:
						self._show_turn()
						self._show_pieces()



	def _draw_circle_black(self, move):
			self._canvas.create_oval(
				(self.canvas_width * (move[1]-1) * self.point_col_spacing._frac_x) + 10,
				(self.canvas_height * (move[0]-1) * self.point_row_spacing._frac_y) + 10,
				(self.canvas_width * (move[1]) * self.point_col_spacing._frac_x) - 10,
				(self.canvas_height * (move[0]) * self.point_row_spacing._frac_y) - 10, fill = 'black')

	def _draw_circle_white(self, move):
			self._canvas.create_oval(
				(self.canvas_width * (move[1]-1) * self.point_col_spacing._frac_x) + 10,
				(self.canvas_height * (move[0]-1) * self.point_row_spacing._frac_y) + 10,
				(self.canvas_width * (move[1]) * self.point_col_spacing._frac_x) - 10,
				(self.canvas_height * (move[0]) * self.point_row_spacing._frac_y) - 10, fill = 'white')

	def _draw_circles(self):
		for row in range(self._othello_state.rows):
			for column in range(self._othello_state.columns):
				if self._othello_state.board[row][column] == 1:
					self._draw_circle_black((row+1,column+1))
				elif self._othello_state.board[row][column]:
					self._draw_circle_white((row+1,column+1))


	def _show_turn(self):
		if self._othello_state.turn == 1:
			self._turn.set('Turn: {}'.format('Black'))
		else:
			self._turn.set('Turn: {}'.format('White'))

	def _show_pieces(self):
		self._othello_state.checkNumTiles()
		self._black_pieces.set('Black: {}'.format(self._othello_state.blackPieces))
		self._white_pieces.set('White: {}'.format(self._othello_state.whitePieces))


	def _show_winner(self):
		if self._othello_state.isGameOver() == True:
			if self._othello_state.winType == '>':
				self._othello_state.checkWinnerMost()
				if self._othello_state.winner == 1:
					self._turn.set(
						'Winner: {}\n\nHit "Start New Game"\nbutton to play again'.format('Black'))
				elif self._othello_state.winner == 2:
					self._turn.set(
						'Winner: {}\n\nHit "Start New Game"\nbutton to play again'.format('White'))
				elif self._othello_state.winner == 0:
					self._turn.set(
						'Winner: {}\n\nHit "Start New Game"\nbutton to play again'.format('None'))
			elif self._othello_state.winType == '<':
				self._othello_state.checkWinnerLeast()
				if self._othello_state.winner == 1:
					self._turn.set(
						'Winner: {}\n\nHit "Start New Game"\nbutton to play again'.format('Black'))
				elif self._othello_state.winner == 2:
					self._turn.set(
						'Winner: {}\n\nHit "Start New Game"\nbutton to play again'.format('White'))
				elif self._othello_state.winner == 0:
					self._turn.set(
						'Winner: {}\n\nHit "Start New Game"\nbutton to play again'.format('None'))


	










if __name__ == '__main__':
	Othello().start()
