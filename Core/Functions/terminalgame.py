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
        self.tries = 0
        self.player_err = list()
        self.game_questions = []
        self.load_questions(kwargs["antigone"])
        self.random_questions = []

    def load_questions(self, antigone_r: Antigone) -> None:
        self.game_questions = antigone_r.questions
        print(f"This just loaded all questions")
        return None

    def mode_random(self) -> None:
        self.tries += 1
        if self.tries == 1:
            self.random_questions = self.game_questions.copy()
        print(f"\n{self.colors.red('b')}Hello for the random mode{self.colors.color_reset()}")
        print("Tu va avoir the question suivant:")
        choosed_q:dict = random.choice(self.random_questions)
        self.random_questions.remove(choosed_q)
        print(f"{self.colors.magenta('f')}{choosed_q['q']}{self.colors.color_reset()}")
        if "ra" in choosed_q:
            index = 0
            for i in choosed_q:
                if i == "q" or i == "ra":
                    index += 1
                else:
                    print(f"{self.colors.blue('f')}{index}){self.colors.color_reset()}{self.colors.yellow('f')} {choosed_q[i]}{self.colors.color_reset()}")
                    index += 1
            del index
            try:
                u_an = int(input(f"{self.colors.green('f')}Enter le nombre de la bonne reponse: {self.colors.color_reset()}"))
                if self.check_sol_for_qcm(choosed_q, u_an):
                    print(f"{self.colors.green('f')}Bravo!!!{self.colors.color_reset()}")
                    self.mode_random()
                else:
                    print("wrong solution")
            except Exception as e:
                print(e)
        else:
            try:
                res = str(input(f"{self.colors.green('f')}Enter votre reponse: {self.colors.color_reset()}"))
                if self.check_sol_for_inputed_data(choosed_q, res) == True:
                    print(f"{self.colors.blue('f')}Bravo!!!{self.colors.color_reset()}")
                else:
                    print(f"{self.colors.red('f')}Dommage votre repose est fausse!{self.colors.color_reset()}")
            except Exception as e:
                print(e)

    def check_sol_for_inputed_data(self, q: dict, r: str) -> bool:
        if "a" in q:
            if q["a"] == r:
                print('yup')
                return True
            else:
                print("nope")
                return False
        else:
            return False

    def check_sol_for_qcm(self, q:dict, r:int) -> bool:
        if "ra" in q:
            #print(q["ra"])
            if str(r) in q["ra"]:
                return True
            else:
                return False
        else:
            print("yup another problem")
            return False
        

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


