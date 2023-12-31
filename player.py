import pygame as pg
from constantes import *
from imagenes import *
from auxiliar import auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravedad,jump_valor,direccion) -> None:
        self.walk_r = auxiliar.getSurfaceFromSpriteSheet(walk_r,10,1)
        self.walk_l = auxiliar.getSurfaceFromSpriteSheet(walk_l,10,1)
        self.stay_r = auxiliar.getSurfaceFromSpriteSheet(stay_r,10,1)
        self.stay_l = auxiliar.getSurfaceFromSpriteSheet(stay_l,10,1)
        self.jump_r = auxiliar.getSurfaceFromSpriteSheet(jump_r,3,1)
        self.jump_l = auxiliar.getSurfaceFromSpriteSheet(jump_l,3,1)
        self.fallin_r = auxiliar.getSurfaceFromSpriteSheet(fall_r,2,1)
        self.fallin_l = auxiliar.getSurfaceFromSpriteSheet(fall_l,2,1)
        self.frame = 0 
        self.live = 5 
        self.score = 0
        self.mover_x = 0
        self.mover_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.jump_velocidad = 0
        self.jumping = jump_valor
        self.is_jump = False
        self.is_fallin = False
        self.gravity = gravedad
        self.animation = self.stay_r
        self.animation_speed = 0.2
        self.direccion = direccion
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.tiempo_transcurrido_animacion = 0
        self.tiempo_transcurrido_movimiento = 0 
       
        
    
    def walk(self):
        if self.direccion == "derecha":
            self.mover_x = self.speed_walk
            self.animation = self.walk_r
        else:
            self.mover_x =  -1 * self.speed_walk
            self.animation = self.walk_l   
        self.frame = 0 

    def jump(self):
        if not self.is_jump:
            self.jump_velocity = JUMP_POWER
            self.is_jump = True
            if self.direccion == "derecha":
                self.animation = self.jump_r
            else:
                self.animation = self.jump_l
            self.frame = 0
            
        
    def stay(self):
        
        if self.direccion == "derecha":
            self.animation = self.stay_r
        else :
            self.animation = self.stay_l    
        self.mover_x = 0
        self.mover_y = 0
        self.frame = 0

    def todos_los_movimientos(self,delta_ms):
        self.tiempo_transcurrido_movimiento += delta_ms

        if self.tiempo_transcurrido_movimiento >= 20:
                self.tiempo_transcurrido_movimiento = 0 
                if self.is_fallin == True:
                    self.is_fallin = False
                    self.frame = 0
                    if self.direccion == "derecha":
                        self.animation = self.fallin_r
                    else:
                        self.animation = self.fallin_l

                if self.is_jump:
                    self.rect.y += self.jump_velocity
                    self.jump_velocity += GRAVEDAD
                    self.is_fallin = True

                
                self.rect.x += self.mover_x
                self.rect.y += self.mover_y
                
                if self.rect.y >= SUELO_PRINCIPAL:
                    self.rect.y = SUELO_PRINCIPAL
                    self.jump_velocity = 0
                    self.is_jump = False

                

    def todas_las_animacion(self,delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms

        if self.tiempo_transcurrido_animacion >= 40:
            self.tiempo_transcurrido_animacion = 0 
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
            
            
    def update(self,delta_ms):
        self.todos_los_movimientos(delta_ms)
        self.todas_las_animacion(delta_ms)
        

        
    def draw(self, screen):
        print(self.frame)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)