
import pygame as pg
import random as rd

from Juegaso.Objetos import Jugador, Meteorito, Madrina

from Juegaso.Escenas import Partida

from Juegaso import FPS, mapa_niveles

pg.init()
pg.display.set_caption('Un nuevo comienzo')

#Arreglar icono = pg.image.load("Recursos/icono.png")
#Arreglar pg.display.set_icon(icono) 00

class Esceno():

    def __init__(self, mama, ANCHO_X_W = 1200, ALTO_Y_H = 800):
        self.mama = mama
        self.ANCHO_X_W = ANCHO_X_W
        self.ALTO_Y_H = ALTO_Y_H

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
        pantalla = pg.display.set_mode((ANCHO_X_W, ALTO_Y_H))
        partida = Partida(pantalla)
        partida.bucle_ppal()