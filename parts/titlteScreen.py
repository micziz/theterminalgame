import time, os

def titleSreen():
    os.system("clear")
    print("""


          
                                    micziz Presents



    """)
    time.sleep(1.5)
    print("""


          
                                    The Terminal Game



    """)
    time.sleep(0.5)
    while True:
        print("1: New Game")
        print("2: Continue (W.I.P)")
        choice = input(": ")
        if choice == "1":
            return 1