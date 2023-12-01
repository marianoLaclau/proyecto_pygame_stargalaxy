### proyecto_pygame_stargalaxy


## Juego creado con la libreria PyGame de Python 

&nbsp;
# ***Descripcion general del proyecto***


&nbsp;
## **Guia del documento:**

* Descricpion general del juego
* Funcionalidad del juego
* Imagenes
* Observaciones


&nbsp;
### **Descripcion general del juego** 

Este proyecto de juego realizado con la libreria PyGame de Python , esta inspirado en clasico "Galaxian".
El juego esta compuesto por varios elementos interactivos :

Nave espacial, representa al jugador unico .
Naves enemigas , representadas por 3 tipos .
Disparos , efectuados por el jugador y por una de las naves enemigas llamada Super Nave.
Explosiones , tanto en la nave del jugador como en las enemigas al recibir disparos , como la super. explosion al ser eliminado el jugador o la Super nave enemiga .

El juego consiste en derribar la Super nave enemiga , disparando y acertando los disparos laser varias veces , pero tambien tratando de esquivar las naves enemigas que se mueven por la pantalla tratando de colisionar la nave del jugador , para efectuar daño y restar un punto de vida . Es importante que al recibir un disparo de la Super Nave enemiga nos restara 3 puntos de vida .
El juego inicia con 5 vidas para el jugador , si se nos acaban , tanto como si vencemos a la Super nave , nos llevara a los menus o pantallas de Game Over o Winner respectivamente , con la posibilidad de volver a jugar o salir del juego .

La construccion de este proyecto no incluye la programacion orientada a objetos , por ende tampoco la creacion de clases . Por lo que si bien el codigo no resulta muy complejo , se puede observar su notable extension , pero a modo de practicar y comprender en profundidad el funcionamiento y logica de esta libreria , ha resultado muy valioso . Y los resultados son muy acordes a lo esperado antes de iniciar con este camino. 


&nbsp;
### **Funcionalidad del juego**

El elemento principal del juego , que esta representado por la Nave espacial , tiene un desplazamiento libre por toda la pantalla , segun lo indique el jugador mediante las teclas up,down,left y right del teclado . Tambien incluye la accion de disparar laseres , presionando la tecla space.

Las naves enemigas se dividen en dos : la primera es la Super nave enemiga , que se desplaza sobre la parte superior de la pantalla, solo de forma horizontal , y mediante la implementacion de un timer dispara sus misiles cada 3 segundos .
Y las degundas naves enemigas, son dos subtipos de nave , con desplazamientos distintos por toda la pantalla , pero su unica funcionalidad es colisionar con la nave del jugador y restar puntos de vida  para agregar dificultad.

El juego finaliza cuando las vidas del jugador o la vida de la Super nave llegan a 0 , se controlan mediante condicionales , y en ambos casos , segun cual suceda primero se lanzan los menus o pantallas de Winner o Game Over respectivamente , dando la posibilidad de jugar nuevamente o salir del juego mediante las teclas 's' o 'n'. 


&nbsp;
### **Imagenes**


&nbsp;
### **Observaciones**

En una futura actualizacion sera necesario agregar el manejo de excepciones , para evitar que el juego se cierre por excepciones lanzadas que resultan irrelevantes para el correcto funcionamiento juego.

Todas las imagenes y sonidos utilizados en el proyecto fueron obtenidas de sitios web gratuitos .
