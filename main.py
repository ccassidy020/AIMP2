from rush_hour import RushHour
from solver import Solver



class UCSSearch(Solver):
	def solve(self):
		search_path_length = 0
		queue = [self.game]
		visited = [self.game.copy()]

		while len(queue) > 0:
			board = queue.pop(0)
			search_path_length += 1
			if board.checkWin():
				return board, search_path_length
			for move in board.getAllValidMoves():
				board.makeMove(*move)
				if board.carArr not in visited:
					queue.append(board.fullCopy())
					visited.append(board.copy())
				board.undo()

		return None

if __name__ == '__main__':
	cases = [x.strip() for x in open("./sample-input.txt", "r").readlines() if x[0] != '#' and x[0] != '\n']
	# s = UCSSearch(".BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0")
	for i, case in enumerate(cases):
		s = UCSSearch(case)
		open("./output/ucs-sol-" + str(i + 1) + ".txt", "w").write(s.out)