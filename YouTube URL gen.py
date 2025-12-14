#YT Vid URL Generator
import random
import time
from bs4 import BeautifulSoup
import requests

#req so far - bs4, requests
#time and rand are in python alr


availableSpace=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_")
vidID=("")
URL=("")
while True:
    vidID=(random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace) + random.choice(availableSpace))
    URL=("https://www.youtube.com/watch?v=" + (vidID))
    #known good, COMMENT OUT after test
    #URL=("https://www.youtube.com/watch?v=t-1x5bV8d7I")
    try:
        response=requests.get(URL)
        response.raise_for_status()
    except Exception as e:
        print(f"An unexpected exception occurred.")
    bsoup = BeautifulSoup(response.content, 'html.parser')
    realvidid = bsoup.title.get_text(separator=" ", strip=True)
    #test, COMMENT OUT
    #print(realvidid)
    isvalid=" - YouTube"
    if (isvalid) not in (realvidid):
        print ("Hit an invalid video ID, retrying...")
    else:
        print(URL)
        with open ("valid_YouTube_Video_IDs.txt", "a") as f:
            print((URL) + "\n", file=f)
    if ("https") in (realvidid):
        print ("Rate limited!!! Ending...")
        exit
    else:
        nothingburger=("i am a burger")
    print("Waiting until next try to stop rate limiting")
    #try to not get blocked or something like that with heuristics
    time.sleep (random.randint(0,1))
    
    
