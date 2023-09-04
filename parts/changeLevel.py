def changeLevel(level):
    if level == 0:
        doorPos = [9, 7]
        enemyPos = [[3, 4], [3, 10]]
        coinPos = []
        chestPos = [5, 10]
        return doorPos, enemyPos, coinPos, chestPos
    elif level == 1:
        doorPos = [9, 7]
        enemyPos = [[4, 2], [4, 6]]
        coinPos = []
        chestPos = [7, 2]
        return doorPos, enemyPos, coinPos, chestPos