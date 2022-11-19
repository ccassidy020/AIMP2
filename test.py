from rush_hour import RushHour

def test_sample():
	rh = RushHour(".BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0")
	# print(rh.getFormattedBoard())
	rh.makeMove("B", "left", 1)
	rh.makeMove("E", "left", 2)
	rh.makeMove("I", "up", 2)
	rh.makeMove("A", "right", 1)
	rh.makeMove("H", "up", 1)
	rh.makeMove("G", "left", 1)
	rh.makeMove("J", "down", 2)
	rh.makeMove("F", "left", 2)
	rh.makeMove("K", "down", 2)
	rh.makeMove("A", "right", 2)
	rh.makeMove("I", "down", 1)
	rh.makeMove("C", "left", 1)
	rh.makeMove("L", "up", 1)
	rh.makeMove("A", "right", 1)
	assert rh.checkWin() == True and rh.getFormattedBoard() == "BBCCCLEEI..LH.I.AAH.FFK.GGGJKM...J.M"

from solver import Solver
class TestSolver(Solver):
	def solve(self):
		self.game.makeMove("B", "left", 1)
		self.game.makeMove("E", "left", 2)
		self.game.makeMove("I", "up", 2)
		self.game.makeMove("A", "right", 1)
		self.game.makeMove("H", "up", 1)
		self.game.makeMove("G", "left", 1)
		self.game.makeMove("J", "down", 2)
		self.game.makeMove("F", "left", 2)
		self.game.makeMove("K", "down", 2)
		self.game.makeMove("A", "right", 2)
		self.game.makeMove("I", "down", 1)
		self.game.makeMove("C", "left", 1)
		self.game.makeMove("L", "up", 1)
		self.game.makeMove("A", "right", 1)
		return self.game, 200


def test_solver():
	s = TestSolver(".BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0")
	print(s.out)

# test_sample()
test_solver()