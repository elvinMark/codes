import os
import random

N = 7
SIZE_BLOCK = (48,48)
DIM = 12
SCREEN_SIZE = (DIM*SIZE_BLOCK[0],DIM*SIZE_BLOCK[1])
FPS = 20
GAME_TITLE = "SALMON RUN"
EXTRA_POS = [0,DIM-1]
MOVE_F = 1
MOVE_B = 0
ARR_R = 1
ARR_D = 2
ARR_L = 3
ARR_U = 4
FISH_U = 1
FISH_D = 2
FISH_R = 3
FISH_L = 4
FISH_SPEED = 1
RM = [[0,180,-90,90],[180,0,90,-90],[90,-90,0,180],[-90,90,180,0]]#Rotation Matrix
JUDGE = [[[],[1,5,0],[3,6,0],[]],[[],[0,5,1],[],[2,6,1]],[[3,5,2],[],[],[1,6,2]],[[2,5,3],[],[0,6,3],[]],[[2,3,5],[0,1,5],[0,3,6],[1,2,6]],[[],[],[0,3,6],[1,2,6]],[[2,3,5],[0,1,5],[],[]]]
TYPE_0 = 0
TYPE_1 = 1
TYPE_2 = 2
TYPE_3 = 3
TYPE_4 = 4
TYPE_5 = 5
TYPE_6 = 6
START_TIME = 10*FPS #10 seconds
BG_DIR = os.path.join('img','bg.png')
START_DIR = os.path.join('img','start.png')
END_DIR = os.path.join('img','end.png')
EDGE_DIR = os.path.join('img','edge.png')
FISH_DIR = [os.path.join('img','fish_' + str(i) + '.png') for i in range(3)]
BLOCKS_DIR = [os.path.join('img','block'+str(i)+'.png') for i in range(N)]
GROUND_DIR = os.path.join('img','ground.png')
BEAR_DIR = os.path.join('img','bear.png')
ROCK_DIR = os.path.join('img','rock.png')
OBSTACLES_DIR = [BEAR_DIR,ROCK_DIR]
ARROW_DIR = os.path.join('img','arrow.png')
def generate_random_map():
    gmap = [DIM*[0] for i in range(DIM)]
    for i in range(2,DIM-2):
        for j in range(2,DIM-2):
            gmap[i][j] = int(random.random()*(N-1) + 1)
    gmap[EXTRA_POS[0]][EXTRA_POS[1]]= int(random.random()*(N-1) + 1)
    gmap[3][1] = 100
    gmap[5][1] = 200
    gmap[6][DIM-2]=300
    return gmap
game_map_1 = generate_random_map()#[[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,2,1,3,5,2,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

LEVELS = [game_map_1]
