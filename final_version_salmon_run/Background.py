import pygame
from constants import *

class Background(pygame.sprite.Sprite):
    def __init__(self,img_loc,pos=(0,0)):
        self.image = pygame.image.load(img_loc)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = pos
