import games
import heuristic


#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()


"""while True:

   ficha = raw_input("Elija ficha X o O:")

       if ficha=="X" or ficha=="O":
           break
       else:
           print "Por favor, introduzca la ficha"

player=ficha

level = None
while level == None or (level > 0 and level <= 3):
   print "Seleccione la dificultad: "
   print "1 para el nivel facil"
   print "2 para el nivel medio"
   print "3 para el nivel dificil"
   l = raw_input("Nivel: ")
   level = int(l)"""

state = game.initial
player = 'X'

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
       move = games.alphabeta_search(state, game, eval_fn=heuristic.newHeuristic)
       #print heuristic.consecutiveChips(state.board, move , state.to_move, (1,1))
       state = game.make_move(move, state)
       player = 'O'
   print "-------------------"
   if game.terminal_test(state):
       game.display(state)
       print "Final de la partida"
       break