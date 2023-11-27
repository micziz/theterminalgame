# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

def setStuff(coordsArray, position):
    position[coordsArray[0][0]][coordsArray[0][1]] = "x"
    position[coordsArray[1][0]][coordsArray[1][1]] = "D"
    position[coordsArray[4][0]][coordsArray[4][1]] = "y"
    for coord in coordsArray[2]:
        position[coord[0]][coord[1]] = "f"
    return position
