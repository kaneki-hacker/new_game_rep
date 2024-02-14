# This is the file for the terminal version of the game

# Importing libraries
import random
from .antigone import Antigone
from .colors import ColorsPallet

class Terminalgame:
    def __init__(self, **kwargs) -> None:
        """This is the class responsible for creating an instance of the terminale version of the this game\nThis class takes kwargs that are used to access the questions that will be used for this game.\nIt can access the following aruments:\nantigone: is the argument that'll take the antigone class\nother will be added soon"""
        self.version = "1.0.0"
        self.colors = ColorsPallet()
        self.clean = kwargs["cleaner"]
        self.g_mode = 0
        self.health = 3
        self.player_err = list()
        self.game_questions = []
        self.load_questions(kwargs["antigone"])
        self.random_questions = []

    def load_questions(self, antigone_r: Antigone) -> None:
        self.game_questions = antigone_r.questions
        print(f"This just loaded all questions")
        return None

    def mode_random(self) -> None:
        ques = self.game_questions.copy()
        print(f"{self.colors.red('b')}Hello for the random mode{self.colors.color_reset()}")
        print("Tu va avoir the question suivant:")
        choosed_q1 = random.choice(ques)
        ques.remove(choosed_q1)
        print(f"{choosed_q1['q']}")
        if "ra" in choosed_q1:
            print(choosed_q1["a1"], choosed_q1["a2"])


    def mode_choice(self, part_choice:str) -> None:
        pass

    def game_mode(self) -> str:
        the_chosed = ""
        if self.g_mode == 1:
            print(f"The mode choosed is for random questions")
            the_chosed = "R"
            return the_chosed
        elif self.g_mode == 2:
            print(f"The mode choosed is for spicific questions")
            the_chosed = "S"
            return the_chosed
        else:
            print(self.game_questions)
            return the_chosed

    def game_controller(self) -> None:
        result = self.game_mode()
        if result == "":
            print("an error occured!")
        else:
            if result == "R":
                self.clean()
                self.mode_random()
            elif result == "S":
                print("specifique")
            else:
                print("something bad happened!")

    def starter(self):
        self.clean()
        print(f"{self.colors.blue('f')}Vous avez choisissé le terminal pour jouer le jeux!{self.colors.color_reset()}") 
        print(f"{self.colors.magenta('f')}On a deux mode de jeux valable pour maintenant\n1) Jouer avec des questions randomisez de tout le programme\n2) Jouer avec des questions sur un topic specifique, par example: avoir des questions sure le roman antigone seulement{self.colors.color_reset()}")
        try:
            g_choice = int(input(f"{self.colors.green('f')}Enter le choix que tu prefere (1 ou 2): {self.colors.color_reset()}"))
            self.g_mode = g_choice
            self.game_controller()
        except Exception as e:
            print(e)
