import math
from car import Car
from typing import Dict, List, Tuple

undoMap = {
	"up": "down",
	"down": "up",
	"right": "left",
	"left": "right"
}

class RushHour:
	def __init__(self, startState: str = None):
		if startState is None:
			return
		self.moves: List[Tuple[str,str,int]] = []
		self.cars: Dict[str, Car] = {}
		[map, *fuel] = startState.split(" ")
		for (i, c) in enumerate(map):
			x = i % 6
			y = math.floor(i / 6)

			if c.isalpha():
				if c not in self.cars:
					self.cars[c] = Car(c, [x,y])
				else:
					self.cars[c].addPosition([x,y])
		for car in fuel:
			[symbol, amt] = list(car)
			self.cars[symbol].fuel = int(amt)
		self.carArr = [car.position for car in self.cars.values()]
	
	def fullCopy(self):
		rh = RushHour()
		rh.moves = self.moves.copy()
		rh.cars = {}
		for car in self.cars:
			rh.cars[car] = self.cars[car].copy()

		rh.carArr = [car.position for car in rh.cars.values()]
		return rh
	
	def makeMove(self, car: str, direction: str, amt: int):
		for _ in range(0, amt):
			self.cars[car].move(direction, self.getCars())

		self.moves.append((car, direction, amt))
		if self.cars[car].checkToBeRemoved():
			self.cars[car].removed = True
	
	def copy(self):
		return [car.copy() for car in self.carArr]
	
	def getCars(self):
		return [self.cars[car] for car in self.cars if not self.cars[car].removed]
	
	def undo(self):
		car, direction, amt= self.moves.pop()
		target_car = self.cars[car]
		if target_car.removed:
			target_car.removed = False

		target_car.forceMove(undoMap[direction], amt)
	
	def checkWin(self):
		win = False
		for car in self.getCars():
			if car.checkWin():
				win = True
		return win
	
	def getAllValidMoves(self) -> List[Tuple[str, str, int]]:
		out = []
		cars = self.getCars()
		for car in cars:
			out += car.getValidMoves(cars)
		return out
	
	def getFormattedBoard(self) -> str:
		out = ["."] * 36
		for symbol in self.cars:
			car = self.cars[symbol]
			if car.removed:
				continue
			if car.isHor:
				for i in range(car.length):
					out[indexFromPos(car.x + i, car.y)] = car.symbol
			else:
				for i in range(car.length):
					out[indexFromPos(car.x, car.y + i)] = car.symbol

		return "".join(out)
	
	def debugString(self, car: Car, dir: str, amt: int) -> str:
		return "{:>1} {:>5} {:>1} {:>8} {:>36}".format(car.symbol, dir, amt, car.fuel, self.getFormattedBoard())

def indexFromPos(x: int, y: int) -> int:
	return (y * 6) + x