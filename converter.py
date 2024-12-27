import os
import json
from Utils import ReplaceChar


json_folder = r"JSON_Content"
try:
    json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]
    if not json_files:
        raise FileNotFoundError(".json files not found on specified path")
except FileNotFoundError as err:
    print(err)
    exit()


print("Select desired message log:")
for i, file in enumerate(json_files, start=1):
    print(f"{i}) {file}")


try:
    user_choice = int(input("Choose: "))
    selected_file = json_files[user_choice - 1]
except (ValueError, IndexError):
    print("Selección no válida.")
    exit()


MAINPATH = os.path.join(json_folder, selected_file)


try:
    with open(MAINPATH, encoding='latin1') as fh:
        data = json.load(fh)
except Exception as err:
    print(f"JSON file couldn't be read {err}")
    exit()


OverAllMessages = reversed(data["messages"])  

CumulativeResponse = ""
for message in OverAllMessages:
    if message.get('content') != None:
        CumulativeResponse = CumulativeResponse + f"{ReplaceChar(message.get('sender_name'))}: {ReplaceChar(message.get('content').encode('latin1').decode('utf-8'))}" + "\n"
    else:
        CumulativeResponse = CumulativeResponse + f"{ReplaceChar(message.get('sender_name'))}: " + '~Multimedia~' + "\n"


SavePath = r"Output.txt"
try:
    with open(SavePath, "w", encoding="utf-8") as f:
        f.write(CumulativeResponse)
except Exception as err:
    print(f"An error has ocurred. {err}")
