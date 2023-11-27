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
        if os.path.exists("./ttgsave/save.txt"):
            print("2: Continue")
        choice = input(": ")
        if choice == "1":
            return 1
        elif choice == "2":
            if os.path.exists("./ttgsave/save.txt"):
                return 2