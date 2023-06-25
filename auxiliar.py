import pygame as pg

class auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(imagen , columnas, filas):
        lista = []
        fotograma_ancho = int(imagen.get_width()/columnas)
        fotograma_alto = int(imagen.get_height()/filas)
        x = 0
        for fila in range(filas):
            for columna in range(columnas):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                print(x,y,fotograma_ancho,fotograma_alto)
                
                surface_fotograma = imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                lista.append(surface_fotograma)

        return lista