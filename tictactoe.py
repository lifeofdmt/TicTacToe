"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

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
    plays = [0,0] # Each element correspond to the number of X and Y plays respectively

    for row in range(len(board)):
        plays[0] += board[row].count(X) # Count up total number of X's
        plays[1] += board[row].count(O) # Count up total number of 0's
    
    if plays[0] == plays[1]:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    for height in range(len(board)):
        for width in range(len(board)):
            if board[height][width] == EMPTY:
                point = (height,width)
                actions.append(point)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    value = copy.deepcopy(board)
    if not action in actions(value):
        raise Exception("Invalid Action")
    value[action[0]][action[1]] = player(value)
    return value


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for height in range(len(board)):
        x = [1,1]
        o = [1,1]

        for width in range(len(board)-1):
            # Check for horizontal win
            if board[height][width] == X and board[height][width + 1] == X:
                x[0] += 1
            elif board[height][width] == O and board[height][width + 1] == O:
                o[0] += 1

            # Check for vertical win
            if board[width][height] == X and board[width + 1][height] == X:
                x[1] += 1
            elif board[width][height] == O and board[width + 1][height] == O:
                o[1] += 1

        if x[0] == 3 or x[1] == 3:
            return X
        elif o[0] == 3 or o[1] == 3:
            return O

    # Check for a diagonal win
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board)!= None:
        return True

    x = 0
    for height in range(len(board)):
        for width in range(len(board)):
            if board[height][width] == EMPTY:
                x += 1
    if x == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def MIN_VALUE(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v,MAX_VALUE(result(board,action)))
    return v

def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v,MIN_VALUE(result(board,action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    actionss = actions(board)
    index = 0

    if player(board) == X:
        values = [MIN_VALUE(result(board,actionss[action])) for action in range(len(actionss))]

        max_val = values[0]
        for i in range(len(values)):
            if values[i] > max_val:
                max_val = values[i]
                index = i
    else:
        values = [MAX_VALUE(result(board,actionss[action])) for action in range(len(actionss))]

        min_val = values[0]

        for i in range(len(values)):
            if values[i] < min_val:
                min_val = values[i]
                index = i
    return actionss[index]