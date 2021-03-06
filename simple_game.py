import pygame
import random
import os

#Define Game Varibales

HEIGHT = 500
WIDTH = 500
flag = True
screen_size = (HEIGHT,WIDTH)
N = 3 #Number of available blocks
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
        self.move_with_mouse = False
    def move(self):
        if self.move_with_mouse:
            self.rect.left, self.rect.top = pygame.mouse.get_pos()

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

b1 = generate_random_block([50,50])

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            continue
        if event.type == pygame.MOUSEBUTTONUP:
            if b1.rect.collidepoint(pygame.mouse.get_pos()):
                b1.move_with_mouse = True
              
    b1.move()
    screen.blit(bg.image,bg.rect)
    screen.blit(b1.image,b1.rect)
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
