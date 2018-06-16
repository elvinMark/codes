import pygame
import os
from Edge import *
from Background import *
from Map import *
from Block import *
from constants import *
from Start import *
from End import *
from Fish import *

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
bg = Background(BG_DIR)
edge = Edge(EDGE_DIR)

def set_pos(obj,map_pos):
    obj.rect.left,obj.rect.top = map_pos[1]*SIZE_BLOCK[0],map_pos[0]*SIZE_BLOCK[1]

def update_game(list_blocks,list_obstacles,arr,game_map,screen):
    for i in range(DIM):
        for j in range(DIM):
            if game_map.get_value(i,j)<0:
                list_obstacles[-game_map.get_value(i,j) - 1].set_pos((j*SIZE_BLOCK[0],i*SIZE_BLOCK[1]))
            elif game_map.get_value(i,j)>0 and game_map.get_value(i,j)<100:
                list_blocks[game_map.get_value(i,j) - 1].set_pos((j*SIZE_BLOCK[0],i*SIZE_BLOCK[1]))
    for lb in list_blocks:
        screen.blit(lb.image,lb.rect)
    for lo in list_obstacles:
        screen.blit(lo.image,lo.rect)
    set_pos(arr,arr.map_pos)
    screen.blit(arr.image,arr.rect)

def do_key_action(gmap,arr,event):
    if event.key == pygame.K_SPACE:
        if arr.get_direction() == ARR_R:
            gmap.move_horizontal(arr.map_pos[0],MOVE_F)
        elif arr.get_direction() == ARR_L:
            gmap.move_horizontal(arr.map_pos[0],MOVE_B)
        elif arr.get_direction() == ARR_D:
            gmap.move_vertical(arr.map_pos[1],MOVE_F)
        elif arr.get_direction() == ARR_U:
            gmap.move_vertical(arr.map_pos[1],MOVE_B)
    if event.key == pygame.K_RIGHT:
        arr.move(1)
    if event.key == pygame.K_LEFT:
        arr.move(-1)
set_pos(edge,EXTRA_POS)
def game_loop(game_map):
    game_flag = True
    gmap = Map(game_map)
    lb,lo,arr,start,end = gmap.get_game_objects()
    set_pos(start,start.map_pos)
    set_pos(end,end.map_pos)
    fish = Fish(FISH_DIR,(start.rect.centerx,start.rect.centery))
    while game_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_flag = False
                break
            if event.type == pygame.KEYDOWN:
                do_key_action(gmap,arr,event)
        fish.move(gmap,lb,lo)
        screen.blit(bg.image,bg.rect)
        screen.blit(start.image,start.rect)
        screen.blit(end.image,end.rect)
        update_game(lb,lo,arr,gmap,screen)
        screen.blit(fish.image,fish.rect)
        screen.blit(edge.image,edge.rect)
        pygame.display.flip()
        clock.tick(FPS)

def run_game():
    for level in LEVELS:
        game_loop(level)
        
if __name__ == "__main__":
    run_game()
