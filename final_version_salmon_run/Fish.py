import pygame
from constants import *
from Block import *
from Map import *

class Fish(pygame.sprite.Sprite):
    def __init__(self,img_loc,pos=(0,0),direction=FISH_R):
        self.image = pygame.image.load(img_loc)
        self.rect = self.image.get_rect()
        self.rect.centerx,self.rect.centery = pos
        self.direction = FISH_R
    def set_pos(self,x,y):
        self.rect.centerx,self.rect.centery = (x,y)
   
        
    def move(self,gmap,lb,lo):
        x = self.rect.centerx
        y = self.rect.centery
        i = y/SIZE_BLOCK[1]
        j = x/SIZE_BLOCK[0]
        if self.direction == FISH_R:
            
            self.set_pos(x+FISH_SPEED,y)
        elif self.direction == FISH_L:
            self.set_pos(x-FISH_SPEED,y)
        elif self.direction == FISH_U:
            self.set_pos(x,y - FISH_SPEED)
        elif self.direciton == FISH_D:
            self.set_pos(x,y + FISH_SPEED)
    
