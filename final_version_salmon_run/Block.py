import pygame
from constants import *

class Block(pygame.sprite.Sprite):
    def __init__(self,img_loc,pos=(0,0)):
        self.image = pygame.image.load(img_loc)
        self.image = pygame.transform.scale(self.image,SIZE_BLOCK)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
    def set_pos(self,pos):
        self.rect.left,self.rect.top = pos
    
