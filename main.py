#! /usr/bin/python3.11

#
# This is the main file for the game code
#

# Importing the used libraries
import sys
import os
from typing import Never, NoReturn
from Core.Functions.Intro import Intro

# Other functionnalities for the game
def clean() -> None:
    os.system("clear")

# The main file function
def main() -> None:
    clean()
    intro = Intro(cleaner=clean)
    intro.start()

# The main code entry
if __name__ == "__main__":
    main()
    sys.exit()

