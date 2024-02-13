# This is the file responsible for the handling the questions of: antigone roman

# Importing libraries
import json
import os

q_a:dict = {"prologue": [
    {"chapter": 0,
     "questions": [
        {"q1": [
            {"Quel est le narrateur d'antigone?":"Jean Anouille"}
        ]},
        {"q2": [
            {"Quel est la soeur d'antigone?": "Isman"}
        ]},
     ]}
    ],
    "scene1":[
    {"chapter": 1,
    "questions":  [
        {"q1":[
            {"qs": "1"}
     ]},
     ],
     },
    ]
}

# Main class in the file
class Antigone:
    def __init__(self) -> None:
        self.questions = []
        self.antigone_q_path = os.path.join(os.getcwd(), "Core/Questions/antigone.json")
        self.load_all_questions()

    def load_all_questions(self) -> None:
        try:
            #with open(self.antigone_q_path) as file:
            #    data = json.load(file)
            all_chapt = []
            for element in q_a:
                all_chapt.append(element)
            for cha in all_chapt:
                self.questions.append(q_a[cha][0])
            #print(self.questions[0])
            #print(self.questions[1])

        except Exception as e:
            print(e)

if __name__ == "__main__":
    ant = Antigone()
    ant.load_all_questions()
    
    #ch = input("enter the good choice")
    #print(q_a[ch][0]["questions"])

