import pygame , random ,time
pygame.init()


#Definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#Incluimos la sentencias necesarias para poder mostrar textos en la ventana (score , vidas)
pygame.font.init()
fuente = pygame.font.Font(None, 36)  #Ajustar el tamaño de la fuente 
color_texto = (WHITE)  # Color del texto 




size = (1000,600) #Definimos el tamaño de la ventana de juego en una variable
ventana = pygame.display.set_mode(size) #Creamos la ventana usando la variable size para determinar el tamaño
pygame.display.set_caption("Star Galaxy") #Definimos un titulo para la ventana de juego
reloj = pygame.time.Clock() #Controlar FPS
temporizador_game_over = None #Servira para retrasar la aparicion de las pantallas finales unos segundos



#Importamos imagenes------------------------------------------------------------------------------------------------------------------------------------------------
#Backgraounds
background_principal = pygame.image.load(".\PyGame\img\zackground_principal.jpg").convert()
background_principal = pygame.transform.scale(background_principal, (1000, 600))#Redimensionar imagen

#Nave Jugador
player_1 = pygame.image.load(".\PyGame\img\znave_1_player.png").convert()
player_1 = pygame.transform.scale(player_1,(70,90))#Redimensionar imagen
player_1.set_colorkey(BLACK) #Quita el contorno negro

#Propulsores(varias imagenes para crear efecto)
nombres_archivos = [".\PyGame\img\propulsores.png",".\PyGame\img\propulsores2.png",".\PyGame\img\propulsores3.png"]
imagenes = [pygame.image.load(nombre_archivo) for nombre_archivo in nombres_archivos]
indice_imagen = 0
#Redimensionamos y quitamos contorno negro individualmente 
imagenes[0] = pygame.transform.scale(imagenes[0], (30, 40))
imagenes[0].set_colorkey(BLACK)

imagenes[1] = pygame.transform.scale(imagenes[1], (30, 40))
imagenes[1].set_colorkey(BLACK)

imagenes[2] = pygame.transform.scale(imagenes[2], (30, 40))
imagenes[2].set_colorkey(BLACK)


#Disparo laser nave espacial
imagen_laser = pygame.image.load(".\PyGame\img\zlasernave.png").convert()
imagen_laser = pygame.transform.scale(imagen_laser,(10,20))#Redimensionar imagen
imagen_laser.set_colorkey(BLACK) #Quita el contorno negro
explosion_laser =  pygame.image.load(".\PyGame\img\zexplosionlaser.png").convert()
explosion_laser = pygame.transform.scale(explosion_laser,(50,50))#Redimensionar imagen
explosion_laser.set_colorkey(BLACK)


#Nave enemigo
enemigo =  pygame.image.load(".\PyGame\img\zenemigo.png").convert()
enemigo = pygame.transform.scale(enemigo,(50,50))#Redimensionar imagen
enemigo.set_colorkey(BLACK) #Quita el contorno negro

#Nave enemigo 2
enemigo2 =  pygame.image.load(".\PyGame\img\zenemigo2.png").convert()
enemigo2 = pygame.transform.scale(enemigo2,(50,50))#Redimensionar imagen
enemigo2.set_colorkey(BLACK) #Quita el contorno negro

#Nave Superenemigo
super_enemigo =  pygame.image.load(".\PyGame\img\zsuperenemigo.png").convert()
super_enemigo = pygame.transform.scale(super_enemigo,(200,200))#Redimensionar imagen
super_enemigo.set_colorkey(BLACK) #Quita el contorno negro

#Misil Superenemigo
super_misil =  pygame.image.load(".\PyGame\img\zlaserenemigo.png").convert()
super_misil = pygame.transform.scale(super_misil,(20,40))#Redimensionar imagen
super_misil.set_colorkey(BLACK) #Quita el contorno negro
explosion_misil = pygame.image.load(".\PyGame\img\zexplosionmisil.png").convert()
explosion_misil = pygame.transform.scale(explosion_misil,(40,80))#Redimensionar imagen
explosion_misil.set_colorkey(BLACK)


#Superxplosion final
super_explosion =  pygame.image.load(".\PyGame\img\zsuperexplosion.png").convert()
super_explosion = pygame.transform.scale(super_explosion,(100,100))#Redimensionar imagen
super_explosion.set_colorkey(BLACK) #Quita el contorno negro

#Pantalla start
start_img =  pygame.image.load(".\PyGame\img\zstart.jpg").convert()
start_img = pygame.transform.scale(start_img,(1000,600))#Redimensionar imagen
start_img.set_colorkey(BLACK) #Quita el contorno negro

#Game over
game_over_img =  pygame.image.load(".\PyGame\img\zgameover.jpg").convert()
game_over_img = pygame.transform.scale(game_over_img,(1000,600))#Redimensionar imagen
  
#Win
win_img =  pygame.image.load(".\PyGame\img\zwin.jpg").convert()
win_img = pygame.transform.scale(win_img,(1000,600))#Redimensionar imagen



#Importamos sonidos ----------------------------------------------------------------------------------------------------------------------------------------
laser_sound = pygame.mixer.Sound(".\PyGame\sounds\zlaser.wav")
misil_sound = pygame.mixer.Sound(".\PyGame\sounds\zmisil.wav")
win_sound = pygame.mixer.Sound(".\PyGame\sounds\zwin.wav")
lost_sound = pygame.mixer.Sound(".\PyGame\sounds\zlost.wav")
impact_sound = pygame.mixer.Sound(".\PyGame\sounds\zimpacto.wav")



#Fijamos coordenadas y velocidad de desplazamiento de los elementos en el juego------------------------------------------------------------------------------------
#Coordenadas player_1 "Nave espacial"
cord_x_navespacial = 400
cord_y_navespacial = 500
#Velocidad a la que se movera el objeto "Nave espacial",dejamos las variables inicializadas en 0 para utilizarlas en el while principal
speed_x_navespacial = 0
speed_y_navespacial = 0

#Coordenadas y velocidad que se desplazara el laser , inicializamos las variables en 0 para poder usarlas dentro del while principal
coord_x_laser = 0
coord_y_laser = 0
speed_y_laser = 0


#Coordenadas "Nave enemigo", en la lista defiimos la cantidad de naves y sus coordenadas que luego seran dibujadas
posiciones_enemigos = [(0, 0), (50, 50), (100, 100),(150,150),(200,200),(250,150),(300,100),(350,50),(400,0)]
#Velocidad a la que se movera el objeto "Nave enemigo"
speed_x_enemigo = 4
speed_y_enemigo = 4

#Coordenadas "Nave enemigo2", en la lista defiimos la cantidad de naves y sus coordenadas que luego seran dibujadas
posiciones_enemigos2 = [(1000, 0), (950, 50), (900, 100),(850,150),(800,200),(750,250),(700,300),(650,350),(600,400),(550,450)]
#Velocidad a la que se movera el objeto "Nave enemigo2"
speed_x_enemigo2 = 4
speed_y_enemigo2 = 4

#Coordenadas  y velocidad nave "Super Enemigo"
cord_x_super = 400
cord_y_super = 0
speed_x_super = 2
tiempo_ultimo_disparo = time.time()


#Estrellas en movimiento, guardamos valores aleatorios en una variable para crear coordenadas
coor_list = []
for i in range(60):  #60 representa la cantidad de "estrellas" que se mostraran en la ventana
    x = random.randint(0,1000)
    y = random.randint(0,600)
    coor_list.append([x,y])


lista_laser = [] #Inicializamos la lista vacia para cargarla dentro del while principal
lista_misil = []
explosiones = []  


#Inicializamos los marcadores
score_player = 0
vida_player1 = 5
vida_enemigo = 3
vida_supernave = 15

start = True
win = False
game_over = False
sounds = True
temporizador = 100

#Funcion explosion Super enemigo final----------------------
def explosion_super():
    global temporizador, win, temporizador_game_over# Incluimos estas variables como globales para poder modificarlas dentro del metodo

    if temporizador > 0:
        ventana.blit(super_explosion, [cord_x_super, 0])
        ventana.blit(super_explosion, [cord_x_super + 100, 0])
        ventana.blit(super_explosion, [cord_x_super + 50, 50])
        win = True
        temporizador -= 1
        temporizador_game_over = pygame.time.get_ticks() #Iniciamos el temporizador
    

#Funcion explosion Nave player1--------------------------
def explosion_player1():
    global temporizador , game_over, temporizador_game_over # Incluimos estas variables como globales para poder modificarlas dentro del metodo

    if temporizador > 0:
        ventana.blit(super_explosion, [cord_x_navespacial, cord_y_navespacial])
        ventana.blit(super_explosion, [cord_x_navespacial + 100, cord_y_navespacial])
        ventana.blit(super_explosion, [cord_x_navespacial + 50, cord_y_navespacial +50])
        game_over = True
        temporizador -= 1
        temporizador_game_over = pygame.time.get_ticks() #Iniciamos el temporizador


#Funcion para normalizar valores iniciales al reiniciar----------------------
def reiniciar_juego():
    global score_player, vida_player1, vida_enemigo, vida_supernave, game_over ,sounds #Incluimos estas variables como globales para poder modificarlas dentro del metodo
    global cord_x_navespacial, cord_y_navespacial, cord_x_super, cord_y_super, speed_x_super
    global posiciones_enemigos, posiciones_enemigos2, speed_x_enemigo, speed_y_enemigo, speed_x_enemigo2, speed_y_enemigo2
    global lista_laser, lista_misil, explosiones

    score_player = 0
    vida_player1 = 5
    vida_enemigo = 3
    vida_supernave = 15
    game_over = False
    sounds = True

    # Restablece las posiciones iniciales
    cord_x_navespacial = 400
    cord_y_navespacial = 500
    cord_x_super = 400
    cord_y_super = 0
    speed_x_super = 2

    # Restablece las posiciones iniciales de las naves enemigas
    posiciones_enemigos = [(0, 0), (50, 50), (100, 100), (150, 150), (200, 200), (250, 150), (300, 100), (350, 50), (400, 0)]
    posiciones_enemigos2 = [(1000, 0), (950, 50), (900, 100), (850, 150), (800, 200), (750, 250), (700, 300), (650, 350), (600, 400), (550, 450)]

    # Restablece las velocidades iniciales de las naves enemigas
    speed_x_enemigo = 4
    speed_y_enemigo = 4
    speed_x_enemigo2 = 4
    speed_y_enemigo2 = 4

    # Limpia las listas y estructuras de datos
    lista_laser = []
    lista_misil = []
    explosiones = []


# Función para verificar colisiones por medio de coincidencias en coordenadas---------------------------------------------
def verificar_colisiones():
    global score_player, vida_player1, vida_enemigo, vida_supernave # Incluimos estas variables como globales para poder modificarlas dentro del metodo
   
    
    rect_nave = player_1.get_rect(topleft=(cord_x_navespacial, cord_y_navespacial))#Actualizamos las coordenadas de nave espacial dentro del metodo para mayo precision
     
    #Colisiones del laser con enemigos -----------------------------------
    for laser in lista_laser:
        #Detectamos las colisones con la Supernave enemiga 
        rect_laser = imagen_laser.get_rect(topleft=laser) #Con get_rect() obtenemos la posicion del laser
        if rect_laser.colliderect(rect_superenemigo): #Con colliderect() verificamos si hay coincidencias
                #Colision detectada , realizar las acciones
                ventana.blit(explosion_laser,[laser[0],laser[1]]) #Agregamos una explosion al acertar el disparo
                score_player += 300
                vida_supernave -= 1
                lista_laser.remove(laser) #Elimina el laser
                 
        
        #Detectamos las colisones con las Naves enemigas 
        for i, (cord_x_enemigo, cord_y_enemigo) in enumerate(posiciones_enemigos):
            #Condiciomaos el laser dentro del rango total de pixels sobre el eje X de la "Nave enemiga"
            if cord_x_enemigo < laser[0] < cord_x_enemigo + 50 and cord_y_enemigo < laser[1] < cord_y_enemigo + 50:
                # Colisión detectada, realizar las acciones
                ventana.blit(explosion_laser,[cord_x_enemigo,cord_y_enemigo]) 
                score_player += 100
                del posiciones_enemigos[i]  # Elimina la nave enemiga
                lista_laser.remove(laser)  # Elimina el láser
                  

        #Detectamos las colisones con las Naves enemigas2 
        for i, (cord_x_enemigo2, cord_y_enemigo2) in enumerate(posiciones_enemigos2):
            #Condiciomaos el laser dentro del rango total de pixels sobre el eje X de la "Nave enemiga"
            if cord_x_enemigo2 < laser[0] < cord_x_enemigo2 + 50 and cord_y_enemigo2 < laser[1] < cord_y_enemigo2 + 50:
                # Colisión detectada, realizar las acciones
                ventana.blit(explosion_laser,[cord_x_enemigo2,cord_y_enemigo2]) 
                score_player += 100
                lista_laser.remove(laser)  # Elimina el láser
                del posiciones_enemigos2[i]  # Elimina la nave enemiga        
                

    
    
    
    #Colisones misil de la Supernave enemiga con Nave espacial  ------------------------ 
    for misil in lista_misil:
        rect_misil = super_misil.get_rect(topleft=misil) #Con get_rect() obtenemos la posicion del misil
        rect_misil.inflate_ip(50, 20) #Redimensioamos el espacio que abarcan los misiles
       
       # Verifica si hay colisión con la nave del jugador
        if rect_misil.colliderect(rect_nave):
            explosiones.append({"pos":misil,"temporizador":10}) #Implementamos un "temporizador" para retrasar la eliminacion de la imagen de efecto
            lista_misil.remove(misil)  # Elimina el misil
            vida_player1 -= 3
            

    
    
    #Colisiones Naves enemigas con Nave espacial -------------------------------
    for i, (cord_x_enemigo, cord_y_enemigo) in enumerate(posiciones_enemigos):
            rect_nave_enemigo = enemigo.get_rect(topleft=(cord_x_enemigo,cord_y_enemigo))
            
            if rect_nave_enemigo.colliderect(rect_nave):
                impact_sound.play() #Agregamos sonido de impacto
                # Colisión detectada, realizar las acciones
                ventana.blit(explosion_laser,[cord_x_enemigo,cord_y_enemigo]) 
                score_player -= 50
                vida_player1 -= 1
                del posiciones_enemigos[i]  # Elimina la nave enemiga

    #Colisiones Naves enemigas2 con Nave espacial 
    for i, (cord_x_enemigo2, cord_y_enemigo2) in enumerate(posiciones_enemigos2):
            rect_nave_enemigo2 = enemigo2.get_rect(topleft=(cord_x_enemigo2,cord_y_enemigo2))
            
            if rect_nave_enemigo2.colliderect(rect_nave):
                impact_sound.play() #Agregamos sonido de impacto
                  # Colisión detectada, realizar las acciones
                ventana.blit(explosion_laser,[cord_x_enemigo2,cord_y_enemigo2]) 
                score_player -= 50
                vida_player1 -= 1
                del posiciones_enemigos2[i]  # Elimina la nave enemiga2





running = True #Condicion del bucle while----------------------------------------------------------------------------------------------------------------------
while running: #Bucle principal del juego
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Necesario para poder cerrar la ventana
            running = False
        
        #Eventos al presionar tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x_navespacial = -4
            if event.key == pygame.K_RIGHT:
                speed_x_navespacial = 4
            if event.key == pygame.K_UP:
                speed_y_navespacial = -4
            if event.key == pygame.K_DOWN:
                speed_y_navespacial = 4    
            if event.key == pygame.K_SPACE:
                lista_laser.append([cord_x_navespacial + 30, cord_y_navespacial + 40])  #Le sumamos pixeles para centrar el laser debajo de la nave
                laser_sound.play() #Iniciamos sonido al disparar
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x_navespacial = 0
            if event.key == pygame.K_RIGHT:
                speed_x_navespacial = 0
            if event.key == pygame.K_UP:
                speed_y_navespacial = 0  
            if event.key == pygame.K_DOWN:
                speed_y_navespacial = 0    
            if event.key==pygame.K_BACKSPACE:
                speed_y_laser = 0



    #Usamos condicionales para escalar las distintas pantallas del juego segun el progreso---------------------          
    if start :
        ventana.blit(start_img,[0,0])
        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Necesario para poder cerrar la ventana
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Tecla Space para iniciar  
                        start = False  # Cambia la condicion a False para que en la siguiente iteracion avance con la siguiente pantalla
                        # Aquí puedes restablecer variables, reiniciar posiciones, etc.
                      
    
    elif win :
        if sounds: #Condicion para que el sonido se reproduzca solo una vez
            win_sound.play()  #Iniciamos efecto de sonido
            sounds = False
        
        tiempo_transcurrido = pygame.time.get_ticks() - temporizador_game_over #Retrasamos la aparicion de la pantalla final 3 segundos
        if tiempo_transcurrido > 3000:
            
            ventana.blit(win_img,[0,0])
            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # S para reiniciar"  
                        win = False  # Cambia la condicion a False para que en la siguiente iteracion avance con la siguiente pantalla
                        # Reestablecemos valores 
                        reiniciar_juego()
                    elif event.key == pygame.K_n:
                         running = False  #Salimos del juego

    elif game_over:
        if sounds:  #Condicion para que el sonido se reproduzca solo una vez 
            lost_sound.play() #Iniciamos efecto de sonido
            sounds = False
        
        tiempo_transcurrido = pygame.time.get_ticks() - temporizador_game_over #Retrasamos la aparicion de la pantalla final 3 segundos
        if tiempo_transcurrido > 3000:
            ventana.blit(game_over_img,[0,0])
            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # S para reiniciar   
                        game_over = False   # Cambia la condicion a False para que en la siguiente iteracion avance con la siguiente pantalla
                        #Reestablevemos valores.
                        reiniciar_juego()
                    elif event.key == pygame.K_n:
                        running = False
    else:
        
        #Cargamos imagen de fondo primero para que no se superponga con demas elemntos
        ventana.blit(background_principal,[0,0]) 
        
        #Agregamos el Score y las vidas en la pantalla
        texto_puntaje = fuente.render(f"SCORE: {score_player}", True, color_texto)
        ventana.blit(texto_puntaje, (50, 10))  # Ajusta las coordenadas según la posición deseada
        
        texto_vidas = fuente.render(f"VIDAS: {vida_player1}",True,color_texto)
        ventana.blit(texto_vidas, (850, 10))  # Ajusta las coordenadas según la posición deseada
        
        
        verificar_colisiones()  #Invocamos el metodo para chequear colisiones por cada iteracion
        
    
        #Parte interactiva o logica del juego------------------------------------------------------------------------------------------------------------------

        #Estrellas en movimiento, damos valores al eje Y para generar el movimiento
        for coord in coor_list:
            x = coord[0]
            y =  coord[1]
            estrellas = pygame.draw.circle(ventana,WHITE,(x,y),2)#Creamos los elemntos segun cantidad de cordenadas almacenadas en "coor_list"
            coord[1] += 4
            
            if coord[1] > 600 : #Condicional para que el efecto sea infinito
                coord[1] = 0
    
    
    
    #Condicon para que el elemento "Nave espacial" , "Nave enemigo" y "Super nave enemiga" no salga de la pantalla
        if cord_x_navespacial > 930 or cord_x_navespacial < 0:
            speed_x_navespacial *= -1
        
        if cord_y_navespacial > 510 or cord_y_navespacial <0:
             speed_y_navespacial *= -1

        if cord_x_super > 650 or cord_x_super < 250:
            speed_x_super *= -1
    
        
        #Aplicamos la animacion de movimiento a "Nave espacial" seguna las teclas presionadas
        cord_x_navespacial += speed_x_navespacial  
        cord_y_navespacial += speed_y_navespacial

        #Definimos el desplazamiento de la nave "Super enemigo"
        cord_x_super += speed_x_super

        
        #Disparo de la Súper nave enemiga cada 3 segundos
        if time.time() - tiempo_ultimo_disparo > 3:
            lista_misil.append([cord_x_super + 95, cord_y_super + 200])
            misil_sound.play()
            tiempo_ultimo_disparo = time.time()
        
        
        #Definimos la posicion del "laser" ligada con la "Nave espacial"
        coord_x_laser += cord_x_navespacial
        coord_y_laser += speed_y_laser
        
        #Guardamos y actualizamos los nuevos valores de "Nave enemiga" para que en cada iteracion se actualice y genere efecto movimiento
        for i in range(len(posiciones_enemigos)):
            cord_x_enemigo, cord_y_enemigo = posiciones_enemigos[i]
            cord_x_enemigo += speed_x_enemigo
            cord_y_enemigo += speed_y_enemigo
            posiciones_enemigos[i] = (cord_x_enemigo, cord_y_enemigo)
        
        #Condicion para que las naves enemigas no desborden de la ventana,usando de referencia la ubicacion del ultimo elemnto posicionado
        if cord_x_enemigo > 1040 or cord_x_enemigo < 300:
                speed_x_enemigo *= -1
        
        if cord_y_enemigo > 500 or cord_y_enemigo < 0:
                speed_y_enemigo *= -1
        
        #Guardamos y actualizamos los nuevos valores de "Nave enemiga2" para que en cada iteracion se actualice y genere efecto movimiento
        for i in range(len(posiciones_enemigos2)):
            cord_x_enemigo2, cord_y_enemigo2 = posiciones_enemigos2[i]
            cord_x_enemigo2 -= speed_x_enemigo2
            cord_y_enemigo2 += speed_y_enemigo2
            posiciones_enemigos2[i] = (cord_x_enemigo2, cord_y_enemigo2)
            
            if cord_x_enemigo2 > 1000 or cord_x_enemigo2 < 0 or cord_y_enemigo2 > 600 or cord_y_enemigo2 < 0: #Hacemos que reaparezcan luego de salir de pantalla
                cord_x_enemigo2 = random.randint(0, 950) #Usamos coordenadas random para aumentar la dificultad
                cord_y_enemigo2 = 0
                speed_x_enemigo2 *= -1

            posiciones_enemigos2[i] = (cord_x_enemigo2, cord_y_enemigo2) #Fijamos las nuevas coordenadas por iteracion
        
        
        #Parte dibujos o represntaciones del juego ---------------------------------------------------------------------------------------------------------------
        
        #Dibujamos las explosiones de misil,implementando el temporizador para retrasar la imagen de efecto
        nuevas_explosiones = []
        for explosion in explosiones:
            x, y = explosion["pos"]
            ventana.blit(explosion_misil, [x, y+50])

            explosion["temporizador"] -= 1
            if explosion["temporizador"] > 0:
                nuevas_explosiones.append(explosion)

        explosiones = nuevas_explosiones
        
        
        #Dibujamos las "Naves enemigas" segun las coordenadas guardadas anteriormente
        for posicion in posiciones_enemigos:
            cord_x_enemigo, cord_y_enemigo = posicion
            ventana.blit(enemigo, (cord_x_enemigo, cord_y_enemigo))
        
        
        #Dibujamos las "Naves enemigas2" segun las coordenadas guardadas anteriormente
        for posicion in posiciones_enemigos2:
                x,y = posicion
                ventana.blit(enemigo2, (x,y))
            
        
        #Obtenemos las coordenadas de los elementos a traves de las imagenes para luego usarlas para chequear las colisiones
        rect_nave = player_1.get_rect(topleft=(cord_x_navespacial, cord_y_navespacial))
        rect_nave.inflate_ip(70, 90) 
        rect_superenemigo = super_enemigo.get_rect(topleft=(cord_x_super,0))
        

        #Dibujamos la "Nave espacial" y la nave "Super enemigo"
        if vida_player1 > 0: #Condicion para determinar el fin del juego
            ventana.blit(player_1,[cord_x_navespacial,cord_y_navespacial]) #Le pasamos como segundo argumento los valores creados anteriormente
        else:
            explosion_player1() #Invocamos al metodo explosion_player cuando ya no quedan mas vidas
        
        if vida_supernave > 0: #Condicion para determinar el fin del juego
            ventana.blit(super_enemigo,(cord_x_super,0)) #Posicionamos la nave sobre el limite inferior de la ventana , con movimiento sobre el eje X
        else :
            explosion_super() #Invocamos al metodo explosion_super cuando ya no quedan mas vidas
        
        
        #Dibujamos los misiles del Superenemigo
        if vida_supernave > 0:
            for misil in lista_misil:
                ventana.blit(super_misil,misil)
                #incluimos otro misil 
                otro_x = misil[0] + 40
                otro_y = misil[1]
                ventana.blit(super_misil, (otro_x,otro_y))
                #incluimos otro misil 
                otro_x = misil[0] - 40
                otro_y = misil[1] 
                ventana.blit(super_misil, (otro_x,otro_y))
        
        #Dibujamos los disparos del misil
        if vida_supernave > 0: 
            for misil in lista_misil:
                misil[1] += 10 #Velocidad de desplazamiento del misil
                ventana.blit(super_misil,misil)


        #Dibujamos los disparos de laser con las coordenadas almacenadas en una lista al presionar tecla "space"
        for laser in lista_laser:
            laser[1] -= 10 #Velocidad de desplazamiento del laser
            ventana.blit(imagen_laser,laser)
            if laser[1] < -10:  #Eliminamos los lasers que salen de la ventana para optimizar el almacenamiento en memoria
                lista_laser.remove(laser)
        
        
        #Logica necesaria para implementar la secuencia de imagenes como efecto de propulsores , proporcionada por la documentacion oficial
        indice_imagen = (indice_imagen + 1) % len(imagenes)
        #Cargamos imagenes de "Propulsores"
        if vida_player1 > 0:
            ventana.blit(imagenes[indice_imagen],(cord_x_navespacial+20,cord_y_navespacial+80))#Usamos las coordenadas de la nave y le sumamos los pixels necesarios para centrarlo
        
        
        #Actualizamos la ventana
        pygame.display.update()

        
    
        # Establece la velocidad del juego
        reloj.tick(60)


    
