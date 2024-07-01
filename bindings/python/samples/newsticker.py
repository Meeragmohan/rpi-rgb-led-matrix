# THIS SCRIPT USES THE LIBRARY AT:
# https://github.com/hzeller/rpi-rgb-led-matrix

import os, time, threading, random
import feedparser
import re
from random import shuffle

BITLY_ACCESS_TOKEN="BITLY_ACCESS_TOKEN"
items=[]
displayItems=[]
feeds=[
    #enter all news feeds you want here
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "http://feeds.bbci.co.uk/news/world/rss.xml"
    #"http://feeds.reuters.com/reuters/topNews",
    #"https://www.npr.org/rss/rss.php?id=1001",
    #"http://feeds.feedburner.com/ndtvnews-latest"
    #"https://markets.businessinsider.com/rss/news",
    #"https://www.cio.com/index.rss"
    ]

def colorRandom():
    return str(random.randint(0,255)) + "," + str(random.randint(0,255))  + "," + str(random.randint(0,255))

def populateItems():
    #first clear out everything

    del items[:]
    del displayItems[:]

    feeds=[
        #enter all news feeds you want here
        #"https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "http://feeds.bbci.co.uk/news/world/rss.xml"
        #"http://feeds.reuters.com/reuters/topNews",
        #"https://www.npr.org/rss/rss.php?id=1001",
        #"http://feeds.feedburner.com/ndtvnews-latest"
        #"https://markets.businessinsider.com/rss/news",
        #"https://www.cio.com/index.rss"
    ]

    for url in feeds:
        feed=feedparser.parse(url)
        print(feed["feed"]["title"])
        items.append("" + feed["feed"]["title"])
        print(feed["feed"]["title"]) 
        posts=feed["items"]
        for post in posts:
            items.append(post["title"]+": "+post["summary"])
            #print(post["title"]+": "+post["summary"])
    # shuffle(items)

def run():
    print("News Fetched at {}\n".format(time.ctime()))
    populateItems()
    # threading.Timer(len(items) * 60, run).start()
    showOnLEDDisplay()

def showOnLEDDisplay():
    for disp in items[:60]:
        txt=re.sub("'","\\'",disp)
        cmd="sudo /home/cyclops/Projects/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-rows=32 --led-cols=64 -f /home/cyclops/Projects/rpi-rgb-led-matrix/fonts/7x14.bdf -s 14 -l 1 --led-gpio-mapping=adafruit-hat  --led-no-hardware-pulse --led-slowdown-gpio=4 -C "+ colorRandom() +" '"+txt+"'"
        os.system(cmd)

if __name__ == '__main__':
    run()
