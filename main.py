from pypresence import Presence
import time

# Create a Presence instance
vaimer = Presence(client_id="834822755752345611") 

# This method logs into your ID and starts the loop
vaimer.connect()

# This will be the place where all of the shit goes down
vaimer.update(state="GET FREE BOBUX",
              details="GET FREE ROBUX",
              large_image="aaamogus",
              buttons=[{"label": "CLAIM NOW",
                        "url":"https://youtu.be/dQw4w9WgXcQ" }] )

# This is the mainloop
while True:
    time.sleep(15)

