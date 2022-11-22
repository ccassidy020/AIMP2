import math

from rush_hour import RushHour
from time import time
from typing import Tuple

class Solver:
	def __init__(self, initalState: str, max_search: int = 1000000, ignore = False):
		self.game: RushHour = RushHour(initalState)
		self.initalState: str = initalState
		self.out: str = ""
		self.out_search: str = ""
		self.solution_found = False
		self.max = max_search
		self.ignore = ignore

		if ignore:
			self.run()
			return
		self.out += "Initial board configuration: " + initalState + "\n\n"
		for i in range(36):
			if i % 6 == 0 and i != 0:
				self.out += '\n'
			self.out += initalState[i]
		self.out += '\n\n'

		self.out += "Car fuel available: " + ", ".join([(car + ":" + str(self.game.cars[car].fuel)) for car in self.game.cars]) + "\n\n"
		self.run()

	# Function that takes the current board state and optionally the value of h(n) and adds an entry to the search file string 
	def appendSearchString(self, board: RushHour, h_n: int = 0):
		g_n = len(board.moves)

		self.out_search += "{:} {:} {:} {:}\n".format(g_n + h_n, g_n, h_n, board.getFormattedBoard())
	
	def run(self):
		t_init = time()
		res = self.solve()
		if res is None:
			self.out = "no solution"
			return
		self.solution_found = True
		game_state, num_search = res
		t_end = time()

		self.execution_time = t_end - t_init
		self.search_path_length = num_search
		self.solution_path_length = len(game_state.moves)
		
		if self.ignore:
			return

		precision = max(2, abs(round(math.log10(self.execution_time))))

		self.out += "Runtime: " + (("%." + str(precision) + "f") % round(self.execution_time, precision)) + " seconds\n"
		self.out += "Search path length: " + str(self.search_path_length) + " states\n"
		self.out += "Solution path length: " + str(self.solution_path_length) + " moves\n"
		self.out += "Solution path: " + "; ".join(["{:} {:} {:}".format(car, direction, amt) for (car, direction, amt) in game_state.moves]) + "\n\n"

		new_game = RushHour(self.initalState)
		for (car, direction, amt) in game_state.moves:
			new_game.makeMove(car, direction, amt)
			self.out += new_game.debugString(new_game.cars[car], direction, amt) + "\n"
		self.out += "\n"
		
		final_board = game_state.getFormattedBoard()
		for i in range(36):
			if i % 6 == 0 and i != 0:
				self.out += '\n'
			self.out += final_board[i]
	
	# This function is meant to be overriden to implement algorithm
	def solve(self) -> Tuple[RushHour, int]:
		'''
    	Function that is called automatically to run the algorithm

            Returns:
					game (RushHour): Final game state found by algorithm
					search_path_length (int): The length of the search path of the algorithm
				
				OR
					None if no solution is found
    	'''
		pass
