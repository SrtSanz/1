import pygame as pg

from Juegaso import mapa_niveles, FPS

from Juegaso.Objetos import Jugador, Meteorito 

class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
        

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.pantalla = pg.display.set_mode((ANCHO_X_W, ALTO_Y_H))       
        self.jugador = Jugador(self.pantalla, self.pantalla.get_width() // 2, self.pantalla.get_height() // 2)
        self.meteorito = []
        #self.meteoritos = [] #creamos una lista vacía  y ahí montamos un bucle
        self.todos = []
        self.todos.append(self.meteorito)
        self.todos.append(self.jugador)
        self.vidas = 3


        #Imagenes
        pg.image.load("Recursos/6fondo.webp").convert_alpha()
        self.fondo = pg.transform.scale(pg.image.load("Recursos/6fondo.webp").convert_alpha(),(self.ANCHO_X_W, self.ALTO_Y_H))
        

        """
        def crea_meteoritos(self):
            for col in range (4):
                for fil in range(5):
            # x = 5 + 60 * col
                    1 = Meteorito(self.pantalla, 5 + 60 * col, 35 + 30 * fil, 50, 20 )
                    self.meteoritos.append(1) 
        """

        self.todos = self.todos + self.meteoritos #sumas dos arrais los concatenas en listas

        
    def bucle_ppal(self):
    #nivel = 0    
    #while self.vidas > 0 and nivel < len(mapa_niveles):
        #self.creameteoritos(nivel)
        
        game_over = False
        while self.vidas > 0:
                         #and lend(self.creameteorito)> 0:
        
            """""
            si pasan n meteoritos. psas al siguiente nivel
            if len(self.meteoritos) == n:
                nivel += 1 -> pasar de nivel 
                if nivel >= len(niveles):
                    game_over = True
                else:
                    self.meteoritos(nivel)
            """
            self.reloj.tick(FPS)
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    self.vidas = 0
        """"            
        nivel += 1
        self.jugador.reset() <- la inicializa en su sitio
        """
            #Llamadas de método
        
            self.pantalla.blit(self.fondo,(0, 0))
            self.pantalla.blit(self.nave,(50, 400))

            self.jugador.mover()
            # self.escena.mover()
            #self.meteorito.mover()

            #todos los cosos que se mueven
            for coso in self.todos:
                coso.mover()

            for coso in self.todos:
                coso.imagen()

            self.jugador.imagen()
           #self.jugador.colisión()
            
            """"
            self.jugador.colision()
            if not self.jugador.vive:
                self.vidas -= 1
                self.jugador.reset()
            """

           # self.escena.imagen()
           
            """
            self.meteorito.imagen()
            for meteorito in self.meteoritos:
                meteoritos.colision(self.jugador) #aquí llamamos el cambio de estado vivo/muerto
                meteorito.imagen()

            """

        
        

        pg.display.flip()

class G_O(Escena):
    def __init__(self, pantalla):
        super().__init__():
        


pg.quit()