from rush_hour import RushHour
from time import time
from typing import Tuple

class Solver:
	out: str = ""
	initalState: str
	game: RushHour

	def __init__(self, initalState: str):
		self.game = RushHour(initalState)
		self.initalState = initalState
		self.out += "Initial board configuration: " + initalState + "\n\n"
		for i in range(36):
			if i % 6 == 0 and i != 0:
				self.out += '\n'
			self.out += initalState[i]
		self.out += '\n\n'

		self.out += "Car fuel available: " + ", ".join([(car + ":" + str(self.game.cars[car].fuel)) for car in self.game.cars]) + "\n\n"
		self.run()


	def run(self):
		t_init = time()
		game_state, num_search = self.solve()
		t_end = time()
		self.out += "Runtime: " + str(t_end - t_init) + "\n"
		self.out += "Search path length: " + str(num_search) + " states\n"
		self.out += "Solution path length: " + str(len(game_state.moves)) + " moves\n"
		self.out += "Solution path: " + "; ".join(["{:} {:} {:}".format(car, direction, amt) for (car, direction, amt) in game_state.moves]) + "\n\n"
		self.out += "\n".join([game_state.debugString(game_state.cars[car], direction, amt) for (car, direction, amt) in game_state.moves]) + "\n\n"

		final_board = game_state.getFormattedBoard()
		for i in range(36):
			if i % 6 == 0 and i != 0:
				self.out += '\n'
			self.out += final_board[i]
		self.out += '\n'

	
	# This function is meant to be overriden to implement algorithm
	
	def solve(self) -> Tuple[RushHour, int]:
		'''
    	Function that is called automatically to run the algorithm

            Parameters:

            Returns:
					game (RushHour): Final game state found by algorithm
					search_path_length (int): The length of the search path of the algorithm
    	'''
		pass


