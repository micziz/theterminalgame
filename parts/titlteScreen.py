# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

# Import sleep to show messages for some time
from time import sleep
# Import system to run command to clear the screen
from os import system
# Import exits to check if a path exists
from os.path import exists

def titleSreen():
    system("clear")
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
        if exists("./ttgsave/save.txt"):
            print("2: Continue")
        choice = input(": ")
        if choice == "1":
            return 1
        elif choice == "2":
            if exists("./ttgsave/save.txt"):
                return 2