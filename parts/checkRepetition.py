# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

# Import exit from sys to exit if the user asks to.
from sys import exit

def checkRepetition(i):
    if i == 3:
        exitQ = input("DO YOU WANT TO EXIT? (y/n): ")
        if exitQ == "y":
            exit(0)
        else:
            i = 0
            return i