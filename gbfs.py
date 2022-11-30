from solver import Solver
import collections

class GBFSSolver(Solver):
    def solve(self):
        # Implemented as Breadth First Search over the Game State Space
        search_path_length = 0
        queue = [self.game]
        visited = [self.game.copy()]

        while len(queue) > 0:
            if search_path_length > self.max:
                return None
            board = queue.pop(0)
            search_path_length += 1
            self.appendSearchString(board, self.calculateHeuristic(board))

            if board.checkWin():
                return board, search_path_length

            Moves = []
            for move in board.getAllValidMoves():
                board.makeMove(*move)
                if board.carArr not in visited:
                    Moves.append([self.calculateHeuristic(board), board.fullCopy()])
                board.undo()

            sortedMoves = sorted(Moves, key=lambda x: x[0], reverse=True)
            for board in sortedMoves:
                queue.insert(0, board[1].fullCopy())
                visited.insert(0, board[1].copy())

        return None
   
    def calculateHeuristic(self, board):
       pass
