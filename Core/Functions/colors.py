# This file will contain the color pallete for the game

from colorama import Style, Fore, Back


class ColorsPallet:
    def __init__(self) -> None:
        self.err_choice = "A wrong argument have been passed!"
    
    def red(self, f_or_b: str) -> str:
        """This function will return the color red either for the background or the foreground\nIt takes one argument and it's: f_or_b: f for foreground color and b for background color"""
        if f_or_b == "f":
            return Fore.RED
        elif f_or_b == "b":
            return Back.RED
        else:
            print(self.err_choice)
            return ""

    def blue(self, f_or_b:str) -> str:
        """This function will return the color blue either for the background or the foreground\nIt take one argument\nf_or_b: f fore foreground color and b for background color"""
        if f_or_b == "f":
            return Fore.BLUE
        elif f_or_b == "b":
            return Back.BLUE
        else:
            print(self.err_choice)
            return ""

    def green(self, f_or_b: str) -> str:
        """This function will return the color green either for the background or the foreground\nIt takes one argument\nf_or_b: f for foreground color and b for background color"""
        if f_or_b == "f":
            return Fore.GREEN
        elif f_or_b == "b":
            return Back.GREEN
        else:
            print(self.err_choice)
            return ""

    def yellow(self, f_or_b: str) -> str:

        if f_or_b == "f":
            return Fore.YELLOW
        elif f_or_b == "b":
            return Back.YELLOW
        else:
            print(self.err_choice)
            return ""

    def magenta(self, f_or_b: str) -> str:
        
        if f_or_b == "f":
            return Fore.MAGENTA
        elif f_or_b == "b":
            return Back.MAGENTA
        else:
            print(self.err_choice)
            return ""   

    def black(self, f_or_b:str) -> str:
        if f_or_b == "f":
            return Fore.BLACK
        elif f_or_b == "b":
            return Back.BLACK
        else:
            print(self.err_choice)
            return ""

    def color_reset(self) -> str:
        return Style.RESET_ALL


