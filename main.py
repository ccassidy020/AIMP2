from rush_hour import RushHour

if __name__ == '__main__':
	rh = RushHour(".BBCCC..EEKLAAIJKLH.IJFFHGGG.M.....M K6 M0")
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
