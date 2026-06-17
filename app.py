from flask import Flask,jsonify
from core.character import load_character

app = Flask(__name__)

@app.route("/")
def home():
    return "Life RPG is running"

@app.route("/character")
def character_load():
    character_dict = load_character()
    character_json = jsonify(character_dict)
    return character_json

if __name__ == "__main__":
    app.run(debug=True)

