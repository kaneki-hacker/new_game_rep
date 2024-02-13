# This file will be handling the gui version of the game

# Importing libraries
import tkinter as tk 
import customtkinter as ctk 

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x1000")
        self.main_frame = ctk.CTkFrame
        self.title("French Game")

    def starter(self):
        self.mainloop()

# This next part is used for testing only
if __name__ == "__main__":
    app = App()
    app.starter()

