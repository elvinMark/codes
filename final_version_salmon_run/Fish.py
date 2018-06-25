import pygame
from constants import *
from Block import *
from Map import *

class Fish(pygame.sprite.Sprite):
    def __init__(self,img_loc,pos=(0,0),direction=FISH_R):
        self.images = [pygame.image.load(img_loc[i]) for i in range(3)]
        self.sprite_count = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx,self.rect.centery = pos
        self.direction = FISH_R
    def set_pos(self,x,y):
        self.rect.centerx,self.rect.centery = (x,y)
    def move(self,flag):
        if flag:
            x = self.rect.centerx
            y = self.rect.centery
            if self.direction == FISH_R:            
                self.set_pos(x+FISH_SPEED,y)
            elif self.direction == FISH_L:
                self.set_pos(x-FISH_SPEED,y)
            elif self.direction == FISH_U:
                self.set_pos(x,y - FISH_SPEED)
            elif self.direction == FISH_D:
                self.set_pos(x,y + FISH_SPEED)
        self.sprite_count += 1
        if self.sprite_count == 5*3:
            self.sprite_count = 0
        self.image = self.images[self.sprite_count/5]
    def is_center(self):
        x = self.rect.centerx
        y = self.rect.centery
        if x%(SIZE_BLOCK[0]/2)==0 and y%(SIZE_BLOCK[1]/2)==0 and (x/(SIZE_BLOCK[0]/2))%2 != 0 and (y/(SIZE_BLOCK[1]/2))%2 != 0:
            return True
        return False
    def rotate(self,past_direction):
        for i in range(3):
            self.images[i] = pygame.transform.rotate(self.images[i],RM[past_direction-1][self.direction-1])
    def is_end(self):
        x = self.rect.centerx
        y = self.rect.centery
        if (x+FISH_SPEED)%SIZE_BLOCK[0]==0 or (y+FISH_SPEED)%SIZE_BLOCK[1]==0 :
            return True
        return False
    def change_direction(self,TYPE_BLOCK):
        past_direction = self.direction
        if TYPE_BLOCK == TYPE_0:
            if self.direction == FISH_U:
                self.direction = FISH_R
            elif self.direction == FISH_L:
                self.direction = FISH_D
        elif TYPE_BLOCK == TYPE_1:
            if self.direction == FISH_U:
                self.direction = FISH_L
            elif self.direction == FISH_R:
                self.direction = FISH_D
        elif TYPE_BLOCK == TYPE_2:
            if self.direction == FISH_D:
                self.direction = FISH_L
            elif self.direction == FISH_R:
                self.direction = FISH_U
        elif TYPE_BLOCK == TYPE_3:
            if self.direction == FISH_D:
                self.direction = FISH_R
            elif self.direction == FISH_L:
                self.direction = FISH_U
        if past_direction != self.direction:
            self.rotate(past_direction)
    def can_pass(self,gmap,lb,lo):
        x = self.rect.centerx
        y = self.rect.centery
        i = y/SIZE_BLOCK[1]
        j = x/SIZE_BLOCK[0]
        i1 = i
        j1 = j
        if self.direction == FISH_R:
            j1 += 1
        elif self.direction == FISH_U:
            i1 -= 1
        elif self.direction == FISH_L:
            j1 -= 1
        elif self.direction == FISH_D:
            i1 += 1
        print lb[gmap.get_value(i1,j1)-1].type_block
        print lb[gmap.get_value(i,j)-1].type_block
        if lb[gmap.get_value(i1,j1)-1].type_block in JUDGE[lb[gmap.get_value(i,j)-1].type_block][self.direction - 1]:
            return False
        return True
    def check_status(self,gmap,lb,lo):
        x = self.rect.centerx
        y = self.rect.centery
        i = y/SIZE_BLOCK[1]
        j = x/SIZE_BLOCK[0]
        if gmap.get_value(i,j)<100 and gmap.get_value(i,j)>0:
            if self.is_center():
                self.change_direction(lb[gmap.get_value(i,j)-1].type_block)
            if self.is_end():
                return self.can_pass(gmap,lb,lo)
        return True
