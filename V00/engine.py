import chess
import chess.engine
import time

start_time = time.time()
#r1bq1rkR/1ppnbpp1/p3p3/4P3/4BB2/4P3/PPP2PP1/RN1QK3 w Qq - 1 1
board = chess.Board("rnbqkbnr/2pp1ppp/pp6/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 1")

engine = chess.engine.SimpleEngine.popen_uci("/home/qqze/Documents/NeuralWorks/NeuralChess/NeuralChess/V00/stockfish_20090216_x64_bmi2")


#position = [board, evaluation]
def moveToPosition(board, move):
    childBoard = board.copy()
    childBoard.push_san(str(move))
    return childBoard

def minimax(node, depth, alpha, beta, maxPlayer):

    if depth == 0 or node.is_game_over():
        evalDict = engine.analyse(node, chess.engine.Limit(depth=0))
        return None, evalDict["score"].relative.score(mate_score=1000000)

    if maxPlayer:
        max_eval = -1000000
        for child in node.legal_moves:
            eval = minimax(moveToPosition(node, child), depth - 1, alpha, beta, False)[1]
            if eval > max_eval:
                max_eval = eval
                best_move = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return best_move, max_eval

    else:
        min_eval = 1000000
        for child in node.legal_moves:
            eval = minimax(moveToPosition(node, child), depth - 1, alpha, beta, True)[1]
            if eval < min_eval:
                min_eval = eval
                best_move = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_move, min_eval


best_move, best_eval = minimax(board, 4, -1000000, 1000000, True)
print(f"best move: {best_move}, eval: {best_eval/100}")
print(f"finished in {time.time() - start_time} seconds")
board.push(best_move)
print(board)