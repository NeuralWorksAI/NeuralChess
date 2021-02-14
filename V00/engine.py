import chess
import chess.engine

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("/home/qqze/Documents/NeuralWorks/NeuralChess/NeuralChess/V00/stockfish_20090216_x64_bmi2")

#position = [board, evaluation]
def moveToPosition(board, move):
    childBoard = board.copy()
    childBoard.push_san(str(move))
    return childBoard

def minimax(position, depth, maxPlayer):
    if depth == 0 or position.is_game_over():
        evalDict = engine.analyse(position, chess.engine.Limit(depth=1))
        print(evalDict["score"].relative.score(mate_score=100000))
        return evalDict["score"].relative.score(mate_score=100000)

    if maxPlayer:
        value = -1000
        for child in position.legal_moves:
            value = max(value, minimax(moveToPosition(position, child), depth - 1, False))
        return value
    else:
        value = 1000
        for child in position.legal_moves:
            value = min(value, minimax(moveToPosition(position, child), depth - 1, True))
        return value


print(minimax(board, 2, True))
print("finished")