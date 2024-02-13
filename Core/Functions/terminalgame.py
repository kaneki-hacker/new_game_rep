# This is the file for the terminal version of the game

# Importing libraries
import random
from .colors import ColorsPallet

class Terminalgame:
    def __init__(self, **kwargs) -> None:
        """This is the class responsible for creating an instance of the terminale version of the this game\nThis class takes kwargs that are used to access the questions that will be used for this game.\nIt can access the following aruments:\n"""
        self.version = "1.0.0"
        self.colors = ColorsPallet()
        self.g_mode = 0
        self.health = 3
        self.player_err = list()

    def load_questions(self):
        pass

    def mode_random(self) -> None:
        pass

    def mode_choice(self, part_choice:str) -> None:
        pass

    def game_mode(self) -> None:
        pass

    def game_controller(self) -> None:
        pass

    def starter(self):
        print(f"{self.colors.blue('f')}Vous avez choisissé le terminal pour jouer le jeux!{self.colors.color_reset()}") 
        print(f"{self.colors.magenta('f')}On a deux mode de jeux valable pour maintenant\n1) Jouer avec des questions randomisez de tout le programme\n2) Jouer avec des questions sur un topic specifique, par example: avoir des questions sure le roman antigone seulement{self.colors.color_reset()}")
        try:
            g_choice = int(input(f"{self.colors.green('f')}Enter le choix que tu prefere (1 ou 2): {self.colors.color_reset()}"))
            self.g_mode = g_choice

        except Exception as e:
            print(e)
