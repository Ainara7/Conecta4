En cuanto a la clase heuristic.py elaboramos los siguientes m�todos:

	-En primer lugar, ideamos una heur�stica aleatoria a la que le pasamos el estado y el jugador, de esta forma, si el estado del jugador es ganador, devolver� 100, 
	y en caso de ser perdedor, devolver� -100, siendo un valor aleatorio recogido entre 1 y 99 para el caso en el que empate. 

	-En segundo lugar, ideamos una heur�stica que mire las posiciones colindantes a la posici�n d�nde el jugador mueve ficha, de tal forma que, pueda predecir su
	su posterior movimiento. A este m�todo llamado consecutiveChips, cuyo objetivo es ver cu�les son las fichas consecutivas que existen desde de la posici�n 
	d�nde el jugador mueve, le pasamos el tablero, el movimiento (ejes que componen el tablero (y,x)), el jugador, y por �ltimo, los valores que nos permitan 
	movernos a partir de la posici�n de la ficha, d�nde el jugador movi�.
	Posteriormente, llamamos a este m�todo, en newHeuristic, pasando el estado y el jugador. Este m�todo se encarga de comprobar si uno de los jugadores
	va a ganar, para en ese caso, devolver un valor muy grande. Despu�s, mira cu�les son los movimientos legales, e itera sobre ellos, para ir acumulando
	los valores de un estado del tablero que deriven de la funci�n anteriormente citada (consecutiveChips). A esta se le pasa el tablero, 
	las iteraciones de los movimientos legales, el jugador y los valores para mirar las posiciones colindantes a la ficha que coloque el jugador.

Adem�s, en la clase run.py creamos unos modos de juego para realizar lo que el enunciado nos ped�a, los modos de juego de los cu�les disponemos son:
m�quina contra m�quina, jugador contra m�quina y jugador contra jugador. De esta forma, el jugador podr� elegir contra qui�n desea jugar. Asimismo, cabe mencionar
que en el modo de juego m�quina contra m�quina, el comportamiento que esperar�amos que resultara, no act�a tal y como deber�a, ya que tendr�a que empatar o al 
menos rellenar el tablero. No obstante, esto s�lo ocurre en ese modo de juego, siendo as�, que en el resto de modos de juegos si siguen el comportamiento esperado.  
Adem�s, le damos la posibilidad de elegir si desea jugar primero o no. Asimismo, hemos establecido los niveles de dificultad que el jugador podr� elegir, tales c�mo, 
el nivel f�cil, medio, dif�cil o el de desaf�o. As� pues, establecimos el nivel f�cil con la heur�stica random, implementando el resto de niveles con la 
nueva heur�stica incrementando la profundidad, en funci�n del nivel del que se trate. Por ejemplo, para el nivel medio la profundida es de 2, para el nivel 
dif�cil es profundidad 3 y por �ltimo, para el nivel desaf�o correponder�a a profundidad 4. En este �ltimo caso, se ver� como se tarda m�s en el tiempo de ejecutar
el juego, esto podr�amos haberlo solucionado usando el patr�n memorize, pero no nos dio tiempo.
