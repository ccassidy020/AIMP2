from gbfs import GBFSSolver
class GBFSSolverH2(GBFSSolver):
    def calculateHeuristic(self, board):
        ambulance = board.cars['A']
        blockedPositions = 0
        for car in board.cars.values():
            if ambulance.isInWay(car):
                if car.isHor:
                    blockedPositions += car.w
                else:
                    blockedPositions += 1
        return blockedPositions