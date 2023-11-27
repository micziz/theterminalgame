# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

# Import mkdir to create a new directory!
from os import mkdir
# Import isdir to check if a directory exits
from os.path import isdir

from json import dumps

def createSF(level, coins):
    if isdir("./ttgsave") == True:
        with open("./ttgsave/save.json", "wt") as f:
            f.write(dumps({
                "level": level,
                "coins": coins
            }))
    else:
        mkdir("./ttgsave")
        with open("./ttgsave/save.json", "wt") as f:
            f.write(dumps({
                "level": level,
                "coins": coins
            }))

def act(action, pos, position, chestPos, currentLevel, coins):
    if action == "e":
        if (position[pos[0]][pos[1] + 1] == "f"):
            return True, "killd"
        elif (position[pos[0] + 1][pos[1]] == "f"):
            return True, "kills"
        elif (position[pos[0]][pos[1] - 1] == "f"):
            return True, "killa"
        else:
            return False,  "kill"
    if action == "o":
        if (position[pos[0]][pos[1] + 1] == "y"):
            return True, "opend"
        elif (position[pos[0] + 1][pos[1]] == "y"):
            return True, "opens"
        elif (position[pos[0]][pos[1] - 1] == "y"):
            return True, "opena"
        else:
            return False, "open"
    if action == "q":
        checkPos = [pos[0] + 2, pos[1]]
        if checkPos != chestPos: 
            if checkPos[0] < len(position):
                return True, "move"
            else:
                return False, "move"
        else: 
            return False, "move"
    if action == "z":
        try:
            createSF(currentLevel, coins)
            return True, "save"
        except:
            return False, "save"
            