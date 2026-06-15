import json

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
    with open("character.json","w") as file:
        json.dump(char,file)

def load_character():
    with open("character.json","r") as file:
        char_json = json.load(file)
    return char_json            

def print_character(char):
    print(f"Name: {char['name']}")                 
    print(f"level: {char['level']}")
    print("Skills:... ")
    for skill_name,skill_value in char['skills'].items():
        print(f" {skill_name}:{skill_value}")


print_character(character)
save_character(character)
loaded = load_character()
print(loaded)
