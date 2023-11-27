# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

# Imports
# Import system to clear the screen
from os import system
# Import exit to exit at a certain point
from sys import exit
# Import sleep to stop the loop for a couple seconds
from time import sleep

from parts.board import upAndDown
from parts.board import position as initialPosition
from parts.board import initialCollisions
from parts.move import move
from parts.act import act
from parts.checkCollisions import checkCollision
from parts.checkRepetition import checkRepetition
from parts.titlteScreen import titleSreen
from parts.changeLevel import changeLevel
from parts.setStuff import setStuff
from parts.clearScreen import clearscreen

choice = titleSreen()

if choice == 1:
    currentLevel = 0
if choice == 2:
    with open("./ttgsave/save.txt", "rt") as f:
        currentLevel = int(f.read())

coordsArray, position, collisions = changeLevel(initialPosition, initialCollisions, currentLevel, [])
position = setStuff(coordsArray, position)

maxLevel = 2
coins = 0

pos = coordsArray[0]
while True:
    didMove = False
    didAct = False
    availableMoves = ["w", "s", "a", "d"]
    actions = [["e", "Sword Swing"], ["o", "Open Chest"], ["q", "Shield"], ["z", "Save"]]
    checkActions = ["e", "o", "q", "z"]
    if "x" in position[0]:
        availableMoves.remove("w")
    if "x" in position[-1]:
        availableMoves.remove("s")

    for i in position:
        if "x" in i[1]:
            availableMoves.remove("a")
        if "x" in i[-2]:
            availableMoves.remove("d")

    if "x" in position[-1]:
        actions.remove(["e", "Sword Swing"])
        actions.remove(["q", "Shield"])
        checkActions.remove("e")
        checkActions.remove("q")
    elif position[pos[0] + 1][pos[1]] != "f":
        actions.remove(["e", "Sword Swing"])
        actions.remove(["q", "Shield"])
        checkActions.remove("e")
        checkActions.remove("q")
    
    if "x" in position[-1]:
        actions.remove(["o", "Open Chest"])
        checkActions.remove("o") 
    elif position[pos[0] + 1][pos[1]] != "y":
        actions.remove(["o", "Open Chest"])
        checkActions.remove("o")

        

    
    print(f"Coins: {str(coins)}")
    print(upAndDown)
    for el in position:
        print(' '.join(el))
    print(upAndDown)
    for moveX in availableMoves:
        print(f"Available Move: {moveX}")
    for actionX in actions:
        print(f"{actionX[1]}: {actionX[0]}")

    i = 1
    while True:
        try:
            action = input("Move: ")
        except KeyboardInterrupt:
            print("\nThanks For Playing")
            exit(0)
        if action in availableMoves:
            didMove = True
            break
        elif action in checkActions:
            didAct = True
            break
        else:
            iProv = checkRepetition(i)
            if iProv != None:
                i = iProv
            i = i + 1

    if didMove:
        position[pos[0]][pos[1]] = " "
        pos = move(action, pos)
        collisions = checkCollision(pos, collisions, coordsArray[1], coordsArray[2], coordsArray[3], coordsArray[4])
        if collisions["door"] == True:
            if (currentLevel + 1) != maxLevel:
                currentLevel = currentLevel + 1
                position[pos[0]][pos[1]] = " "
                coordsArray, position, collisions = changeLevel(position, collisions, currentLevel, coordsArray)
                position = setStuff(coordsArray, position)
                pos = coordsArray[0]
            else:
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
            sleep(0.2)
        collisions["chest"] = False
    elif didAct:
        sucsess, wdid = act(action, pos, position, coordsArray[4], str(currentLevel))
        if sucsess:
            if wdid == "kill": 
                position[pos[0] + 1][pos[1]] = "c"
                coordsArray[2].remove([pos[0] + 1, pos[1]])
                coordsArray[3].append([pos[0] + 1, pos[1]])
            elif wdid == "open":
                coins = coins + 5
                position[pos[0] + 1][pos[1]] = " "
                coordsArray[4].clear()
            elif wdid == "move":
               position[pos[0] + 1][pos[1]] = " " 
               position[pos[0] + 2][pos[1]] = "f"
               coordsArray[2].remove([pos[0] + 1, pos[1]])
               coordsArray[2].append([pos[0] + 2, pos[1]])
            elif wdid == "save":
                print("Saved Successfully")
                sleep(2.2)
        else:
            if wdid == "move":
                print("You tried to push me outside. It's not possible")
            elif wdid == "save":
                print("Error while saving")
                sleep(2.2)
    
    system(clearscreen())
    
print("Thanks For Playing")