# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

# Import sleep to show messages for some time
from time import sleep
# Import system to run command to clear the screen
from os import system
# Import exits to check if a path exists
from os.path import exists

# Import system to check the platform
from platform import system as checkSys

# Function that returns the command to clear the screen based on platform
def clearscreen():
    # If the system is Linux or MacOS (darwin is MacOS's code)
    if (checkSys() == "Linux") or (checkSys() == "Darwin"):
        # The command is clear
        return "clear"
    # If it's windows
    elif checkSys() == "Windows":
        # The command is cls
        return "cls"
    # If nothing can be found, default to clear
    return "clear"

def titleSreen():
    system(clearscreen())
    print("""


          
                                    micziz Presents



    """)
    sleep(1.5)
    print("""


          
                                    The Terminal Game



    """)
    sleep(0.5)
    while True:
        print("1: New Game")
        if exists("./ttgsave/save.json"):
            print("2: Continue")
        choice = input(": ")
        if choice == "1":
            return 1
        elif choice == "2":
            if exists("./ttgsave/save.json"):
                return 2