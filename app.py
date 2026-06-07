import ollama
import json

user_input = "i want to check flights available from Jhansi to Delhi for next Sunday"

response = ollama.chat(
    model='qwen2.5-coder:7b',
    messages=[
        {
            'role': 'user',
            'content': f"""Understand this user input: "{user_input}"

Divide it into these parts:
1. Mode of travel: write the mode mentioned by the user (bus, train, flight, etc.)
2. Time of travel: write the date, date with time, or words like next, upcoming, tomorrow, etc input by user.
3. Current location: write the proper location from which the user wants to travel
4. Destination: write the proper location where the user wants to go

Return the answer in JSON format only. Do not edit the user input, just divide it into parts."""
        }
    ],
    format="json"
)

main_agent = json.loads(response['message']['content'])

if main_agent.get('mode_of_travel') == "flight":
    print("Working")
else:
    print("not working")

print(json.dumps(main_agent, indent=4))