from A import ASolver
class ASolverH2(ASolver):
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