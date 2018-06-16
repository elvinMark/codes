import pygame

class End(pygame.sprite.Sprite):
    def __init__(self,img_loc,pos=(0,0),map_pos=(0,0)):
        self.image = pygame.image.load(img_loc)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = pos
        self.map_pos = map_pos
