import pygame as pg
import random as rd

class Madrina:
    def __init__(self, mama: pg.surface, x, y, ANCHO_X_W = 1200, ALTO_Y_H = 800):
        self.mama = mama
        self.x = x
        self.y = y
        self.ANCHO_X_W = ANCHO_X_W
        self.ALTO_Y_H = ALTO_Y_H
        self.vx = 0
        self.vy = 0

    def imagen(self):
        pass
    
    def dibujar(self):
        pass

    def mover(self):
        pass

class Jugador(Madrina):
    def __init__(self, mama, x, y, ANCHO_X_W = 1200, ALTO_Y_H = 800):
        self.nave = pg.transform.scale(pg.image.load("Recursos/Imagenes/nave.png").convert_alpha(),(150,80))
        self.rect = self.nave.get_rect()
        super().__init__(mama, x, y, ANCHO_X_W, ALTO_Y_H)
        self.vx = 1
        self.vy = 1
        self.vive = True

    def imagen(self):
        self.mama.blit(self.nave(self.x, self.y))
    
    def mover(self):
        tecla = pg.key.get_pressed()
        #Pa mover las teclas
        if tecla[pg.K_LEFT]:
            self.x -= self.vx
        if tecla[pg.K_RIGHT]:
            self.x += self.vx

        #limites
        if self.x < 0:
            self.x = 0
        if self.x + self.ANCHO_X_W >= self.mama.get_width():
            self.x = self.mama.get_width() - self.ANCHO_X_W

      #límites??
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= self.mama.get_width() - self.ANCHO_X_W:
            self.vx *= -1

        if self.y <= 0 or self.y >= self.mama.get_height()- self.ALTO_Y_H:
            self.vy *= -1
        """
        esto hará que cuando la nave se choq pierda una vida

        if self.nave = self.colision:
            self.vive = False
        
    
    def colisión(self, x1, y1, a1, b1, x2, y2, a2, b2, ex=0):
        if x1 + a1 > x2 + ex and \
           x1 + ex < x2 + a2 and \
           y1 + b1 > y2 + ex and \
           y1 + ex < y2 + b2:
           return True
        else:
            return False
    
    def reset(self):


    """

class Meteorito(pg.sprite.Sprite):
    def __init__(self, mama):
        super().__init__()
        self.mama = mama

    def imagen(self):

        self.imaletoria = rd.randrange(6)
        if self.imaletoria == 0:
            self.m1 = pg.transform.scale(pg.image.load("Recursos/m1.jpeg").convert(),(100,100))
        if self.imaletoria == 1:
            self.m2 = pg.transform.scale(pg.image.load("Recursos/m2.jpeg").convert(),(80,80))
        if self.imaletoria == 2:
            self.m3 = pg.transform.scale(pg.image.load("Recursos/m3.jpeg").convert(),(60,60))
        if self.imaletoria == 3:
            self.m4 = pg.transform.scale(pg.image.load("Recursos/m4.jpeg").convert(),(40,40))
        if self.imaletoria == 4:
            self.m5 = pg.transform.scale(pg.image.load("Recursos/m5.jpeg").convert(),(20,20))
        if self.imaletoria == 5:
            self.m6 = pg.transform.scale(pg.image.load("Recursos/m6.jpeg").convert(),(10,10))
        if self.imaletoria == 6:
            self.m7 = pg.transform.scale(pg.image.load("Recursos/m7.jpeg").convert(),(50,50))
        """
        m1 = pg.image.load("Recursos/m1.jpeg").convert_alpha()
        pg.transform.scale(m1,(200,80))
        m2 = pg.image.load("Recursos/m2.jpeg").convert_alpha()
        pg.transform.scale(m2,(200,80))
        m3 = pg.image.load("Recursos/m3.jpeg").convert_alpha()
        pg.transform.scale(m3,(200,80))
        m4 = pg.image.load("Recursos/m4.jpeg").convert_alpha()
        pg.transform.scale(m4,(200,80))
        m5 = pg.image.load("Recursos/m5.jpeg").convert_alpha()
        pg.transform.scale(m5,(200,80))
        m6 = pg.image.load("Recursos/m6.jpeg").convert_alpha()
        pg.transform.scale(m6,(200,80))
        m7 = pg.image.load("Recursos/m7.jpeg").convert_alpha()
        pg.transform.scale(m7,(200,80))
        """
    def mover():
        pass