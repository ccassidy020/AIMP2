import math
from typing import Dict, Tuple


dirMap = {
	"up": (0, -1),
	"down": (0, 1),
	"right": (1, 0),
	"left": (-1, 0)
}

class Car:
	isAmbulance: False
	position: Tuple[int, int]
	_savePos: Tuple[int, int] = None
	fuel: int = 100
	length: int = 1
	direction: str
	symbol: str
	def __init__(self, symbol: str, position: Tuple[int]):
		self.symbol = symbol
		self.isAmbulance = symbol == "A"
		self.position = position

	def addPosition(self, position: Tuple[int, int]):
		if (self.position[0] == position[0]):
			self.direction = "vert"
		else:
			self.direction = "hor"
		self.length += 1

	@property
	def h(self):
		if (self.direction == "hor"):
			return 0
		else:
			return self.length - 1
	
	@property
	def w(self):
		if (self.direction == "hor"):
			return self.length - 1
		else:
			return 0
	
	@property
	def x(self):
		return self.position[0]

	@property
	def y(self):
		return self.position[1]

	def save(self):
		self._savePos = self.position
	
	def restore(self):
		if (self._savePos is None):
			print("Cannot restore from None!")
			return
		self.position = self._savePos
		self._savePos = None
	
	def deleteSave(self):
		self._savePos = None


	def isPositionValid(self, cars) -> bool:
		if (self.x < 0 or self.y < 0 or self.x + self.w > 5 or self.y + self.h > 5):
			return False
		for car in cars:
			if car is self:
				continue
			if (self.checkCollision(car)):
				return False
		return True

	
	def checkCollision(self, other) -> bool:
		if (self.x <= other.x + other.w and self.x + self.w >= other.x and self.y <= other.y + other.h and self.y + self.h >= other.y):
			print(self.symbol + " collides with " + other.symbol + "!")
			return True
		return False
	
	def __repr__(self):
		return "<Pos: " + str(self.position) + ", Dir: " + self.direction + ", Dims: " + str((self.w, self.h)) + ", Fuel: " + str(self.fuel) + ">"

	def checkWin(self):
		if self.isAmbulance and self.y == 2 and self.x == 5 - (self.length  - 1):
			return True
		return False



	def move(self, direction, cars) -> bool:
		if (self.fuel == 0):
			print("Not enough fuel!")
			return False

		if (self.direction == "hor" and (direction == "up" or direction == "down")):
			print("Car can only move horizontally!")
			return False

		if (self.direction == "vert" and (direction == "right" or direction == "left")):
			print("Car can only move vertically!")
			return False
		
		self.save()
		move = dirMap[direction]
		self.position = (self.position[0] + move[0], self.position[1] + move[1])
		if not self.isPositionValid(cars):
			# raise Exception("Move is invalid!")
			print("Move is invalid!")
			self.restore()
			return False
		self.fuel -= 1
		return True

		
		


		

		

		




class RushHour:
	cars: Dict[str, Car] = {}
	def __init__(self, startState: str):
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
				print(car, direction, amt)

		self.debugPrint(self.cars[car], direction, amt)
		if won:
			print("GAME WON!")
		return True
	
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
	
	def debugPrint(self, car: Car, dir: str, amt: int):
		print("{:>1} {:>5} {:>1} {:>8} {:>36}".format(car.symbol, dir, amt, car.fuel, self.getFormattedBoard()))



def indexFromPos(x,y):
	return (y * 6) + x