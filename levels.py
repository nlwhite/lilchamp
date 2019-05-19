############################################################################
#
# Name: levels.py
# Date: May, 2019
# By: Nicole White
# Description: Levels
#
############################################################################
import level_raw_data
import classes
import tiles

def load_level(raw_data):
    result = []

    # Read the raw data values and store them as Tile objects
    for j, row in enumerate(raw_data):
        result.append([])
        for item in row:
            if item == 0:
                result[j].append(tiles.grass)
            elif item == 1:
                result[j].append(tiles.stone_wall)
            elif item == 2:
                result[j].append(tiles.npc1)
            elif item == 9:
                result[j].append(tiles.portal1)

    return result

level_one = classes.Level()
level_one.data = load_level(level_raw_data.level_one)
level_one.name = 'Level 1'

level_two = classes.Level()
level_two.data = load_level(level_raw_data.level_two)
level_two.name = 'Level 2'
