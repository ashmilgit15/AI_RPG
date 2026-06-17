import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")


# name = "Ashmil"
# level = 0

# character = {
#     "name":name,
#     "level":level,
#     "skills":{
#         "python":0,
#         "discipline":0,
#     },
#     "achievements":[],

# }

# print(response["choices"][0]["messages"]["content"])


def get_skill_activity(activity,character):
    prompt = f"""
                You are an RPG game master. A player did this activity: "{activity}".
                Their current skills are: {character["skills"]}.
                Return ONLY a JSON object with skill point increases. Example: {{"python": 3, "discipline": 1, "reason": "..."}}
                No explanation, no markdown, just raw JSON.
                                                            """
    


    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
    },
    data=json.dumps({
        "model":"nex-agi/nex-n2-pro:free",
        "messages": [
        {
            "role": "user",
            "content": prompt,
        }
        ]
    })
    )

    data = response.json()

    reply_str = data["choices"][0]["message"]["content"]

    ai_msg_in_json_dict = json.loads(reply_str)

    return ai_msg_in_json_dict

# result = get_skill_activity("practiced python for 2 hours",character)
# print(result)
# print(type(result))




