
# ! READ THISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# TODO: MAH MAN FOR THE LOVE OF GOD PLEASE MAKE A IF CLAUSE WHERE YOU PUSH VALUES IN THE ARRAY OF THE .UPDATE METHOD PLSSS DUDE

# TODO: Make error catching for json error
from json.decoder import JSONDecodeError
from typing import NamedTuple, cast
from pypresence import Presence
import time
import json
from colorama import Fore, init

try:
    with open("config.json", "r") as file:
        data = json.loads(file.read())
except JSONDecodeError:
    print("There seems to be a problem with the formatting of `Config.json`, Please check if there are any problems in the file formatting.")

# This chonky piece of code just gets all the values from the json
ID =  data["id"]
state = data["attributes"]["state"]
details = data["attributes"]["details"]
large_image = data["attributes"]["large_image"]
small_image = data["attributes"]["small_image"]
large_image_tooltip = data["attributes"]["large_image_tooltip"]
small_image_tooltip =  data["attributes"]["small_image_tooltip"]
b1_label =  data["button_attributes"]["button1"][0]["label"]
b1_url =  data["button_attributes"]["button1"][1]["url"]
b2_label = data["button_attributes"]["button2"][0]["label"]
b2_url = data["button_attributes"]["button2"][1]["url"]



# Create a Presence instance
client = Presence(client_id=ID)

# This method logs into your ID and starts the loop
client.connect()

b1_details = None if b1_label == "Placeholder" else b1_label
b1_link = None if b1_url == "Placeholder" else b1_url

b2_details = None if b2_label == "Placeholder" else b2_label
b2_link = None if b2_url == "Placeholder" else b2_url

# This will be the place where all of the stuff goes down
client.update(state=state,
              details=details,
              large_image=large_image,
              large_text=large_image_tooltip,
              buttons=[{"label": f"{b1_details}",
              			"url":f"{b1_link}"},
                          
                       {"label": f"{b2_label}",
                        "url": f"{b2_url}"
                       }]
)

# This is the mainloop
n = 0
print(Fore.RED + """                    

 ██▓███ ▓██   ██▓    ██▀███   ██▓███   ▄████▄  
▓██░  ██▒▒██  ██▒   ▓██ ▒ ██▒▓██░  ██▒▒██▀ ▀█  
▓██░ ██▓▒ ▒██ ██░   ▓██ ░▄█ ▒▓██░ ██▓▒▒▓█    ▄ 
▒██▄█▓▒ ▒ ░ ▐██▓░   ▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒
▒██▒ ░  ░ ░ ██▒▓░   ░██▓ ▒██▒▒██▒ ░  ░▒ ▓███▀ ░
▒▓▒░ ░  ░  ██▒▒▒    ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░ ░▒ ▒  ░
░▒ ░     ▓██ ░▒░      ░▒ ░ ▒░░▒ ░       ░  ▒   
░░       ▒ ▒ ░░       ░░   ░ ░░       ░        
         ░ ░           ░              ░ ░      
         ░ ░                          ░        
""" + Fore.RESET)

print("The presence is now online                Press ctrl+C to stop presence")
while True:
    try:
        n += 1
        time.sleep(15)

        print(f"Refreshed for the {n}th Time                Press ctrl+C to stop presence")
    except KeyboardInterrupt:
        client.close()
        print("Presence Stopped")
        exit()