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
    x = 0
    o = 0
    for row in board:
        x += row.count(X)
        o += row.count(O)

    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    new_board = copy.deepcopy(board)
    
    current_player = player(board)
    
    new_board[action[0]][action[1]] = current_player
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_to_move = player(board)

    if player_to_move == X:
        _, move = max_value(board)
    else:
        _, move = min_value(board)

    return move


def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    optimal_move = None

    for action in actions(board):
        new_board = result(board, action)
        min_val, _ = min_value(new_board)
        if min_val > v:
            v = min_val
            optimal_move = action

    return v, optimal_move


def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    optimal_move = None

    for action in actions(board):
        new_board = result(board, action)
        max_val, _ = max_value(new_board)
        if max_val < v:
            v = max_val
            optimal_move = action

    return v, optimal_move
