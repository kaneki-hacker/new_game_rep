# This file is used for handling the game opening and different types of game

# Importing the libraries
from typing import NoReturn
from .antigone import Antigone
from .terminalgame import Terminalgame
from .gui import App
from .colors import ColorsPallet

class Intro:
    def __init__(self) -> None:
        """This is the class used to handle the different game opening and modes and other stuff hehe"""
        self.game_mode_c = "T"
        self.colors = ColorsPallet()
        self.game_controller = None
        self.antigone_questions = Antigone()

    def handle_game_type(self, choice: int) -> None:
        if choice == 1:
            self.game_mode_c = "T"
        elif choice == 2:
            self.game_mode_c = "G"
        else:
            print("An error occured while choosing the game type!")
        return None

    def game_mode(self) -> None:
        if self.game_mode_c == "T":
            print("using terminal")
            self.game_controller = Terminalgame(antigone=Antigone())
        elif self.game_mode_c == "G":
            print("using gui app")
            self.game_controller = App(antigone=Antigone())
        else:
            print("sorry something that we have no idea about just occured!")

    def game_started(self) -> None:
        try:
            self.game_controller.starter()
        except Exception as e:
            print(e)

    def start(self):
        """This is the start of this function it's used to start the game and handle other things during the game"""
        print(f"{self.colors.magenta('f')}Bonjour!{self.colors.color_reset()}")
        print(f"{self.colors.red('f')}On a deux mode pour jouer\nLe premier: (1) pour jouer en terminal ou cette instant de jeux que tu vois le jeux a commancer avec\nLe deuxieme: (2) pour ouvrir l'application de desktop pour jouer(L'application desktop est en beta mode, il peux avoir des problems!){self.colors.color_reset()}")
        try:
            first_choice = int(input(f"{self.colors.green('f')}Maintenant choisir le mode de jeux que tu veux (1 ou 2): {self.colors.color_reset()}"))
            self.handle_game_type(first_choice)
            self.game_mode()
            self.game_started()
        except Exception as e:
            print(e)
        

