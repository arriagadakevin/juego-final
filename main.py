import pygame as pg
import sys
from constantes import *
from player import Player

screen = pg.display.set_mode( (ANCHO_VENTANA,ALTO_VENTANA) )
pg.init()
clock = pg.time.Clock()
imagen_fondo = pg.image.load(r"C:\Users\arria\OneDrive\Escritorio\caballero\fondo\forest_tileset_lite\Demo\demo.jpg")
imagen_fondo = pg.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
player1 = Player(X,Y,SPEED_WALK,SPEED_RUN,GRAVEDAD,JUMP_POWER)
flag_stay = "derecha"
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_d:
                player1.control("walk_r",flag_stay)
                flag_stay = "derecha"
            if evento.key == pg.K_a:
                player1.control("walk_l",flag_stay)
                flag_stay = "izquierda"
            if evento.key == pg.K_w:
                player1.control("jump",flag_stay)
        
        if evento.type == pg.KEYUP:
            if evento.key == pg.K_d or evento.key == pg.K_a or evento.key == pg.K_w:
                    player1.control("stay", flag_stay)
                
    screen.blit(imagen_fondo, imagen_fondo.get_rect())
    player1.update() 
    player1.draw(screen) 
    
    
    
    # player update == verificar como el playyer interactua con el nivel
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel 

    pg.display.flip()
    
    
    delta_ms = clock.tick(FPS)
    