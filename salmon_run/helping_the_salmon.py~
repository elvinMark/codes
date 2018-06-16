import pygame
import os
import random
import sounds

#Game variables

##Screen Variables
HEIGHT = 500
WIDTH = 500
screen_size = (HEIGHT,WIDTH)
window_name = "Helping the Salmon"

##Game Variables
N = 7 #number of blocks
Dx = 48 # displacement in X
Dy = 48 # displacement in Y
dim = 10
rows = dim #Number of rows (game + edge)
cols = dim #Number of cols (game + edge)

#Maps
map_level1 = [[0,0,0,0,1,0,0,0,0,0],[0,3,7,6,7,7,4,6,5,0],[0,2,6,6,7,4,6,7,2,0],[0,1,7,6,5,2,4,2,6,0],[0,5,4,6,6,3,7,2,1,0],[0,2,1,1,2,2,3,2,5,0],[0,7,3,1,7,7,3,2,1,0],[0,5,6,7,2,5,7,3,7,0],[0,6,2,7,3,3,6,7,5,0],[0,0,0,0,0,0,0,0,0,0]]
map_level2 =[[0,0,0,0,0,0,0,0,3,0],[0,1,4,7,7,6,1,4,5,0],[0,4,7,6,6,6,1,3,6,0],[0,2,4,1,5,2,2,7,7,0],[0,5,4,4,2,2,5,2,3,0],[0,1,7,7,1,1,6,4,4,0],[0,5,6,7,4,5,7,1,6,0],[0,2,3,7,6,1,3,7,3,0],[0,6,4,3,1,2,7,7,2,0],[0,0,0,0,0,0,0,0,0,0]]
levels = [map_level1,map_level2]
#coordinates	
origin = (0,0)
game_panel_pos = (50,50)
edge_panel_pos = (15,15)


##Directories 
bg_game_dir = os.path.join('img','bg.jpg')
gp_dir = os.path.join('img','gp.png')
edge_dir = os.path.join('img','edge.png')
blocks_dir = [os.path.join('img','block'+str(i)+'.png') for i in range(N)]
arr_left_dir = os.path.join('img','arrow_left.png')
arr_right_dir = os.path.join('img','arrow_right.png')
arr_up_dir = os.path.join('img','arrow_up.png')
arr_down_dir = os.path.join('img','arrow_down.png')
fish_dir = [os.path.join('img','fish_'+str(i) +'.png') for i in range(4)]

game_loop_sound_dir = os.path.join('wav','flowing-loop.wav')
game_start_sound_dir = os.path.join('wav','flowing-intro.wav')
slip_sound_dir = os.path.join('wav','move.wav')
splash_sound_dir = os.path.join('wav','splash.wav')
move_sound_dir =os.path.join('wav','pop.wav')


#Classes and Functions
class Background(pygame.sprite.Sprite):
	def __init__(self,img_loc,pos=(0,0)):
		self.image = pygame.image.load(img_loc)
		self.image = pygame.transform.scale(self.image,screen_size)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = pos

class Blocks(pygame.sprite.Sprite):
	def __init__(self,img_loc,pos=(0,0)):
		self.image = pygame.image.load(img_loc)
		self.image = pygame.transform.scale(self.image,(Dx,Dy))
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = pos 
	def set_pos(self,pos):
		self.rect.left, self.rect.top = pos

class Panel(pygame.sprite.Sprite):
	def __init__(self,img_loc,pos=(0,0)):
		self.image = pygame.image.load(img_loc)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = pos

class Fish(pygame.sprite.Sprite):
	def __init__(self,img_dir,vector=0,pos=(0,0)):
		self.vector = vector
		self.directions = [pygame.image.load(img_dir[i]) for i in range(len(img_dir))]
		self.image = self.directions[self.vector]
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = pos
		self.moving = False

	def set_pos(self,pos):
		self.rect.left, self.rect.top = pos
	def rotate(self,alpha = 1):
		self.vector += 1
		if self.vector >3:
			self.vector = 0
		self.image = self.directions[self.vector]
		self.rect = self.image.get_rect()
	def move(self):
		if self.vector == 0:
			self.rect.top -= 5
		elif self.vector == 1:
			 self.rect.left += 5
		elif self.vector == 2:
			self.rect.top += 5
		elif self.vector==3:
			self.rect.left -= 5
	def get_coordinates(self):
		return [(self.rect.left - game_panel_pos[0])/Dx,(self.rect.top - game_panel_pos[1])/Dy]


def generate_random_block(pos):
	n = int(N*random.random())
	return Blocks(os.path.join(blocks_dir[n]),pos)

def create_empty_map():
	return [[0]*cols for i in range(rows)]
class fish_pos():
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.direction = 0
class Block():
	def __init__(self,game_map):
		self.x = 1
		self.y = 0
		flag = False
		self.value = 0
		for i in range(rows):
			if i==0 or i == dim-1:
				for j in range(cols):
					if game_map[i][j] != 0:
						self.x = i
						self.y = j
						self.value = game_map[i][j]
						flag = True
						break
			else:
				if game_map[i][0] != 0:
					self.x = i
					self.y = 0
					self.value = game_map[i][0]
					break
				if 	game_map[i][dim-1] != 0:
					self.x = i
					self.y = dim-1
					self.value = game_map[i][dim-1]
					break
			if flag:
				break
		self.arrow = 0
		check_arrow(self)

def init_game(game_map):
	list_blocks = []	
	count = 1
	curr_map = create_empty_map()
	for i in  range(rows):
		for j in range(cols):
			if game_map[i][j]!=0:
				list_blocks.append(Blocks(os.path.join(blocks_dir[game_map[i][j]-1])))
				curr_map[i][j] = count
				count += 1
	return list_blocks,curr_map

def update_blocks(curr_map,list_blocks):
	for i in range(rows):
		for j in range(cols):
			if curr_map[i][j] != 0:
				list_blocks[curr_map[i][j]-1].set_pos((game_panel_pos[0]+j*Dx,game_panel_pos[1]+i*Dy))

##Changing the Matrix:
def move_horizontal(curr_map,row,opt):
	a = curr_map[row][-opt-1]
	for i in range(opt+1,cols+opt):
		curr_map[row][i] = curr_map[row][i -2*opt - 1]
	curr_map[row][opt] = a
def move_vertical(curr_map,col,opt):
	a = curr_map[-opt-1][col]
	for i in range(opt+1,rows+opt):
		curr_map[i][col] = curr_map[i -2*opt - 1][col]
	curr_map[opt][col] = a

def printmap(matrix):
    for y in range(0,dim):
        mapp=""
        for x in range(0,dim):
            mapp += str(matrix[x][y]) + " "
        print(mapp)
def check_arrow(block):
    if block.x==0:
        block.arrow=4
    elif block.x==dim-1:
        block.arrow=2
    elif block.y==0:
        block.arrow=1
    elif block.y==dim-1:
        block.arrow=3


def Relocateblock(block,matrix):
    if block.x==0:
        for i in range(dim-1,0,-1): #move row to right
            #print("block" + str(i) + " " + str(block.y) + " value: "+ str(matrix[i][block.y]) + "substitue by " + str(i-1) + " " + str(block.y) + " value: "+ str(matrix[i-1][block.y]))
            matrix[i][block.y]=matrix[i-1][block.y]
        matrix[block.x][block.y]=0 #empty current block 
        block.x=dim-1
        block.value=matrix[block.x][block.y]
        #k = input("stop")
    elif block.x==dim-1:
        for i in range(0,dim-1): #move row to left
            matrix[i][block.y]=matrix[i+1][block.y]
        matrix[block.x][block.y]=0 #empty current block 
        block.x=0
        block.value=matrix[block.x][block.y]
    elif block.y==0:
        for j in range(dim-1,0,-1): #move row to down
            matrix[block.x][j]=matrix[block.x][j-1]
        matrix[block.x][block.y]=0
        block.y=dim-1
        block.value=matrix[block.x][block.y]
    elif block.y==dim-1:
        for j in range(0,dim-1): #move row to up
            matrix[block.x][j]=matrix[block.x][j+1]
        matrix[block.x][block.y]=0 #empty current block 
        block.y=0
        block.value=matrix[block.x][block.y]

def do_key_action(event,matrix,block):
	##to do
	matrix[block.x][block.y]=0
	if (event.key == pygame.K_RIGHT and block.x <(dim-1) and block.y%(dim-1)==0):
		block.x += 1
		if block.x==dim-1:
			if block.y==0: 
				block.y +=1
			else:
				block.y-=1
	elif (event.key == pygame.K_LEFT and block.x >0 and block.y%(dim-1)==0):
		block.x -= 1
		if block.x==0:
			if block.y==0: 
				block.y +=1
			else:
				block.y-=1
	elif (event.key == pygame.K_UP and block.y>0 and block.x%(dim-1)==0):
		block.y -= 1
		if block.y==0:
			if block.x==0: 
				block.x +=1
			else :
				block.x-=1
	elif (event.key == pygame.K_DOWN and block.x%(dim-1)==0):
		block.y += 1
		if block.y==(dim-1):
			if block.x==0: 
				block.x +=1
			else:
				block.x-=1
	elif (event.key == pygame.K_a):
		if block.x==0:
			block.y +=1
			if block.y==dim-1:
				block.x+=1
		elif block.y==0:
			block.x -=1
			if(block.x==0):
				block.y+=1
		elif block.x==dim-1:
			block.y-=1
			if block.y==0:
				block.x-=1
		elif block.y==dim-1:
			block.x +=1
			if block.x==dim-1:
				block.y-=1
	elif event.key == pygame.K_s :
		if block.x==0:
			block.y -=1
			if block.y==0:
				block.x+=1
		elif block.y==0:
			block.x +=1
			if(block.x==dim-1):
				block.y+=1
		elif block.x==dim-1:
			block.y+=1
			if block.y==dim-1:
				block.x-=1
		elif block.y==dim-1:
			block.x -=1
			if block.x==0:
				block.y-=1
	elif event.key == pygame.K_SPACE: 
		matrix[block.x][block.y]=block.value
		Relocateblock(block,matrix)

	matrix[block.x][block.y]=block.value
	check_arrow(block)

def checknextdir(k,olddi):#checkthedirectionofthe next block the fish wil be
    if k==1:
        if olddi ==4:
            return 1
        elif olddi ==3:
            return 2
        else :
            return 0
    elif k==2:
        if olddi ==1:
            return 2
        elif olddi ==4:
            return 3
        else :
            return 0
    elif k==3:
        if olddi ==1:
            return 4
        elif olddi ==2:
            return 3
        else :
            return 0
    elif k==4:
        if olddi ==2:
            return 1
        elif olddi ==3:
            return 4
        else :
            return 0
    elif k==5:
        return olddi
    elif k==6:
        if (olddi==1 or olddi==3) :
            return olddi
        else :
            return 0
    elif k==7:
        if (olddi==4 or olddi==2) :
            return olddi
        else:
             return 0
    elif k==-1:
        return 0
    
def directionoffish(matrix,fish):
    lx=fish.x#locarion in x
    ly=fish.y#location in y
    if(fish.direction==1):
        return checknextdir(matrix[lx+1][ly],1)
    elif(fish.direction==2):
        return checknextdir(matrix[lx][ly+1],2)
    elif(fish.direction==3):
        return checknextdir(matrix[lx-1][ly],3)
    elif(fish.direction==4):
        return checknextdir(matrix[lx][ly-1],4)
def do_mouse_action(curr_map):
	#to implement
	a =2 

#Set pygame
pygame.init()
pygame.display.set_caption(window_name)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#Creating Sprites
bg_game = Background(bg_game_dir,origin) #Background
gp = Panel(gp_dir,game_panel_pos) #Game Panel
edge = Panel(edge_dir,edge_panel_pos)
arr_left = Blocks(arr_left_dir)
arr_right = Blocks(arr_right_dir)
arr_up = Blocks(arr_up_dir)
arr_down = Blocks(arr_down_dir)
arrs = [arr_right,arr_up,arr_left,arr_down]
fish = Fish(fish_dir,vector=1)

#Creating Sounds
game_loop_sound = pygame.mixer.Sound(game_loop_sound_dir)
game_start_sound = pygame.mixer.Sound(game_start_sound_dir)
slip_sound = pygame.mixer.Sound(slip_sound_dir)
splash_sound = pygame.mixer.Sound(splash_sound_dir)
move_sound = pygame.mixer.Sound(move_sound_dir)
sounds.music.start()

def start_screen():
	#game_start_sound.play(loops=-1)
	start_flag = True
	while start_flag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				start_flag = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					start_flag = False
		pygame.display.flip()
		clock.tick(20)
	game_start_sound.stop()

def game_loop(game_map,init_pos,final_pos):
	game_flag = True
	lb,curr_map = init_game(game_map)
	block = Block(game_map)
	#game_loop_sound.play(loops=-1)
	count = 0
	fish.set_pos(init_pos)
	fishp = fish_pos(fish.rect.left,fish.rect.top)
	while game_flag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_flag = False
				break
			if event.type == pygame.KEYDOWN:
				sounds.pop_fx.play()
				do_key_action(event,curr_map,block)
			if event.type == pygame.MOUSEBUTTONDOWN:
				do_mouse_action(curr_map)
			if event.type == sounds.SONG_END:
				sounds.music.on_music_end()
			if event.type == sounds.SONG_END:
				sounds.music.on_sfx_end()
		if count > 50 and not fish.moving:
			fish.moving = True
		if fish.moving == True:
			
			fish.move()

		update_blocks(curr_map,lb)
		lb[block.value-1].set_pos(origin)
		printmap(curr_map)
		check_arrow(block)
		arrs[block.arrow-1].set_pos((game_panel_pos[0]+block.y*Dx,game_panel_pos[1]+block.x*Dy))
		screen.blit(bg_game.image,bg_game.rect)
		screen.blit(gp.image,gp.rect)
		screen.blit(edge.image,edge.rect)
		screen.blit(arrs[block.arrow-1].image,arrs[block.arrow-1].rect)
		for i in lb:
			screen.blit(i.image,i.rect)
		screen.blit(fish.image,fish.rect)
		pygame.display.flip()
		clock.tick(20)
		count += 1
	game_loop_sound.stop()

def run_game():
	start_screen()
	for level in levels:
		game_loop(level,(game_panel_pos[0]+Dx-5,game_panel_pos[1]+Dy-5),(game_panel_pos[0]+10*Dx+5,game_panel_pos[1]+10*Dx+5))

run_game()
pygame.quit()
