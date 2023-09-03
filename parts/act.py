def act(action, pos, position, chestPos):
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