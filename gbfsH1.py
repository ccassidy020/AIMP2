from gbfs import GBFSSolver
class GBFSSolverH1(GBFSSolver):
    def calculateHeuristic(self, board):
        ambulance = board.cars['A']
        carsInWay = 0
        for car in board.cars.values():
            if ambulance.isInWay(car):
                carsInWay += 1
        return carsInWay