import random


def heuristic(state):

    if state.utility != 0:
        return 10000 * state.utility

    legal_moves = [(x, y) for (x, y) in state.moves if y==1 or (x, y-1) in state.board]

    heu = 0
    for i in legal_moves:
        heu += Nconsecutivos(state.board, i, state.to_move, (0, 1))
        heu += Nconsecutivos(state.board, i, state.to_move, (1, 0))
        heu += Nconsecutivos(state.board, i, state.to_move, (1, 1))
        heu += Nconsecutivos(state.board, i, state.to_move, (1, -1))
    print heu
    return heu

def Nconsecutivos(board, move, player, (delta_x, delta_y)):

    #x, y = move
    y, x = move
    y = y - 1

    if y >= 6:
        y = 6
    if y <= 0:
        y = 1

    n = 0



    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y

    #x, y = move
    y, x = move
    y = y - 1

    if y >= 6:
        y = 6
    if y <= 0:
        y = 1

    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y


    if(n > 0):
        n -= 1

    return n
