import pygame
from constants import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self,img_loc,pos=(0,0),map_pos=(0,0)):
        self.image = pygame.image.load(img_loc)
        self.image = pygame.transform.scale(self.image,SIZE_BLOCK)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = pos
        self.map_pos = map_pos
    def set_map_pos(self,map_pos):
        self.map_pos = map_pos
    def get_direction(self):
        i = self.map_pos[0]
        j = self.map_pos[1]
        if i-j > 0:
            if i == DIM-2:
                return ARR_U
            else:
                return ARR_R
        elif j-i > 0:
            if j == DIM-2:
                return ARR_L
            else:
                return ARR_D
    def move(self,opt):
        i = self.map_pos[0]
        j = self.map_pos[1]
        d = self.get_direction()
        if d == ARR_R:
            if i+opt == j or i+j+opt == DIM-1:
                self.map_pos = (i+opt,j+1)
                self.image = pygame.transform.rotate(self.image,opt*90)
            else :
                self.map_pos = (i+opt,j)
        elif d == ARR_U:
            if i == j+opt or i+j+opt == DIM-1:
                self.map_pos = (i-1,j+opt)
                self.image = pygame.transform.rotate(self.image,opt*90)
            else :
                self.map_pos = (i,j+opt)
        elif d == ARR_L:
            if j == i-opt or i+j-opt == DIM-1:
                self.map_pos = (i-opt,j-1)
                self.image = pygame.transform.rotate(self.image,opt*90)
            else:
                self.map_pos = (i-opt,j)
        elif d == ARR_D:
            if i == j-opt or i+j-opt == DIM-1:
                self.map_pos = (i+1,j-opt)
                self.image = pygame.transform.rotate(self.image,opt*90)
            else :
                self.map_pos = (i,j-opt)
            
        
