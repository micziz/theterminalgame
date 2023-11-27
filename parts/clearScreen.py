# Copyright 2023-Present Micziz. Licensed under the MIT license. More info in the LICENSE file!

# Import system to check the platform
from platform import system

def clearscreen():
    if (system() == "Linux") or (system() == "Darwin"):
        return "clear"
    elif system() == "Windows":
        return "cls"