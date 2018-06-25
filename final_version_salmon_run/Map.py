from Block import *
from constants import *
from Arrow import *
from Start import *
from End import *
class Map:
    def __init__(self,init_map):
        self.map_data = [DIM*[0] for i in range(DIM)]
        for i in range(DIM):
            for j in range(DIM):
                self.map_data[i][j] = init_map[i][j]
    def get_game_objects(self):
        list_blocks = []
        list_obstacles = []
        count_blocks = 0
        count_obstacles = 0
        arr = Arrow(ARROW_DIR)
        start = Block(START_DIR,type_block=TYPE_5)
        end = Block(END_DIR,type_block=TYPE_5)
        for i in range(DIM):
            for j in range(DIM):
                if self.map_data[i][j] > 0 and self.map_data[i][j]<100:
                    list_blocks.append(Block(BLOCKS_DIR[self.map_data[i][j]-1],type_block=self.map_data[i][j]-1))
                    count_blocks += 1
                    self.map_data[i][j] = count_blocks
                elif self.map_data[i][j] < 0:
                    list_obstacles.append(Block(OBSTACLES_DIR[-self.map_data[i][j] - 1]))
                    count_obstacles += 1
                    self.map_data[i][j] = -count_obstacles
                elif self.map_data[i][j] == 100:
                    arr.set_map_pos((i,j))
                elif self.map_data[i][j] == 200:
                    start.map_pos = (i,j)
                elif self.map_data[i][j] == 300:
                    end.map_pos = (i,j)
        return list_blocks,list_obstacles,arr,start,end
    def get_value(self,i,j):
        return self.map_data[i][j]
    def move_horizontal(self,row,opt):
        extra = self.map_data[EXTRA_POS[0]][EXTRA_POS[1]]
        aux = self.map_data[row][(DIM-5)*opt + 2]
        for i in range(opt*(DIM-5) + 2,opt*(5-DIM)+DIM-3,-2*opt +1):
            self.map_data[row][i] = self.map_data[row][i - 2*opt + 1]
        self.map_data[row][opt*(5 - DIM) + DIM-3] = extra
        self.map_data[EXTRA_POS[0]][EXTRA_POS[1]] = aux

    def move_vertical(self,col,opt):
        extra = self.map_data[EXTRA_POS[0]][EXTRA_POS[1]]
        aux = self.map_data[(DIM-5)*opt + 2][col]
        for i in range(opt*(DIM-5) + 2,opt*(5-DIM)+DIM-3,-2*opt +1):
            self.map_data[i][col] = self.map_data[i - 2*opt + 1][col]
        self.map_data[opt*(5 - DIM) + DIM-3][col] = extra
        self.map_data[EXTRA_POS[0]][EXTRA_POS[1]] = aux
    def print_map(self):
        for i in self.map_data:
            print i
