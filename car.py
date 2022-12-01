from typing import List, Tuple

dirMap = {
	"up": (0, -1),
	"down": (0, 1),
	"right": (1, 0),
	"left": (-1, 0)
}

class Car:
	def __init__(self, symbol: str, position: List[int]):
		self.isHor = False
		self.symbol = symbol
		self.position = position
		self.fuel = 100
		self.length = 1
		self.removed = self.checkToBeRemoved()
	
	def copy(self):
		c = Car(self.symbol, self.position.copy())
		c.fuel = self.fuel
		c.length = self.length
		c.isHor = self.isHor
		c.removed = self.removed
		return c

	def addPosition(self, position: List[int]):
		if self.position[1] == position[1]:
			self.isHor = True
		self.length += 1

	@property
	def h(self):
		return 0 if self.isHor else self.length - 1
	
	@property
	def w(self):
		return self.length - 1 if self.isHor else 0
	
	@property
	def x(self):
		return self.position[0]

	@property
	def y(self):
		return self.position[1]

	def isPositionValid(self, cars) -> bool:
		if self.x < 0 or self.y < 0 or self.x + self.w > 5 or self.y + self.h > 5:
			return False
		for car in cars:
			if car is self:
				continue
			if self.checkCollision(car):
				return False
		return True
	
	def checkCollision(self, other) -> bool:
		if self.x <= other.x + other.w and self.x + self.w >= other.x and self.y <= other.y + other.h and self.y + self.h >= other.y:
			return True
		return False
	
	def isInWay(self, car):
		if car is self:
			return False

		if self.isHor:
			if self.y >= car.y and self.y <= car.y + car.h:
				return True
		else: 
			if self.x >= car.x and self.x <= car.x + car.w:
				return True

		return False
	
	def computeDistance(self, cars):
		if self.isHor:
			s_p = self.x
			s_s = self.w
		else:
			s_p = self.y
			s_s = self.h
		n = s_p
		p = 5 - (s_p + s_s)

		for car in cars:
			if not self.isInWay(car):
				continue

			if self.isHor:
				c_p = car.x
				c_s = car.w
			else:
				c_p = car.y
				c_s = car.h
			if c_p < s_p:
				n = min(n, s_p - (c_p + c_s + 1))
			else:
				p = min(p, c_p - (s_p + s_s + 1))
		return n, p

	def getValidMoves(self, cars) -> List[Tuple[str, str, int]]:
		if self.fuel == 0:
			return []
		n,p = self.computeDistance(cars)
		if self.fuel < n:
			n = self.fuel
		if self.fuel < p:
			p = self.fuel

		n_dir, p_dir = "left" if self.isHor else "up", "right" if self.isHor else "down"

		return *[(self.symbol, n_dir, i + 1) for i in range(n)], *[(self.symbol, p_dir, i + 1) for i in range(p)]

	def __repr__(self):
		return self.symbol+ ": <Pos: " + str(self.position) + ", Dir: " + ("hor" if self.isHor else "vert") + ", Dims: " + str((self.w, self.h)) + ", Fuel: " + str(self.fuel) + ">"

	def checkWin(self):
		if self.symbol == "A" and self.y == 2 and self.x == 5 - (self.length  - 1):
			return True
		return False
	
	def checkToBeRemoved(self):
		if self.symbol != "A" and self.isHor and self.y == 2:
			if self.x + self.w == 5:
				return True
		return False

	def forceMove(self, direction, amt):
		move = dirMap[direction]
		self.position[0] += move[0] * amt
		self.position[1] += move[1] * amt
		self.fuel += amt

	def move(self, direction, cars):
		if self.fuel == 0:
			raise Exception('Car "{:}" tried to move but does not have fuel!'.format(self.symbol))

		if self.isHor and (direction == "up" or direction == "down"):
			raise Exception('Car "{:}" tried to move vertically!'.format(self.symbol))

		if not self.isHor and (direction == "right" or direction == "left"):
			raise Exception('Car "{:}" tried to move horizontally!'.format(self.symbol))
		
		move = dirMap[direction]
		self.position[0] += move[0]
		self.position[1] += move[1]
		if not self.isPositionValid(cars):
			raise Exception('Car "{:}" tried to move to a position that either puts it out of bounds or colliding with another car!'.format(self.symbol))
		self.fuel -= 1