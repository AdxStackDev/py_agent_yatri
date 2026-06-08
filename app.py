import ollama
import json
import datetime

import travel_agent

user_input = "i want to check flights available from Jhansi to Delhi for next Sunday."

response = ollama.chat(
    model='qwen2.5-coder:7b',
    messages=[
        {
            'role': 'user',
            'content': f"""Understand this user input: "{user_input}"

Divide it into these parts:
1. mode_of_travel: write the mode mentioned by the user (bus, train, flight, etc.). It could be multiple.
2. time_of_travel: write the date, date with time, or words like next, upcoming, tomorrow, etc input by user. It could be multiple.
3. current_location: write the proper location from which the user wants to travel. It could be multiple.
4. destination: write the proper location where the user wants to go. It could be multiple. 

Return the answer in JSON format only. Do not edit the user input, just divide it into parts."""
        }
    ],
    format="json"
)

main_agent = json.loads(response['message']['content'])

check_travel = main_agent.get('mode_of_travel')

if check_travel:
    print (travel_agent.checkMedium(check_travel))
# print(json.dumps(main_agent, indent=4))

response_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"{response_time}.json"

with open(file_name, "w", encoding="utf-8") as file:
    json.dump(main_agent, file, indent=4)

print ("response saved")
