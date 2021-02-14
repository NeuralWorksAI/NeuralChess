import chess
import chess.engine

board = chess.Board()


def minimax(node, depth, maxPlayer):
    if depth = 0 or #terminal node:
        return #herusitic value of node
    if maximisingPlayer:
        value = -1000
        for child in node.legal_moves:
            value = max(value, minimax(child, depth - 1, False))
        return value
    else:
        value = 1000
        for child in node.legal_moves:
            value = min(value, minimax(child, depth, depth - 1, True))