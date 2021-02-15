import chess
import chess.engine
import time

start_time = time.time()
#r1bq1rkR/1ppnbpp1/p3p3/4P3/4BB2/4P3/PPP2PP1/RN1QK3 w Qq - 1 1
board = chess.Board("rnbqkbnr/p1pp1ppp/1p2p3/6B1/3P4/8/PPP1PPPP/RN1QKBNR w KQkq - 0 1")
print(board)
engine = chess.engine.SimpleEngine.popen_uci("/home/qqze/Documents/NeuralWorks/NeuralChess/NeuralChess/V00/stockfish_20090216_x64_bmi2")

class Node:
    def __init__(self, eval, position):
        self.eval = eval
        self.position = position

#position = [board, evaluation]
def moveToPosition(board, move):
    childBoard = board.copy()
    childBoard.push_san(str(move))
    return childBoard

def minimax(node, depth, maxPlayer, move=""):
    if depth == 0 or node.is_game_over():
        evalDict = engine.analyse(node, chess.engine.Limit(depth=0))
        return evalDict["score"].relative.score(mate_score=100000)

    if maxPlayer:
        value = -1000000
        for child in node.legal_moves:
            eval = minimax(moveToPosition(node, child), depth - 1, False, child)
            value = max(value, eval)
            print(f"max value: {value}")
            print(depth)
            print(child)
        return value

    else:
        value = 1000000
        for child in node.legal_moves:
            eval = minimax(moveToPosition(node, child), depth - 1, True, child)
            print(depth)
            value = min(value, eval)
        print(f"min value: {value}")
        return value


print(minimax(board, 3, True))
print(f"finished in {time.time() - start_time} seconds")
print(board.legal_moves)