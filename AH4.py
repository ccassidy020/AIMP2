from A import ASolver
class ASolverH4(ASolver):
    def calculateHeuristic(self, board):
        ambulance = board.cars['A']
        carsInWay = 0
        for car in board.cars.values():
            if ambulance.isInWay(car):
                carsInWay += 1
                for car2 in board.cars.values():
                    if car.isInWay(car2):
                        carsInWay += 1
        return carsInWay