from copy import deepcopy, copy

position = [
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
]

emptyCollisions = {
    "door": False,
    "enemy": False,
    "coin": False,
    "chest": False
}

def getCoords(level):
    if level == 0:
        startPos = [0, 7]
        doorPos = [9, 7]
        enemyPos = [[3, 4], [3, 10]]
        coinPos = []
        chestPos = [5, 10]
        return [startPos, doorPos, enemyPos, coinPos, chestPos]
    elif level == 1:
        startPos = [0, 7]
        doorPos = [9, 7]
        enemyPos = [[3, 2], [3, 5], [3, 7]]
        coinPos = []
        chestPos = [6, 2]
        return [startPos, doorPos, enemyPos, coinPos, chestPos]
    elif level == 2:
        startPos = [0, 7]
        doorPos = [9, 7]
        enemyPos = [[4, 2], [3, 6], [3, 10]]
        coinPos = []
        chestPos = [5, 5]
        return [startPos, doorPos, enemyPos, coinPos, chestPos]


def changeLevel(currentPos, currentCollisions, level, coordsArray):
    currentPos = deepcopy(position)
    currentCollisions = copy(emptyCollisions)
    if level == 0:
        newCordsArray = getCoords(0)
        coordsArray.clear()
        coordsArray = newCordsArray
        return coordsArray, currentPos, currentCollisions
    elif level == 1:
        newCordsArray = getCoords(1)
        coordsArray.clear()
        coordsArray = newCordsArray
        return coordsArray, currentPos, currentCollisions
    elif level == 2:
        newCordsArray = getCoords(2)
        coordsArray.clear()
        coordsArray = newCordsArray
        return coordsArray, currentPos, currentCollisions