import pygame
import os
import random

#Game variables

##Screen Variables
HEIGHT = 500
WIDTH = 500
screen_size = (HEIGHT,WIDTH)
window_name = "Helping the Salmon"

##Game Variables
flag = True #game loop
N = 6 #number of blocks
Dx = 50 # displacement in X
Dy = 50 # displacement in Y
rows = 8 #Number of rows
cols = 8 #Number of cols	
origin = (0,0)
game_panel_pos = (80,80)

##Directions 
bg_dir = os.path.join('img','bg.jpg')
gp_dir = os.path.join('img','gp.png')
blocks_dir = [os.path.join('img','block'+str(i)+'.jpg') for i in range(N)]

#Classes and Functions
class Background(pygame.sprite.Sprite):
	def __init__(self,img_loc,pos):
		self.image = pygame.image.load(img_loc)
		self.image = pygame.transform.scale(self.image,screen_size)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = pos

class Blocks(pygame.sprite.Sprite):
	def __init__(self,img_loc,pos):
		self.image = pygame.image.load(img_loc)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = pos 
	def move(self,x,y):
		self.rect.left += x*Dx
		self.rect.top += y*Dy

class GamePanel(pygame.sprite.Sprite):
	def __init__(self,img_loc,pos):
		self.image = pygame.image.load(img_loc)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = pos
class Sync():
	def __init__(self):
		self.sync_elems = []
	def add_elem(e):
		sync_elems.append(e)
	def 
def generate_random_blocks(pos):
	n = int(N*random.random())
	return Blocks(os.path.join(blocks_dir[n]),pos)

#Set pygame
pygame.init()
pygame.display.set_caption(window_name)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#Create Objects
bg = Background(bg_dir,origin)
gp = GamePanel(gp_dir,game_panel_pos)

while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			flag = False
			break
		if event.type == pygame.KEYDOWN:

	screen.blit(bg.image,bg.rect)
	screen.blit(gp.image,gp.rect)
	pygame.display.flip()
	clock.tick(20)

pygame.quit()

