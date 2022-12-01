import random
from car import Car
from ucs import UCSSearch
from rush_hour import RushHour
from time import time

from typing import List
import threading
import math


pieces = {
	"A": 2,
	"B": 2,
	"C": 3,
	"K": 2,
	"I": 2,
	"J": 2,
	"G": 3,
	"H": 2,
	"L": 2,
	"M": 2,
	"F": 2,
	"E": 2
}
import sys
class Generator:
	def __init__(self, num):
		self.num = num
	
	def generate(self) -> List[str]:
		boards = []
		total_time = 0
		for i in range(self.num):
			t_init = time()
			boards.append(self.generateBoard())
			t_final = time()
			total_time += t_final - t_init
			average_time = total_time / (i + 1)
			estimated_time_remaining = average_time * (self.num - i - 1)
			minutes = math.floor(estimated_time_remaining / 60)
			hours = math.floor(minutes / 60)
			minutes = round(((minutes / 60) - hours) * 60)
			seconds = round(((estimated_time_remaining / 60) - minutes) * 60)
			print("Remaining: {:} (Estimated time: {:}:{:}:{:})".format(self.num - i - 1, '%02d' % hours, '%02d' % minutes, '%02d' % seconds), end='\r')
		print()
		return boards
	
	def generateBoard(self) -> str:
		solvable = False
		while not solvable:
			cars = []
			for piece in pieces:
				valid = False
				while not valid:
					length = pieces[piece]
					if piece == "A":
						isHor = True
						pos = [random.randint(0, 3), 2]

					else:
						isHor = bool(random.randint(0, 1))

						if isHor:
							pos = [random.randint(0, 5 - length), random.randint(0, 5)]
						else:
							pos = [random.randint(0, 5), random.randint(0, 5 - length)]
					
					car = Car(piece, pos)
					car.length = length
					car.isHor = isHor
					valid = car.isPositionValid(cars)
				cars.append(car)
			
			rh = RushHour()
			rh.cars = {}
			for car in cars:
				rh.cars[car.symbol] = car
			rh.moves = []
			rh.carArr = [car.position for car in rh.cars.values()]
			board = rh.getFormattedBoard()
			algo = UCSSearch(board, 10000, True)
			solvable = algo.solution_found and algo.search_path_length > 100
		return board
		


open("./generated-input4.txt", "w").write("\n".join(Generator(50).generate()))
