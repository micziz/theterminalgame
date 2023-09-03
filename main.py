# Imports
import os, sys, time

from parts.board import upAndDown, position
from parts.initialPositions import doorPos,enemyPos, coinPos, chestPos
from parts.move import move
from parts.act import act
from parts.checkCollisions import checkCollision

position[0][7] = "x"
position[-1][7] = "D"
position[3][4] = "f"
position[3][10] = "f"
position[5][8] = "y"

coins = 0

collisions = {
    "door": False,
    "enemy": False,
    "coin": False,
    "chest": False
}


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
        try:
            action = input("Move: ")
        except KeyboardInterrupt:
            print("\nThanks For Playing")
            sys.exit(0)
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
        collisions = checkCollision(pos, collisions, doorPos, enemyPos, coinPos, chestPos)
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
        sucsess, wdid = act(action, pos, position, chestPos)
        if sucsess:
            if wdid == "kill": 
                position[pos[0] + 1][pos[1]] = "c"
                enemyPos.remove([pos[0] + 1, pos[1]])
                coinPos.append([pos[0] + 1, pos[1]])
            elif wdid == "open":
                coins = coins + 5
                position[pos[0] + 1][pos[1]] = " "
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