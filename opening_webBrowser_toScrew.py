import webbrowser
import time
import random

while True:

    websites = random.choice(["google.com","youtube.com","amazon.com"])

    visit = f"https://{websites}"

    webbrowser.open(visit)
    seconds = random.randrange(0,5)
    time.sleep(seconds)

