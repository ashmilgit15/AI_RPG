import json
import os
from core.ai_update import get_skill_activity


filename = "/home/ashmilp/Documents/AI_RPG/data/character.json"
name = "Ashmil"
level = 0

character = {
    "name":name,
    "level":level,
    "skills":{
        "python":0,
        "discipline":0,
    },
    "achievements":[],

}


def save_character(char):
    with open(filename,"w") as file:
        json.dump(char,file)

def load_character():
    with open(filename,"r") as file:
        char_json = json.load(file)
    return char_json            

  

def print_character(char):
    print(f"Name: {char['name']}")                 
    print(f"level: {char['level']}")
    print("Skills:... ")
    for skill_name,skill_value in char['skills'].items():
        print(f" {skill_name}:{skill_value}")




def apply_update(character,update):
    for key,value in update.items():
        for skill in character["skills"]:
            if skill == key:
                character["skills"][key] += value
                print(f"skill updated: {key} +{value}")

    save_character(character)            

if __name__ == "__main__":

    if os.path.exists("/home/ashmilp/Documents/AI_RPG/data/character.json"):
        character = load_character()
    else:
        save_character(character)  
    activity = input("What did you do today?: ")
    update = get_skill_activity(activity,character)
    print(f"AI says: {update['reason']}")
    apply_update(character, update)
    print_character(character)

# print_character(character)
# save_character(character)
# loaded = load_character()
# print(loaded)
