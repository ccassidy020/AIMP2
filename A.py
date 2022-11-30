from solver import Solver
import collections

class ASolver(Solver):
    def solve(self):
        # Implemented as Breadth First Search over the Game State Space
        search_path_length = 0
        queue = [self.game]
        visited = [self.game.copy()]

        while len(queue) > 0:
            if search_path_length > self.max:
                return None
            bestBoard = None
            for board in queue:
                if(bestBoard == None or self.calculateHeuristic(board) + len(board.moves) < self.calculateHeuristic(bestBoard) + len(bestBoard.moves)):
                    bestBoard = board

            board = queue.pop(queue.index(bestBoard))
            search_path_length += 1
            self.appendSearchString(board, self.calculateHeuristic(board))

            if board.checkWin():
                return board, search_path_length

            for move in board.getAllValidMoves():
                board.makeMove(*move)
                if board.carArr not in visited:
                    queue.append(board.fullCopy())
                    visited.append(board.copy())
                board.undo()
        return None
   
    def calculateHeuristic(self, board):
       pass
