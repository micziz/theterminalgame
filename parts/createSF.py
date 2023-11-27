from os import mkdir
from os.path import isdir
from json import dumps

def createSF(level, coins):
    if isdir("./ttgsave") == True:
        with open("./ttgsave/save.json", "wt") as f:
            f.write(dumps({
                "level": level,
                "coins": coins
            }))
    else:
        mkdir("./ttgsave")
        with open("./ttgsave/save.json", "wt") as f:
            f.write(dumps({
                "level": level,
                "coins": coins
            }))