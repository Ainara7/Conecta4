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


"""
    metodo para contar
def count (state):

   #Saber el momento de la partida
   if ((state.utility != 0) and (state.to_move == "X")):
       return state.utility
   elif ((state.utility != 0) and (state.to_move == "O")):
       return -state.utility

   c = 0
   # recorres el tablero
   for x in range(1, 7):
       for y in range(1, 6):
           if (state.board.get((x, y)) == "O"): #pos donde ha movido el jugador
               c+=1 #cuentas

   return c

"""

"""

    heuristica 1

def newHeuristic(state):

    if state.utility != 0 and state.to_move == 'X':
        return state.utility

    legal_moves = [(x, y) for (x, y) in state.moves if y == 1 or (x, y-1) in state.board]

    h = 0
    for i in legal_moves:
        h += consecutiveChips(state.board, i, state.to_move, (0, 1))
        #h += consecutiveChips(state.board, i, state.to_move, (1, 0))
        #h += consecutiveChips(state.board, i, state.to_move, (1, 1))
        #h += consecutiveChips(state.board, i, state.to_move, (1, -1))
    #print h
    return h

def consecutiveChips(board, move, player, (delta_x, delta_y)):
    x, y = move
    n = 0

    for x in range(1, 6):
        for y in range(1, 7):
            if board.get((x, y)) == player:
                n += 1
                x, y = x + delta_x, y + delta_y
        x, y = move

    print (n, ' hola')
    return n

"""

"""

    heuristica 2
def newHeuristic(state):

    if state.utility != 0 and state.to_move == 'X':
        return state.utility

    legal_moves = [(x, y) for (x, y) in state.moves if y == 1 or (x, y-1) in state.board]

    h = 0
    for i in legal_moves:
        h += values(state.board, i, state.to_move)

    return h

def values(board, move, player):
    x, y = move
    c = 0

    while(board.get(x, y) == player):
        if x == 4 and y == 4: #ideal pq es el centro
            c +=100
        elif x == y: #diagonal que empieza en 1.1
            c +=25
        elif x == 7 or y == 6: #diagonales que empiezan en 6 o 7
            c +=25
        elif x == 3:
            c +=15
        elif x < 3 and x > 1:
            c +=10
        elif y == 3:
            c +=15
        elif y == 5:
            c +=25
        elif y > 1 and y < 3:
            c +=10

    return c

"""

def newHeuristic(state):
    h = 0
    for column in range(1,8):
        for row in range(1,7):
            if state.board.get(column, row):
                for element in range(1,4):
                    if state.to_move == 'O':
                        h+=10
    print h
    return h