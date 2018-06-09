import pygame
import random
import os

#Define Game Varibales

HEIGHT = 500
WIDTH = 500
flag = True
screen_size = (HEIGHT,WIDTH)
N = 6 #Number of available blocks
D = 50
#Classes

class Background(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image,screen_size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Block(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location    
    def move(self,x,y):
        self.rect.left += x*D
        self.rect.top += y*D 
#Functions

def generate_random_block(location):
    n = int(random.random()*N)
    return Block(os.path.join('img','block'+str(n)+'.png'),location)

#Define Game objects

bg = Background(os.path.join('img','bg.jpg'),[0,0])


#Initialize the environment of pygame
pygame.init()

#Set Screen size
screen = pygame.display.set_mode(screen_size)

#Set the clock
clock = pygame.time.Clock()
blocks = []
b1 = generate_random_block([0,0])
blocks.append(b1)
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            blocks[-1].move((event.key == pygame.K_LEFT)*-1 + (event.key == pygame.K_RIGHT)*1,(event.key == pygame.K_UP)*-1+(event.key == pygame.K_DOWN)*1)
            if event.key == pygame.K_BACKSPACE:
                b1 = generate_random_block([0,0])
                blocks.append(b1)
    screen.blit(bg.image,bg.rect)
    for i in blocks:
        screen.blit(i.image,i.rect)
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
