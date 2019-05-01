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
    new_x = 0
    new_y = 0
    moving = 'still'
    current_tile = Tile()
    above_tile = Tile()
    below_tile = Tile()
    left_tile = Tile()
    right_tile = Tile()

level = []
level_input = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]




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
    level.append([])
    for k, item in enumerate(row):
        if item == 0:
            level[j].append(grass)
        elif item == 1:
            level[j].append(stone_wall)

# champ.current_tile = level[int(champ.y / 32)][int(champ.x  / 32)]
champ.current_tile = level[champ.new_y][champ.new_x]

pygame.init()

FPS = 12
fpsClock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x_max = len(level[0]) * 32   # num of cols in the level * 32 px
y_max = len(level) * 32 # num of rows in the level * 32 pix

up = pygame.K_w
right = pygame.K_d
down = pygame.K_s
left = pygame.K_a
space_bar = pygame.K_SPACE

show_text = False



tile_counter_y = 0
tile_counter_x = 0

# MAke
SURF = pygame.display.set_mode((300,300),0,32)
pygame.display.set_caption('Lil Champ')

champImg = pygame.image.load(champ.right)
grassImg = pygame.image.load(grass.sprite)
blockImg = pygame.image.load(stone_wall.sprite)

while True:
    fpsClock.tick(FPS)
    tile_counter_y = 0
    pygame.display.update()
    # Draw map
    for row in level:
        tile_counter_x = 0
        for tile in row:
            if tile == grass:
                sprite = grassImg
            elif tile == stone_wall:
                sprite = blockImg

            SURF.blit(sprite, (tile_counter_x * 32, tile_counter_y * 32))
            tile_counter_x += 1
        tile_counter_y += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            print('{}, {}'.format(champ.new_x,champ.new_y))

            if event.key == up:
                champ.moving = 'up'

            if event.key == right:
                champ.moving = 'right'

            if event.key == down:
                champ.moving = 'down'

            if event.key == left:
                champ.moving = 'left'

            if event.key == space_bar:
                print('player xy: {},{}'.format(champ.new_x, champ.new_y))
                print('current: {}'.format(champ.current_tile))
                print('above: {}'.format(champ.above_tile))
                print('below: {}'.format(champ.below_tile))
                print('left: {}'.format(champ.left_tile))
                print('right: {}'.format(champ.right_tile))
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
                    champImg = pygame.image.load(champ.right)
                    champ.new_x += 1

                    if champ.new_x < len(level[0]):
                        new_tile = level[champ.new_y][champ.new_x]
                        champ.current_tile = new_tile
                        if new_tile.passable == False:
                            champ.new_x -= 1

                    elif champ.new_x > len(level[0]) :
                        champ.new_x -= 1


            elif champ.moving == 'left':
                    champImg = pygame.image.load(champ.left)
                    champ.new_x -= 1

                    if champ.new_x > 1:
                        new_tile = level[champ.new_y][champ.new_x]
                        champ.current_tile = new_tile
                        if new_tile.passable == False:
                            champ.new_x += 1

                    elif champ.new_x < 1:
                        champ.new_x += 1


            elif champ.moving == 'up':
                    champImg = pygame.image.load(champ.up)
                    champ.new_y -= 1

                    if champ.new_y > 0:
                        new_tile = level[champ.new_y][champ.new_x]
                        champ.current_tile = new_tile
                        if new_tile.passable == False:
                            champ.new_y += 1

                    elif champ.new_y < 0:
                        champ.new_y += 1


            elif champ.moving == 'down':

                    champImg = pygame.image.load(champ.right)
                    champ.new_y += 1

                    if champ.new_y < len(level):
                        new_tile = level[champ.new_y][champ.new_x]
                        champ.current_tile = new_tile
                        if new_tile.passable == False:
                            champ.new_y -= 1

                    elif champ.new_y > len(level):
                        champ.new_y -=1


    SURF.blit(champImg, (champ.new_x * 32, champ.new_y * 32))

    if show_text:
        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        textSurfaceObj = fontObj.render('Name: {} HP: {}'.format(champ.name, champ.hp), True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (x_max - 50, y_max - 50)
        SURF.blit(textSurfaceObj, textRectObj)

    try:
        champ.above_tile = level[champ.new_y - 1][champ.new_x]
        champ.below_tile = level[champ.new_y + 1][champ.new_x]
        champ.left_tile = level[champ.new_y][champ.new_x - 1]
        champ.right_tile = level[champ.new_y][champ.new_x + 1]
    except:
        pass
