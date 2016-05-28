En cuanto a la clase heuristic.py elaboramos los siguientes métodos:

	-En primer lugar, ideamos una heurística aleatoria a la que le pasamos el estado y el jugador, de esta forma, si el estado del jugador es ganador, devolverá 100, 
	y en caso de ser perdedor, devolverá -100, siendo un valor aleatorio recogido entre 1 y 99 para el caso en el que empate. 

	-En segundo lugar, ideamos una heurística que mire las posiciones colindantes a la posición dónde el jugador mueve ficha, de tal forma que, pueda predecir su
	su posterior movimiento. A este método llamado consecutiveChips, cuyo objetivo es ver cuáles son las fichas consecutivas que existen desde de la posición 
	dónde el jugador mueve, le pasamos el tablero, el movimiento (ejes que componen el tablero (y,x)), el jugador, y por último, los valores que nos permitan 
	movernos a partir de la posición de la ficha, dónde el jugador movió.
	Posteriormente, llamamos a este método, en newHeuristic, pasando el estado y el jugador. Este método se encarga de comprobar si uno de los jugadores
	va a ganar, para en ese caso, devolver un valor muy grande. Después, mira cuáles son los movimientos legales, e itera sobre ellos, para ir acumulando
	los valores de un estado del tablero que deriven de la función anteriormente citada (consecutiveChips). A esta se le pasa el tablero, 
	las iteraciones de los movimientos legales, el jugador y los valores para mirar las posiciones colindantes a la ficha que coloque el jugador.

Además, en la clase run.py creamos unos modos de juego para realizar lo que el enunciado nos pedía, los modos de juego de los cuáles disponemos son:
máquina contra máquina, jugador contra máquina y jugador contra jugador. De esta forma, el jugador podrá elegir contra quién desea jugar. Asimismo, cabe mencionar
que en el modo de juego máquina contra máquina, el comportamiento que esperaríamos que resultara, no actúa tal y como debería, ya que tendría que empatar o al 
menos rellenar el tablero. No obstante, esto sólo ocurre en ese modo de juego, siendo así, que en el resto de modos de juegos si siguen el comportamiento esperado.  
Además, le damos la posibilidad de elegir si desea jugar primero o no. Asimismo, hemos establecido los niveles de dificultad que el jugador podrá elegir, tales cómo, 
el nivel fácil, medio, difícil o el de desafío. Así pues, establecimos el nivel fácil con la heurística random, implementando el resto de niveles con la 
nueva heurística incrementando la profundidad, en función del nivel del que se trate. Por ejemplo, para el nivel medio la profundida es de 2, para el nivel 
difícil es profundidad 3 y por último, para el nivel desafío correpondería a profundidad 4. En este último caso, se verá como se tarda más en el tiempo de ejecutar
el juego, esto podríamos haberlo solucionado usando el patrón memorize, pero no nos dio tiempo.
