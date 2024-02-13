import json
import os

file_path = os.path.join(os.getcwd(), "Core/Questions/antigone.json")
print(file_path)
with open("/home/hacker/pr/new_game/Core/Questions/la_boite.json", 'r') as file:
    data = json.load(file)
    print("done")


