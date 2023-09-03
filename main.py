# Imports
import os, sys, time

# Initial ASCII grid
upAndDown = "-------------------------------"

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

position[0][7] = "x"
position[-1][7] = "D"
position[3][4] = "f"
position[3][10] = "f"
position[5][10] = "y"

doorPos = [9, 7]
enemyPos = [[3, 4], [3, 10]]
coinPos = []
chestPos = [5, 10]

def move(action, pos):
    if action == "w":
        pos[0] = pos[0] - 1
        return pos
    elif action == "s":
        pos[0] = pos[0] + 1
        return pos
    elif action == "a":
        pos[1] = pos[1] - 1
        return pos
    elif action == "d":
        pos[1] = pos[1] + 1
        return pos

def act(action, pos):
    if action == "e":
        if position[pos[0] + 1][pos[1]] == "f":
            return True, "kill"
        else:
            return False,  "kill"
    if action == "o":
        if position[pos[0] + 1][pos[1]] == "y":
            return True, "open"
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

coins = 0

collisions = {
    "door": False,
    "enemy": False,
    "coin": False,
    "chest": False
}

def checkCollision(pos):
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

startPos = [0, 7]
pos = startPos
while True:
    didMove = False
    didAct = False
    availableMoves = ["w", "s", "a", "d"]
    actions = [["e", "Sword Swing"], ["o", "Open Chest"], ["q", "Shield"]]
    checkActions = ["e", "o", "q"]
    if "x" in position[0]:
        availableMoves.remove("w")

    
    for i in position:
        if "x" in i[1]:
            availableMoves.remove("a")
        if "x" in i[-2]:
            availableMoves.remove("d")

    if "x" in position[-1]:
        availableMoves.remove("s")
        actions.remove(["e", "Sword Swing"])
        checkActions.remove("e")

        

    
    print(f"Coins: {str(coins)}")
    print(upAndDown)
    for el in position:
        print(' '.join(el))
    print(upAndDown)
    for moveX in availableMoves:
        print(f"Available Move: {moveX}")
    for actionX in actions:
        print(f"{actionX[1]}: {actionX[0]}")
    
    i = 0
    while True:
        action = input("Move: ")
        if action in availableMoves:
            didMove = True
            break
        elif action in checkActions:
            didAct = True
            break
        else:
            if i == 3:
                exitQ = input("DO YOU WANT TO EXIT? (y/n): ")
                if exitQ == "y":
                    sys.exit(0)
                else:
                    i = 0
            i = i + 1

    if didMove:
        position[pos[0]][pos[1]] = " "
        pos = move(action, pos)
        collisions = checkCollision(pos)
        if collisions["door"] == True:
            break
        if collisions["enemy"] == True:
            print("You died")
            break
        if collisions["coin"] == True:
            coins = coins + 1
            collisions["coin"] = False
        if collisions["chest"] != True:
            position[pos[0]][pos[1]] = "x"
        else:
            pos = [pos[0] - 1, pos[1]]
            position[pos[0]][pos[1]] = "x"
            print("You are Blocked, try proceeding elswhere")
            time.sleep(0.2)
        collisions["chest"] = False
    elif didAct:
        sucsess, wdid = act(action, pos)
        if sucsess:
            if wdid == "kill": 
                position[pos[0] + 1][pos[1]] = "c"
                enemyPos.remove([pos[0] + 1, pos[1]])
                coinPos.append([pos[0] + 1, pos[1]])
            elif wdid == "open":
                position[pos[0] + 1][pos[1]] = "l"
                coins = coins + 5
                chestPos.clear()
            elif wdid == "move":
               position[pos[0] + 1][pos[1]] = " " 
               position[pos[0] + 2][pos[1]] = "f"
               enemyPos.remove([pos[0] + 1, pos[1]])
               enemyPos.append([pos[0] + 2, pos[1]])
        else:
            if wdid == "move":
                print("You tried to push me outside. It's not possible")
    os.system("clear")
    
print("Thanks For Playing")