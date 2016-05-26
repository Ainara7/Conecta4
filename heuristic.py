import games
import random


def randomHeuristic (state, player):
   # player = games.ConnectFour().to_move(state)

   if games.ConnectFour().utility(state, player) == 1:
       return 100
   elif games.ConnectFour().utility(state, player) == -1:
       return -100
   else:
       return random.randint(1, 99)

def newHeuristic(state, player):
    #Si uno de los jugadores va a ganar, devuelve un valor muy grande
    if state.utility != 0:
        print 1000 * state.utility
        return 1000 * state.utility


    legal_moves = [(x, y) for (x, y) in state.moves if y == 1 or (x, y-1) in state.board]

    h = 0
    for i in legal_moves:
        h += consecutiveChips(state.board, i, player, (0, 1))
        h += consecutiveChips(state.board, i, player, (1, 0))
        h += consecutiveChips(state.board, i, player, (1, 1))
        h += consecutiveChips(state.board, i, player, (1, -1))
    print h
    return h

def consecutiveChips(board, move, player, (delta_x, delta_y)):

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
