import math
from car import Car
from typing import Dict, List, Tuple

class RushHour:
	def __init__(self, startState: str):
		self.moves: List[Tuple[str,str,int]] = []
		self.cars: Dict[str, Car] = {}
		[map, *fuel] = startState.split(" ")
		for (i, c) in enumerate(map):
			x = i % 6
			y = math.floor(i / 6)

			if c.isalpha():
				if c not in self.cars:
					self.cars[c] = Car(c, (x,y))
				else:
					self.cars[c].addPosition((x,y))
		for car in fuel:
			[symbol, amt] = list(car)
			self.cars[symbol].fuel = int(amt)
	
	def makeMove(self, car: str, direction: str, amt: int):
		won = False
		for _ in range(0, amt):
			if self.cars[car].move(direction, self.cars.values()):
				if self.cars[car].checkWin():
					won = True
			else:
				return 0

		self.moves.append((car, direction, amt))
		# self.debugPrint(self.cars[car], direction, amt)
		if won:
			return 2
			# print("GAME WON!")
		return 1
	
	def checkWin(self):
		win = False
		for car in self.cars.values():
			if car.checkWin():
				win = True
		return win
	
	def getAllValidMoves(self):
		out = []
		for car in self.cars.values():
			out += car.getValidMoves(self.cars.values())
		return out


	
	def getFormattedBoard(self):
		out = ["."] * 36
		for symbol in self.cars:
			car = self.cars[symbol]
			if car.direction == "hor":
				for i in range(car.length):
					out[indexFromPos(car.x + i, car.y)] = car.symbol
			else:
				for i in range(car.length):
					out[indexFromPos(car.x, car.y + i)] = car.symbol

		return "".join(out)
	
	def debugString(self, car: Car, dir: str, amt: int):
		return "{:>1} {:>5} {:>1} {:>8} {:>36}".format(car.symbol, dir, amt, car.fuel, self.getFormattedBoard())

def indexFromPos(x,y):
	return (y * 6) + x