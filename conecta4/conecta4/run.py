import games
import heuristic

#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial

entrada = raw_input("Elige quien empieza- 0: Maquina y 1: Jugador- ")
respuesta = int(str(entrada).strip())

if(respuesta == 0):
    player = 'O'
else:
    player = 'X'


nivel = raw_input("Selecciona el nivel: 1 Facil, 2 Medio, 3 Dificil- ")
profundidad = int(str(nivel).strip())

while True:
   print "Jugador a mover:", game.to_move(state)
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
       #move = games.minimax_decision(state, game)
       #move = games.alphabeta_full_search(state, game)
       # if profundidad == 1:
       #     move = games.alphabeta_search(state, game, d=1, eval_fn=heuristic.randomHeuristic)
       # else:
       move = games.alphabeta_search(state, game, d=profundidad, eval_fn=heuristic.newHeuristic)

       state = game.make_move(move, state)
       player = 'O'
   print "-------------------"
   if game.terminal_test(state):
       game.display(state)
       print "Final de la partida"
       break