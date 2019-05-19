import classes
import pygame

# Create some tiles
grass = classes.Tile()
grass.name = 'Grass'
grass.passable = True
grass.sprite = pygame.image.load('spr/grass.png')

stone_wall = classes.Tile()
stone_wall.name = 'Stone Wall'
stone_wall.passable = False
stone_wall.sprite = pygame.image.load('spr/block.png')

portal1 = classes.Tile()
portal1.name = 'Portal'
portal1.portal = True
portal1.passable = True
portal1.sprite = pygame.image.load('spr/grass.png')
portal1.portal_destination_level = 1


npc1 = classes.NPC()
npc1.name = 'Nicole'
