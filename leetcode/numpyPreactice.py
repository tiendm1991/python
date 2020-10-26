import random
import numpy as np
import matplotlib.pyplot as plt


def create_board():
    return np.zeros((3, 3), dtype=int)


def possible(board):
    idx = np.where(board == 0)
    return [(idx[0][i], idx[1][i]) for i in range(len(idx[0]))]


def row_win(board, player):
    return np.any([np.all(x == player) for x in board])


def col_win(board, player):
    return row_win(np.transpose(board), player)


def diag_win(board, player):
    check = True
    for i in range(len(board)):
        if board[i][i] != player:
            check = False
            break
    if check:
        return True
    check = True
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] != player:
            check = False
            break
    return check


def random_place(board, player):
    selection = possible(board)
    choice = random.choice(selection)
    board[choice[0]][choice[1]] = player


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            break
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
    board = create_board()

    def play(board, player):
        random_place(board, player)
        w = evaluate(board)
        if w != 0:
            return w
        return play(board, 3 - player)

    return play(board, 1)


def play_strategic_game():
    board = create_board()

    def play(board, player):
        random_place(board, player)
        w = evaluate(board)
        if w != 0:
            return w
        return play(board, 3 - player)

    board[1][1] = 1
    return play(board, 2)


random.seed(1)
results = []
for i in range(1000):
    results.append(play_strategic_game())
print(results.count(1))
