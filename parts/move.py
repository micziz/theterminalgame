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