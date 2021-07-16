from pypresence import Presence
import time
import json

with open("config.json", "r") as file:
    data = json.loads(file.read())

# This chonky piece of code just gets all the values from the json so dont freak out in here
ID =  data["id"]
state = data["attributes"]["state"]
details = data["attributes"]["details"]
large_image = data["attributes"]["large_image"]
small_image = data["attributes"]["small_image"]
large_image_tooltip = data["attributes"]["large_image_tooltip"]
small_image_tooltip =  data["attributes"]["small_image_tooltip"]
label =  data["button_attributes"]["button1"][0]["label"]
url =  data["button_attributes"]["button1"][1]["url"]



# Create a Presence instance
client = Presence(client_id=ID) 

# This method logs into your ID and starts the loop
client.connect()

# This will be the place where all of the stuff goes down
client.update(state=state,
              details=details,
              large_image=large_image,
              large_text=large_image_tooltip,
              buttons=[{"label": f"{label}",
              			"url":rf"https://github.com/Vaimer9/py-rpc"}]
)
print("The presence is now online")
# This is the mainloop
while True:
    time.sleep(15)
    print("Refreshed")
