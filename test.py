from rush_hour import RushHour

def test_distances(rh: RushHour, init: bool):
	if init:
		expected = {
			"B": (1, 0),
			"C": (0, 0),
			"E": (2, 0),
			"K": (0, 0),
			"L": (0, 0),
			"A": (0, 0),
			"I": (0, 0),
			"J": (0, 0),
			"H": (0, 1),
			"F": (0, 0),
			"G": (0, 1),
			"M": (0, 0)
		}
	else:
		expected = {
			"B": (0, 0),
			"C": (0, 0),
			"E": (0, 0),
			"K": (0, 1),
			"L": (0, 0),
			"A": (1, 0),
			"I": (0, 0),
			"J": (0, 0),
			"H": (0, 0),
			"F": (1, 0),
			"G": (0, 0),
			"M": (1, 0)
		}

	for car in rh.cars:
		assert rh.cars[car].computeDistance(rh.cars.values()) == expected[car]


def test_sample():
	rh = RushHour(".BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0")
	test_distances(rh, True)
	# print(rh.cars["E"].getValidMoves(rh.cars.values()))
	print(rh.getAllValidMoves())
	print(rh.carArr)
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
	print(rh.carArr)
	test_distances(rh, False)
	# for car in rh.cars:
	# 	print('"' + car + '": ' + str(rh.cars[car].computeDistance(rh.cars.values())) + ",")
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
	out = """Initial board configuration: .BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0

.BBCCC
..EEKL
AAIJKL
H.IJFF
HGGG.M
.....M

Car fuel available: B:100, C:100, E:100, K:6, L:100, A:100, I:100, J:100, H:100, F:100, G:100, M:0

Runtime: 0.00015783309936523438
Search path length: 200 states
Solution path length: 14 moves
Solution path: B left 1; E left 2; I up 2; A right 1; H up 1; G left 1; J down 2; F left 2; K down 2; A right 2; I down 1; C left 1; L up 1; A right 1

B  left 1       99 BB.CCC..EEKLAAIJKLH.IJFFHGGG.M.....M
E  left 2       98 BB.CCCEE..KLAAIJKLH.IJFFHGGG.M.....M
I    up 2       98 BBICCCEEI.KLAA.JKLH..JFFHGGG.M.....M
A right 1       99 BBICCCEEI.KL.AAJKLH..JFFHGGG.M.....M
H    up 1       99 BBICCCEEI.KLHAAJKLH..JFF.GGG.M.....M
G  left 1       99 BBICCCEEI.KLHAAJKLH..JFFGGG..M.....M
J  down 2       98 BBICCCEEI.KLHAA.KLH...FFGGGJ.M...J.M
F  left 2       98 BBICCCEEI.KLHAA.KLH.FF..GGGJ.M...J.M
K  down 2        4 BBICCCEEI..LHAA..LH.FFK.GGGJKM...J.M
A right 2       97 BBICCCEEI..LH..AALH.FFK.GGGJKM...J.M
I  down 1       97 BB.CCCEEI..LH.IAALH.FFK.GGGJKM...J.M
C  left 1       99 BBCCC.EEI..LH.IAALH.FFK.GGGJKM...J.M
L    up 1       99 BBCCCLEEI..LH.IAA.H.FFK.GGGJKM...J.M
A right 1       96 BBCCCLEEI..LH.I.AAH.FFK.GGGJKM...J.M

BBCCCL
EEI..L
H.I.AA
H.FFK.
GGGJKM
...J.M"""
	s = TestSolver(".BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0")
	print(s.out)
	print(s.game.checkWin())
	# assert out == s.out

test_sample()
test_solver()