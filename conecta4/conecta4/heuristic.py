import games
import random


def randomHeuristic (state):
   player = games.ConnectFour().to_move(state)

   if games.ConnectFour().utility(state, player) == 1:
       return 100
   elif games.ConnectFour().utility(state, player) == -1:
       return -100
   else:
       return random.randint(1, 99)

def newHeuristic(state):

    if state.utility != 0:
        return 1000 * state.utility

    legal_moves = [(x, y) for (x, y) in state.moves if y == 1 or (x, y-1) in state.board]
    h = 0
    # TODO MEMOIZE
    for i in legal_moves:
        h += consecutiveChips(state.board, i, state.to_move, (0, 1))
        h += consecutiveChips(state.board, i, state.to_move, (1, 0))
        h += consecutiveChips(state.board, i, state.to_move, (1, 1))
        h += consecutiveChips(state.board, i, state.to_move, (1, -1))
    # print h
    return h

def consecutiveChips(board, move, player, (delta_x, delta_y)):
    x, y = move
    n = 0

    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y

    y, x = move

    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y

    return n


