############################################################################
#
# Name: classes.py
# Date: May, 2019
# By: Nicole White
# Description: Classes
#
############################################################################
import pygame
from spritesheet_functions import SpriteSheet
import constants

pygame.init()
SURF = pygame.display.set_mode((constants.SCREEN_X,constants.SCREEN_Y),1,32)
pygame.display.set_caption('Lil Champ')


class Tile():
    ''' Tile -- a level map is comprised of these '''
    type = 'Terrain'
    passable = True                      # can you walk through the tile
    poison = False                       # is the tile poison
    name = 'Tile'                        # name of the tile (eg, 'grass')
    sprite = ''                          # graphic for the tile
    portal = False
    portal_destination_level = 0
    portal_destination_coords = []

    def __str__(self):
        ''' Informaton to display if the object is called as a string '''

        if self.name:
            return 'Tile: {}'.format(str(self.name))

        else:
            print('Tile')

class NPC():
    ''' NPC '''
    type = 'NPC'
    sprite_sheet = SpriteSheet('spr/Engineer.png')

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

    dialogue = 'I touch butts !'

    right = sprites[0]
    left = sprites[3]
    up = sprites[8]
    down = sprites[1]


    passable = False                      # can you walk through the tile
    poison = False                       # is the tile poison
    name = 'Creature'
    img = pygame.image.load('spr/rog1.png')

    def __str__(self):
        ''' Information to display if the object is called as a string '''

        if self.name:
            return 'Creature: {}'.format(str(self.name))

        else:
            print('NPC')

class Level():
    ''' A list holding an array of tiles, creating a level map '''
    id = 0
    name = 'Lobby'
    data = []                          # list array of Tile objects
    raw_data = []
    tile_counter_y = 4               # x offset used when drawing the level
    tile_counter_x = 2                 # y offset used when drawing the level


class Player():
    ''' The player, a champ. '''
    type = 'Me'
    right = 'spr/rog1.png'
    left = 'spr/rog2.png'
    up = 'spr/rog3.png'
    down = 'spr/rog3.png'
    name = 'Player 1'
    hp = 5
    x = 1
    y = 1
    moving = 'still'
    facing = 'east'
    block_facing = [6,5]
    current_tile = Tile()
    above_tile = Tile()
    below_tile = Tile()
    left_tile = Tile()
    right_tile = Tile()
