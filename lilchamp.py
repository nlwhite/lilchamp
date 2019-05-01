import pygame
import sys
from pygame.locals import *

############################################################################
#
# Name: 2.py
# Date: April, 2019
# By: Nicole White
# Description: Beginning of a little game. Requires pygame module.
#
############################################################################


class Tile():
    ''' Tile '''
    passable = True
    poison = False
    name = 'Tile'
    sprite = ''

    def __str__(self):
        ''' Informaton to display if the object is called as a string '''

        if self.name:
            return 'Tile: {}'.format(str(self.name))

        else:
            print('Tile')

class Level():
    data = []
    tile_counter_y = 0
    tile_counter_x = 0


class Player():
    ''' The player '''
    right = 'spr/rog1.png'
    left = 'spr/rog2.png'
    up = 'spr/rog3.png'
    down = 'spr/rog1.png'
    name = 'Player 1'
    hp = 5
    x = 30
    y = 30
    moving = 'still'
    current_tile = Tile()
    above_tile = Tile()
    below_tile = Tile()
    left_tile = Tile()
    right_tile = Tile()


level_input = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,1,0,1],
[1,0,0,1,0,0,0,0,0,0,0,1,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]


level_one = Level()

champ = Player()
champ.name = 'Nico'

grass = Tile()
grass.name = 'Grass'
grass.passable = True
grass.sprite = 'spr/grass.png'

stone_wall = Tile()
stone_wall.name = 'Stone Wall'
stone_wall.passable = False
stone_wall.sprite = 'spr/block.png'

for j, row in enumerate(level_input):
    level_one.data.append([])
    for k, item in enumerate(row):
        if item == 0:
            level_one.data[j].append(grass)
        elif item == 1:
            level_one.data[j].append(stone_wall)



# champ.current_tile = level_one.data[champ.new_y][champ.new_x]

pygame.init()

FPS = 12
fpsClock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x_max = len(level_one.data[0]) * 32   # num of cols in the level * 32 px
y_max = len(level_one.data) * 32 # num of rows in the level * 32 pix

up = pygame.K_w
right = pygame.K_d
down = pygame.K_s
left = pygame.K_a
space_bar = pygame.K_SPACE

show_text = False

# MAke
screen_x = 300
screen_y = 300
SURF = pygame.display.set_mode((screen_x,screen_y),1,32)
pygame.display.set_caption('Lil Champ')

champImg = pygame.image.load(champ.right)
grassImg = pygame.image.load(grass.sprite)
blockImg = pygame.image.load(stone_wall.sprite)


while True:
    fpsClock.tick(FPS)

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            print('tile counter x: {}'.format(level_one.tile_counter_x))
            print('x coord: {}'.format(int(len(level_one.data[0]) / 2) - level_one.tile_counter_x))


            if event.key == up:
                champ.moving = 'up'

            if event.key == right:
                champ.moving = 'right'

            if event.key == down:
                champ.moving = 'down'

            if event.key == left:
                champ.moving = 'left'

            if event.key == space_bar:
                print('current tile: {}'.format(champ.current_tile))

                if show_text == False:
                    show_text = True
                elif show_text == True:
                    show_text = False



    if champ.moving != 'still':

        if event.type == KEYUP:
            print('end')
            champ.moving = 'still'

        else:
            if champ.moving == 'right':
                level_one.tile_counter_x -= 1

                # Get the Tile beneath the player
                y_row = int((len(level_one.data) / 2 ) - level_one.tile_counter_y)
                x_offset = level_one_data[y_row]
                x_offset = int((len(level_one.data[y_row]) / 2 ) - level_one.tile_counter_x)


                the_tile = [y_row][x_offset]
                champ.current_tile = the_tile


                #level_one.data[int(len(level_one.data) / 2) - level_one.tile_counter_y][int(len(level_one.data[int(len(level_one.data) / 2) - level_one.tile_counter_x]) / 2) - level_one.tile_counter_x]

                if champ.current_tile.passable == False:
                    level_one.tile_counter_x += 1


            elif champ.moving == 'left':
                level_one.tile_counter_x += 1

                if champ.current_tile.passable == False:
                    level_one.tile_counter_x -= 1

            elif champ.moving == 'up':
                champImg = pygame.image.load(champ.up)

                level_one.tile_counter_y += 1

                if champ.current_tile.passable == False:
                    level_one.tile_counter_y -= 1


            elif champ.moving == 'down':

                level_one.tile_counter_y -= 1


                if champ.current_tile.passable == False:
                    level_one.tile_counter_y += 1
    # Draw the map
    tile_counter_y = level_one.tile_counter_y

    for row in level_one.data:
        tile_counter_x = level_one.tile_counter_x
        for tile in row:
            if tile == grass:
                sprite = grassImg
            elif tile == stone_wall:
                sprite = blockImg

            SURF.blit(sprite, (tile_counter_x * 32, tile_counter_y * 32))
            tile_counter_x += 1
        tile_counter_y += 1


    SURF.blit(champImg, (screen_x / 2, screen_y / 2))

    if show_text:
        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        textSurfaceObj = fontObj.render('Name: {} HP: {}'.format(champ.name, champ.hp), True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (x_max - 50, y_max - 50)
        SURF.blit(textSurfaceObj, textRectObj)

    try:
        champ.above_tile = level[int(champ.y /32) - 1][int(champ.x / 32)]
        champ.below_tile = level[champ.new_y + 1][champ.new_x]
        champ.left_tile = level[champ.new_y][champ.new_x - 1]
        champ.right_tile = level[champ.new_y][champ.new_x + 1]
    except:
        pass
