def checkCollision(pos, collisions, doorPos, enemyPos, coinPos, chestPos):
    if pos == doorPos:
        collisions["door"] = True
    if len(enemyPos) != 0:
        for posX in enemyPos:
            if pos == posX:
                collisions["enemy"] = True
    if len(coinPos) != 0:
        for coin in coinPos:
            if pos == coin:
                collisions["coin"] = True
    if pos == chestPos:
        collisions["chest"] = True
    return collisions