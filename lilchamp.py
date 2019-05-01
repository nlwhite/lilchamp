import pygame
import sys
from pygame.locals import *

############################################################################
#
# Name: lilchamp.py
# Date: April, 2019
# By: Nicole White
# Description: Beginning of a little game. Requires pygame module.
#
############################################################################


class Tile():
    ''' Tile -- a level map is comprised of these '''
    passable = True                      # can you walk through the tile
    poison = False                       # is the tile poison
    name = 'Tile'                        # name of the tile (eg, 'grass')
    sprite = ''                          # graphic for the tile

    def __str__(self):
        ''' Informaton to display if the object is called as a string '''

        if self.name:
            return 'Tile: {}'.format(str(self.name))

        else:
            print('Tile')

class Level():
    ''' A list holding an array of tiles, creating a level map '''
    data = []                          # list array of Tile objects
    tile_counter_y = 0                 # x offset used when drawing the level
    tile_counter_x = 0                 # y offset used when drawing the level


class Player():
    ''' The player, a champ. '''
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

# raw data for the level, store in external file later
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

# Create a level instance
level_one = Level()

# Pixel count for tiles
tile_px = 32

# Create a player instance
champ = Player()
champ.name = 'Nico'

# Create some tiles
grass = Tile()
grass.name = 'Grass'
grass.passable = True
grass.sprite = 'spr/grass.png'

stone_wall = Tile()
stone_wall.name = 'Stone Wall'
stone_wall.passable = False
stone_wall.sprite = 'spr/block.png'

# Read the raw data values and store them as Tile objects
for j, row in enumerate(level_input):
    level_one.data.append([])
    for item in row:
        if item == 0:
            level_one.data[j].append(grass)
        elif item == 1:
            level_one.data[j].append(stone_wall)

# Start pygame
pygame.init()

# animation speed
FPS = 12
fpsClock = pygame.time.Clock()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x_max = len(level_one.data[0]) * tile_px   # num of cols in the level * tile_px px
y_max = len(level_one.data) * tile_px # num of rows in the level * tile_px pix

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
                if show_text == False:
                    show_text = True
                elif show_text == True:
                    show_text = False


    # if champ is anything other than still, do the following:
    if champ.moving != 'still':

        # set champ to 'still' if a keyup event is detected
        if event.type == KEYUP:
            print('end')
            champ.moving = 'still'

        # if there is no key up, do movement
        else:
            if champ.moving == 'right':

                champImg = pygame.image.load(champ.right)

                level_one.tile_counter_x -= 1

                # Get the Tile beneath the player:
                # y is the length of the level array (ie how many rows),
                # divided by two to place the character in the center.
                # the incrementing tile_counter_y balue is subtracted to this
                # to shift the drawing of the map tiles
                y_row = int((len(level_one.data) / 2 ) - level_one.tile_counter_y)
                print('y row: {}'.format(y_row))

                # x value is the length of one row (ie number of columns)
                # divided by 2, minus tile_counter_x
                x_col = int(len(level_one.data[y_row]) / 2 - level_one.tile_counter_x) - 2
                print('x_col: {}'.format(x_col))

                # set current_tile to the Tile object found at the place
                # in the level array determined above
                champ.current_tile = level_one.data[y_row][x_col]

                print('current: {}'.format(champ.current_tile))
                # If the new current tile is not passable, put the player location
                # back the way it was
                if champ.current_tile.passable == False:
                    level_one.tile_counter_x += 1
                    champ.current_tile = level_one.data[y_row][x_col - 1]


            elif champ.moving == 'left':
                champImg = pygame.image.load(champ.left)
                level_one.tile_counter_x += 1
                y_row = int((len(level_one.data) / 2 ) - level_one.tile_counter_y)
                print('y row: {}'.format(y_row))
                x_col = int(len(level_one.data[y_row]) / 2 - level_one.tile_counter_x) - 2
                print('x_col: {}'.format(x_col))
                champ.current_tile = level_one.data[y_row][x_col]
                print('current: {}'.format(champ.current_tile))

                if champ.current_tile.passable == False:
                    level_one.tile_counter_x -= 1
                    champ.current_tile = level_one.data[y_row][x_col + 1]

            elif champ.moving == 'up':
                champImg = pygame.image.load(champ.up)

                level_one.tile_counter_y += 1
                y_row = int((len(level_one.data) / 2 ) - level_one.tile_counter_y)
                print('y row: {}'.format(y_row))
                x_col = int(len(level_one.data[y_row]) / 2 - level_one.tile_counter_x) - 2
                print('x_col: {}'.format(x_col))
                champ.current_tile = level_one.data[y_row][x_col]
                print('current: {}'.format(champ.current_tile))

                if champ.current_tile.passable == False:
                    level_one.tile_counter_y -= 1


            elif champ.moving == 'down':

                champImg = pygame.image.load(champ.down)

                level_one.tile_counter_y -= 1
                y_row = int((len(level_one.data) / 2 ) - level_one.tile_counter_y)
                print('y row: {}'.format(y_row))
                x_col = int(len(level_one.data[y_row]) / 2 - level_one.tile_counter_x) - 2
                print('x_col: {}'.format(x_col))
                champ.current_tile = level_one.data[y_row][x_col]
                print('current: {}'.format(champ.current_tile))


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

            SURF.blit(sprite, (tile_counter_x * tile_px, tile_counter_y * tile_px))
            tile_counter_x += 1
        tile_counter_y += 1

    # Draw the character in the middle of the screen and add a few extra pixels
    # to place it in the middle of the tile
    SURF.blit(champImg, ((screen_x / 2) + (tile_px / 4), (screen_y / 2) + (tile_px / 4)))

    if show_text:
        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        textSurfaceObj = fontObj.render('Name: {} HP: {}'.format(champ.name, champ.hp), True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (50, 20)
        SURF.blit(textSurfaceObj, textRectObj)

    try:
        champ.above_tile = level[int(champ.y /tile_px) - 1][int(champ.x / tile_px)]
        champ.below_tile = level[champ.new_y + 1][champ.new_x]
        champ.left_tile = level[champ.new_y][champ.new_x - 1]
        champ.right_tile = level[champ.new_y][champ.new_x + 1]
    except:
        pass
