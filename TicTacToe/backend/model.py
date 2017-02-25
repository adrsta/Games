import numpy as np


EMPTY = ' '
NOONE = ' '
PLAYER1 = 'X'
PLAYER2 = 'O'
DRAW = '='

class State:
    def __init__(self, player=PLAYER1):
        self.player = player
        self.cursor = (1, 1)
        self.matrix = [[EMPTY, EMPTY, EMPTY],
                       [EMPTY, EMPTY, EMPTY],
                       [EMPTY, EMPTY, EMPTY]]

def move_cursor(pos, vec):
    pos = np.array(pos)
    vec = np.array(vec)
    new_pos = pos + vec
    if new_pos[0] >= 0 and new_pos[0] <= 2:
        if new_pos[1] >= 0 and new_pos[1] <= 2:
            return tuple(new_pos)
    return tuple(pos)

def opponent(player):
        if player == PLAYER1:
            return PLAYER2
        else:
            return PLAYER1

def mark_spot(matrix, player, cursor):
    x = cursor[0]
    y = cursor[1]
    if matrix[x][y] == EMPTY:
        matrix[x][y] = player
        player = opponent(player)
    return (matrix, player)

def check_winner(matrix):
    # horizontals
    for row in range(3):
        if matrix[row][0] == matrix[row][1]:
            if matrix[row][1] == matrix[row][2]:
                if matrix[row][0] != NOONE:
                    return matrix[row][0]
    # verticals
    for col in range(3):
        if matrix[0][col] == matrix[1][col]:
            if matrix[1][col] == matrix[2][col]:
                if matrix[0][col] != NOONE:
                    return matrix[0][col]
    # diagonals
    if matrix[0][0] == matrix[1][1]:
        if matrix[1][1] == matrix[2][2]:
            if matrix[1][1] != NOONE:
                return matrix[1][1]
    if matrix[2][0] == matrix[1][1]:
        if matrix[1][1] == matrix[0][2]:
            if matrix[1][1] != NOONE:
                return matrix[1][1]
    # draw
    num_marks = 0
    for row in range(3):
        for col in range(3):
            mark = matrix[row][col]
            if mark == PLAYER1 or mark == PLAYER2:
                num_marks += 1
    if num_marks == 9:
        return DRAW
    # still playing
    return NOONE
