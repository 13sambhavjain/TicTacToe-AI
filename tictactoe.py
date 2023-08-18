"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
X = "X"
O = "O"
EMPTY = None
startP = X


def otherP(p):
    if p == X:
        return O
    elif p == O:
        return X
    return None

    raise NotImplementedError

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for r in board:
        x += r.count(X)
        o += r.count(O)

    if x < o:
        return X
    # elif o < x:
    return O
    # else:
    #     return otherP(startP)

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i, j))
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    b1 = deepcopy(board)
    if b1[i][j] != None:
        raise Exception
    b1[i][j] = player(board)
    return b1
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[1][1] != None:
        if (board[1][1] == board[0][0] == board[2][2] or
            board[1][1] == board[0][2] == board[2][0] or
            board[1][1] == board[0][1] == board[2][1] or
            board[1][1] == board[1][0] == board[1][2]):
            return board[1][1]
    if board[0][0] != None:
        if (board[0][0] == board[0][1] == board[0][2] or
            board[0][0] == board[1][0] == board[2][0]):
            return board[0][0]
    if board[2][2] != None:
        if (board[2][0] == board[2][1] == board[2][2] or
            board[0][2] == board[1][2] == board[2][2]):
            return board[2][2]

    return None


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return False
    return True


    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def Max(board):
        if terminal(board):
            return (utility(board), ())
        max_u = -2
        max_a = ()
        for a in actions(board):
            n = Min(result(board, a))
            if n[0] > max_u:
                max_u = n[0]
                max_a = a
        return (max_u, max_a)
        raise NotImplementedError

    def Min(board):
        if terminal(board):
            return (utility(board), ())
        min_u = 2
        min_a = ()
        for a in actions(board):
            n = Max(result(board, a))
            if n[0] < min_u:
                min_u = n[0]
                min_a = a
        return (min_u, min_a)
        raise NotImplementedError

    if terminal(board):
        return None
    # p = player(board)
    if player(board) == X:
        return Max(board)[1]
    else:
        return Min(board)[1]
    raise NotImplementedError

