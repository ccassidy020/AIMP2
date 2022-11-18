from typing import Tuple

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