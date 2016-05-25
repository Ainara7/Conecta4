import games
import heuristic


def machineVsMachine(state, player):
    while True:
        print "Jugador a mover:", player
        game.display(state)
        if player == 'O':
            print "Thinking..."
            if profundidad == 1:
                move = games.alphabeta_search(state, game, d=1, eval_fn=heuristic.randomHeuristic)
            else:
                move = games.alphabeta_search(state, game, d=profundidad, eval_fn=heuristic.newHeuristic)

            state = game.make_move(move, state)
            player = 'X'
            print "-------------------"
        else:
            print "Thinking..."
            if profundidad == 1:
                move = games.alphabeta_search(state, game, d=1, eval_fn=heuristic.randomHeuristic)
            else:
                move = games.alphabeta_search(state, game, d=profundidad, eval_fn=heuristic.newHeuristic)

            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break


def playerVsMachine(state, player):
    while True:
        print "Jugador a mover:", player
        game.display(state)

        if player == 'X':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'O'
        else:
            print "Thinking..."
            if profundidad == 1:
                move = games.alphabeta_search(state, game, d=1, eval_fn=heuristic.randomHeuristic)
            else:
                move = games.alphabeta_search(state, game, d=profundidad, eval_fn=heuristic.newHeuristic)

            state = game.make_move(move, state)
            player = 'X'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break


def machineVSPlayer(state, player):
    while True:
        print "Jugador a mover:", player
        game.display(state)

        if player == 'O':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "Thinking..."
            if profundidad == 1:
                move = games.alphabeta_search(state, game, d=1, eval_fn=heuristic.randomHeuristic)
            else:
                move = games.alphabeta_search(state, game, d=profundidad, eval_fn=heuristic.newHeuristic)

            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

# TODO implementar entero
def playerVSPlayer(state, player):
    while True:
        print "Jugador a mover:", player
        game.display(state)

        if player == 'O':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "Thinking..."
            if profundidad == 1:
                move = games.alphabeta_search(state, game, d=1, eval_fn=heuristic.randomHeuristic)
            else:
                move = games.alphabeta_search(state, game, d=profundidad, eval_fn=heuristic.newHeuristic)

            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

game = games.ConnectFour()
state = game.initial

entrada = raw_input("Elige Modo de juego- 0: Jugador vs Jugador || 1: Jugador vs Maquina || 2: Maquina vs Maquina- ")
gamemode = int(str(entrada).strip())

entrada = raw_input("Elige quien empieza- 0: Jugador y 1: Maquina- ")
respuesta = int(str(entrada).strip())
if(respuesta == 0):
    player = 'O'
else:
    player = 'X'

nivel = raw_input("Selecciona el nivel: 1 Facil, 2 Medio, 3 Dificil 4 DESAFIO- ")
profundidad = int(str(nivel).strip())

if (gamemode == 0):
    playerVSPlayer(state, player)
elif (gamemode == 1 and respuesta == 0):
    playerVsMachine(state, player)
elif (gamemode == 1 and respuesta == 1):
    machineVSPlayer(state, player)
elif (gamemode == 2):
    machineVsMachine(state, player)
