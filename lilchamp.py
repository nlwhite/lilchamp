import pygame
import sys
from pygame.locals import *

import constants
import classes
import tiles
import levels
import level_raw_data
from spritesheet_functions import SpriteSheet
############################################################################
#
# Name: lilchamp.py
# Date: April, 2019
# By: Nicole constants.WHITE
# Description: Beginning of a little game. Requires pygame module.
#
############################################################################



# Create a player instance
champ = classes.Player()
champ.name = 'Nico'

# Choose a level
current_level = levels.level_one

# Define keys for player input
SPACE_BAR = pygame.K_SPACE
QUIT_GAME = [pygame.K_ESCAPE, pygame.K_q]

# Start pygame
pygame.init()


constants.FPSClock = pygame.time.Clock()

show_text = False
npc_dialogue = False

# MAke
SURF = pygame.display.set_mode((constants.SCREEN_X,constants.SCREEN_Y),1,32)
pygame.display.set_caption('Lil Champ')

sprite_sheet = SpriteSheet('spr/Rogue.png')

# player - sprites from sprite sheet in a list
sprites = [sprite_sheet.get_image(0, 0, 32, 32), # right
            sprite_sheet.get_image(32, 0, 32, 32),
            sprite_sheet.get_image(64, 0, 32, 32),
            sprite_sheet.get_image(96, 0, 32, 32), # left
            sprite_sheet.get_image(128, 0, 32, 32),
            sprite_sheet.get_image(160, 0, 32, 32),
            sprite_sheet.get_image(192, 0, 32, 32), # right blink
            sprite_sheet.get_image(224, 0, 32, 32), # left blink
            sprite_sheet.get_image(0, 32, 32, 32), # up
            sprite_sheet.get_image(32, 32, 32, 32),
            sprite_sheet.get_image(64, 32, 32, 32),
            sprite_sheet.get_image(96, 32, 32, 32)]

champ.right = sprites[0]
champ.left = sprites[3]
champ.up = sprites[8]
champ.down = sprites[1]
champImg = champ.right

while True:
    constants.FPSClock.tick(constants.FPS)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                champ.moving = 'north'
                champ.facing = champ.moving

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                champ.moving = 'east'
                champ.facing = champ.moving

            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                champ.moving = 'south'
                champ.facing = champ.moving

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                champ.moving = 'west'
                champ.facing = champ.moving

            if event.key == pygame.K_e:
                if show_text == False:
                    show_text = True
                elif show_text == True:
                    show_text = False

            if event.key == SPACE_BAR:

                print('tile counter x: {} y: {}'.format(tile_counter_x, tile_counter_y))

                if champ.facing == 'east':
                    champ.block_facing = [champ.x + 1, champ.y]
                elif champ.facing == 'west':
                    champ.block_facing = [champ.x - 1, champ.y]
                elif champ.facing == 'south':
                    champ.block_facing = [champ.x, champ.y + 1]
                elif champ.facing == 'north':
                    champ.block_facing = [champ.x, champ.y - 1]

                print('current: {} {}'.format(champ.x, champ.y))

                print('facing ' + str(champ.block_facing[0]) + ',' + str(champ.block_facing[1]))
                print(current_level.data[champ.block_facing[1]][champ.block_facing[0]].name)
                #
                # if npc_dialogue == True:
                #     npc_dialogue = False

                if current_level.data[champ.block_facing[1]][champ.block_facing[0]].type == 'NPC' and npc_dialogue == False:
                    npc_dialogue = True
                    dialogue_text = current_level.data[champ.block_facing[1]][champ.block_facing[0]].dialogue
                else:
                    npc_dialogue = False


            if event.key in QUIT_GAME:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_c:
                print('x counter: {}'.format(current_level.tile_counter_x))
                print('len champ.y: {}'.format(str(int(len(current_level.data[champ.x])))))
                print('divided by 2: {}'.format(str(int(len(current_level.data[champ.y]) / 2))))
                print('divided by 2 minus x counter: {}'.format(str(int(len(current_level.data[champ.y]) / 2 - current_level.tile_counter_x))))
                print('x = divided by 2, minus x counter, minus 2: {}'.format(str(int(len(current_level.data[champ.y]) / 2 - current_level.tile_counter_x) - 2)))
                print('current: {}, {}'.format(champ.x, champ.y))


    # if champ is anything other than still, do the following:
    if champ.moving != 'still':

        npc_dialogue = False

        # If a keyup event is detected figure out which keys, if any, are
        # still being pressed and call set the player moving in the right
        # direction. If no keys are pressed set player to still.
        if event.type == KEYUP:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w] or pressed[pygame.K_UP]:
                champ.moving = 'north'
                champ.facing = champ.moving
            elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                champ.moving = 'east'
                champ.facing = champ.moving
            elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                champ.moving = 'south'
                champ.facing = champ.moving
            elif pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                champ.moving = 'west'
                champ.facing = champ.moving


            else:
                champ.moving = 'still'

        # Do movement
        if champ.moving == 'east':

            champImg = champ.right


            current_level.tile_counter_x -= 1

            # Get the Tile beneath the player:
            # y is the length of the level array (ie how many rows),
            # divided by two to place the character in the center.
            # the incrementing tile_counter_y value is subtracted to this
            # to shift the drawing of the map tiles

            champ.y = int((len(current_level.data) / 2 ) - current_level.tile_counter_y)

            # x value is the length of one row (ie number of columns)
            # divided by 2, minus tile_counter_x
            champ.x = int(len(current_level.data[champ.y]) / 2 - current_level.tile_counter_x) - 2



            # set current_tile to the Tile object found at the place
            # in the level array determined above
            champ.current_tile = current_level.data[champ.y][champ.x]

            # If the new current tile is not passable, put the player location
            # back the way it was
            if champ.current_tile.passable == False:
                current_level.tile_counter_x += 1
                champ.x -= 1
                champ.current_tile = current_level.data[champ.y][champ.x]

            # If the new current tile is a portal, move to a new level
            if champ.current_tile.portal == True:
                current_level = levels.level_two


            champ.block_facing = [champ.x + 1, champ.y]


        elif champ.moving == 'west':
            champImg = champ.left


            current_level.tile_counter_x += 1

            champ.y = int((len(current_level.data) / 2 ) - current_level.tile_counter_y)
            champ.x = int(len(current_level.data[champ.y]) / 2 - current_level.tile_counter_x) - 2

            champ.current_tile = current_level.data[champ.y][champ.x]


            if champ.current_tile.passable == False:
                current_level.tile_counter_x -= 1
                champ.x += 1
                champ.current_tile = current_level.data[champ.y][champ.x]

            champ.block_facing = [champ.x - 1, champ.y]

        elif champ.moving == 'north':
            champImg = champ.up


            current_level.tile_counter_y += 1
            champ.y = int((len(current_level.data) / 2 ) - current_level.tile_counter_y)
            champ.x = int(len(current_level.data[champ.y]) / 2 - current_level.tile_counter_x) - 2
            champ.current_tile = current_level.data[champ.y][champ.x]

            if champ.current_tile.passable == False:
                current_level.tile_counter_y -= 1
                champ.y += 1
                champ.current_tile = current_level.data[champ.y][champ.x]

            champ.block_facing = [champ.x, champ.y - 1]

        elif champ.moving == 'south':
            champImg = champ.down


            current_level.tile_counter_y -= 1
            champ.y = int((len(current_level.data) / 2 ) - current_level.tile_counter_y)
            champ.x = int(len(current_level.data[champ.y]) / 2 - current_level.tile_counter_x) - 2
            champ.current_tile = current_level.data[champ.y][champ.x]


            if champ.current_tile.passable == False:
                current_level.tile_counter_y += 1
                champ.y -= 1
                champ.current_tile = current_level.data[champ.y][champ.x]

            champ.block_facing = [champ.x, champ.y + 1]

        champ.y = int((len(current_level.data) / 2 ) - current_level.tile_counter_y)
        champ.x = int(len(current_level.data[champ.y]) / 2 - current_level.tile_counter_x) - 2

    # Draw the map
    SURF.fill(constants.BLACK)
    tile_counter_y = current_level.tile_counter_y

    for row in current_level.data:
        tile_counter_x = current_level.tile_counter_x

        for tile in row:
            if tile == tiles.grass:
                sprite = tiles.grass.sprite
            elif tile == tiles.stone_wall:
                sprite = tiles.stone_wall.sprite
            elif tile == tiles.npc1:
                sprite = tiles.npc1.right

            SURF.blit(sprite, (tile_counter_x * constants.TILE_PX, tile_counter_y * constants.TILE_PX))

            tile_counter_x += 1
        tile_counter_y += 1

    # Draw the character in the middle of the screen and add a few extra pixels
    # (1/4th the width of a tile on each side) to place it in the middle of the tile
    SURF.blit(champImg, ((constants.SCREEN_X / 2) + (constants.TILE_PX / 4), (constants.SCREEN_Y / 2) + (constants.TILE_PX / 4)))


    if show_text:
        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        textSurfaceObj = fontObj.render('Name: {} HP: {}'.format(champ.name, champ.hp), True, constants.BLACK, constants.WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (50, 20)
        SURF.blit(textSurfaceObj, textRectObj)

    if npc_dialogue:
        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        textSurfaceObj = fontObj.render(dialogue_text, True, constants.BLACK, constants.WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (150, 275)
        SURF.blit(textSurfaceObj, textRectObj)
