import sys

def checkRepetition(i):
    if i == 3:
        exitQ = input("DO YOU WANT TO EXIT? (y/n): ")
        if exitQ == "y":
            sys.exit(0)
        else:
            i = 0
            return i