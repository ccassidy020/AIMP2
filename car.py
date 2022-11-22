from typing import List



dirMap = {
	"up": (0, -1),
	"down": (0, 1),
	"right": (1, 0),
	"left": (-1, 0)
}

class CarQuery:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

class Car:
	def __init__(self, symbol: str, position: List[int]):
		self.symbol = symbol
		self.position = position
		self.fuel = 100
		self.length = 1
		self._savePos: List[int] = None
	
	def copy(self):
		c = Car(self.symbol, self.position.copy())
		c.fuel = self.fuel
		c.length = self.length
		c.direction = self.direction
		if self._savePos is None:
			c._savePos = None
		else:
			c._savePos = self._savePos.copy()
		return c


	def addPosition(self, position: List[int]):
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
		self._savePos = [None]*2
		self._savePos[0] = self.position[0]
		self._savePos[1] = self.position[1]
	
	def restore(self):
		if (self._savePos is None):
			print("Cannot restore from None!")
			return
		self.position[0] = self._savePos[0]
		self.position[1] = self._savePos[1]
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
			# print(self.symbol + " collides with " + other.symbol + "!")
			return True
		return False
	
	def filterCollided(self, cars):
		if self.direction == "hor":
			q1 = CarQuery(0, self.y, self.x, 0)
			q2 = CarQuery(self.x, self.y, 5 - self.x, 0)
		elif self.direction == "vert":
			q1 = CarQuery(self.x, 0, 0, self.y)
			q2 = CarQuery(self.x, self.y, 0, 5 - self.y)
		
		return [car for car in cars if car is not self and (car.checkCollision(q1) or car.checkCollision(q2))]
	
	def computeDistance(self, cars):
		if self.direction == "hor":
			s_p = self.x
			s_s = self.w
		else:
			s_p = self.y
			s_s = self.h
		n = s_p
		p = 5 - (s_p + s_s)
		for car in self.filterCollided(cars):
			if self.direction == "hor":
				c_p = car.x
				c_s = car.w
			else:
				c_p = car.y
				c_s = car.h
			if c_p < s_p:
				n = min(n, s_p - (c_p + c_s + 1))
			else:
				p = min(p, c_p - (s_p + s_s + 1))
		return (n, p)

	def getValidMoves(self, cars):
		if self.fuel == 0:
			return []
		n,p = self.computeDistance(cars)
		if self.fuel < n:
			n = self.fuel
		if self.fuel < p:
			p = self.fuel

		return *[(self.symbol, "left" if self.direction == "hor" else "up", i + 1) for i in range(n)], *[(self.symbol, "right" if self.direction == "hor" else "down", i + 1) for i in range(p)]


	
	def __repr__(self):
		return "<Pos: " + str(self.position) + ", Dir: " + self.direction + ", Dims: " + str((self.w, self.h)) + ", Fuel: " + str(self.fuel) + ">"

	def checkWin(self):
		if self.symbol == "A" and self.y == 2 and self.x == 5 - (self.length  - 1):
			return True
		return False



	def forceMove(self, direction, amt):
		move = dirMap[direction]
		self.position[0] = self.position[0] + (move[0] * amt)
		self.position[1] = self.position[1] + (move[1] * amt)
		self.fuel += amt

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
		self.position[0] = self.position[0] + move[0]
		self.position[1] = self.position[1] + move[1]
		if not self.isPositionValid(cars):
			# raise Exception("Move is invalid!")
			print("Move is invalid!")
			self.restore()
			return False
		self.fuel -= 1
		return True