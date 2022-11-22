from rush_hour import RushHour
from solver import Solver



class UCSSearch(Solver):

	def bfs(self):
		queue = [self.game]
		visited = [self.game.copy()]

		print(queue)

		while len(queue) > 0:
			board = queue.pop(0)
			if board is None:
				print(queue)
			print(board.carArr)
			if board.checkWin():
				return board
			for move in board.getAllValidMoves():
				board.makeMove(*move)
				if board.carArr not in visited:
					queue.append(board.fullCopy())
					visited.append(board.copy())
				board.undo()

		raise Exception("NO path found")
			

	# def bfs(self):
	# 	queue = []
	# 	for move in self.game.getAllValidMoves():
	# 		queue.append(move)
	# 		queue.append(None)
	# 	visited = []

	# 	while len(queue) > 0:
	# 		move = queue.pop(0)
	# 		if move is None:
	# 			self.game.undo()
	# 			continue
	# 		print(move)

	# 		self.game.makeMove(*move)
	# 		if self.game.checkWin():
	# 			return
	# 		if self.game.carArr in visited:
	# 			self.game.undo()
	# 			continue


			
	# 		queue.append(move)
	# 		for move in self.game.getAllValidMoves():
	# 			queue.append(move)
	# 			queue.append(None)
	# 		queue.append(None)

	def solve(self):
		search_path_length = 0
		queue = [self.game]
		visited = [self.game.copy()]

		print(queue)

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

		raise Exception("No path found")

		# return self.bfs(), 100

if __name__ == '__main__':
	print([x.strip() for x in open("./sample-input.txt", "r").readlines() if x[0] != '#' and x[0] != '\n'])
	s = UCSSearch(".BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0")
	print(s.out)


	# visted = []
	# a = [[1,2], [1,2]]
	# visted.append([i.copy() for i in a])
	# print(visted)
	# a[0][1] = 4
	# print(visted)
	# print(a)
	# print(a == visted[0])
	# a[0][1] = 2
	# print(a == visted[0])

