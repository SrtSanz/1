
import pygame as pg
import random as rd

from Juegaso.Objetos import Jugador, Meteorito, Madrina

from Juegaso import FPS, mapa_niveles

pg.init()
pg.display.set_caption('Un nuevo comienzo')

#Arreglar icono = pg.image.load("Recursos/icono.png")
#Arreglar pg.display.set_icon(icono) 00

class Escena():

    def __init__(self, mama, ANCHO_X_W = 1200, ALTO_Y_H = 800):
        self.mama = mama
        self.ANCHO_X_W = ANCHO_X_W
        self.ALTO_Y_H = ALTO_Y_H
        self.reloj = pg.time.Clock()

    def imagen(self, fondo):
        self.fondo = fondo

        #Imagenes
        fondo = pg.image.load("Recursos/6fondo.webp").convert_alpha()
        fondo = pg.transform.scale(fondo,(self.ANCHO_X_W, self.ALTO_Y_H))

    def mover(self, x, x_mover):
        self.x = x
        self.x_mover = x_mover
        #movimiento de fondo
        self.x_mover = x % self.fondo.get_rect().width
        self.pantalla.blit(self.fondo,(x_mover - self.fondo.get_rect().width, 0))
        if x_mover < self.ANCHO_X_W:
            self.pantalla.blit(self.fondo,(x_mover, 0))
            x -= 5
    
class Juego():
    def __init__(self, ANCHO_X_W = 1200, ALTO_Y_H = 800):
        self.pantalla = pg.display.set_mode((ANCHO_X_W, ALTO_Y_H))
        self.escena = Escena(self.pantalla)         
        self.jugador = Jugador(self.pantalla, ANCHO_X_W // 2, ALTO_Y_H // 2)
        self.meteorito = Meteorito(self.pantalla)
        #self.meteoritos = [] #creamos una lista vacía  y ahí montamos un bucle
        self.reloj = pg.time.Clock()
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

        
    def bucle_ppal(self):

    #while self.vidas > 0 and nivel < len(niveles):
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
        
            

            #Llamadas de método
        
            self.pantalla.blit(self.fondo,(0, 0))
            self.pantalla.blit(self.nave,(50, 400))

            self.jugador.imagen()
           #self.jugador.colisión()
            self.jugador.mover()
            """"
            self.jugador.colision()
            if not self.jugador.vive:
                self.vidas -= 1
                self.jugador.reset()
            """

           # self.escena.imagen()
           # self.escena.mover()
            """
            self.meteorito.imagen()
            for meteorito in self.meteoritos:
                meteoritos.colision(self.jugador) #aquí llamamos el cambio de estado vivo/muerto
                meteorito.imagen()
            """
        

        pg.display.flip()       

if __name__ == '__main__':
   
    pg.init()

    juego = Juego()
    juego.bucle_ppal()

    pg.quit()