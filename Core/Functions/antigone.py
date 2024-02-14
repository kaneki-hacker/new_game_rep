# This is the file responsible for the handling the questions of: antigone roman

# Importing libraries
import json
import os

# Main class in the file
class Antigone:
    def __init__(self) -> None:
        self.questions = []
        self.antigone_q_path = os.path.join(os.getcwd(), "Core/Questions/antigone.json")
        self.load_all_questions()

    def load_all_questions(self) -> None:
        try:
            with open(self.antigone_q_path) as f:
                data = json.load(f)
            qu=[]
            for el in data:
                #print(data[el]["chapter"])
                qu.append(data[el]["questions"])
            for element in qu:
                for k in element:
                    if element[k] != {} and element[k]["q"] != "":
                        self.questions.append(element[k])
            #print(self.questions)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    ant = Antigone()
    #ant.load_all_questions()
    
    #ch = input("enter the good choice")
    #print(q_a[ch][0]["questions"])

