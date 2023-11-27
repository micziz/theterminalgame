# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

# Import system to check the platform
from platform import system

# Function that returns the command to clear the screen based on platform
def clearscreen():
    # If the system is Linux or MacOS (darwin is MacOS's code)
    if (system() == "Linux") or (system() == "Darwin"):
        # The command is clear
        return "clear"
    # If it's windows
    elif system() == "Windows":
        # The command is cls
        return "cls"
    # If nothing can be found, default to clear
    return "clear"