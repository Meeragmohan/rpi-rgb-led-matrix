import random
import re
import time
import scrolltext as scrolltext
import newsticker as Newsticker
import randomjoke as RandomJoke
import os
import glob
import imagescroller as ImageScroller
import cricketscores as CricketScores
import weather as Weather
import currentdatetime as CurrentDateTime
import nationaltoday as NationalToday
#import stockprices as StockPrices
import quotes as Quotes
import trivia as Trivia
import numbersapi as NumbersAPI
import countryfacts as CountryFacts
import cryptoprices as CryptoPrices
import wordoftheday as WordOfTheDay

#!/usr/bin/env python

textloopcount = 1 # Number of times to loop the text
direction="left" # 'left', 'right', 'up', 'down', 'no scroll', 'in', 'out'

xposition='center' # 'left', 'center', 'right'
yposition='middle' # 'up', 'middle', 'down'
xoffset=0 # Offset from xposition
yoffset=0 # Offset from yposition
startingxposition=0 # Starting x position
startingyposition=0 # Starting y position

fontfile="/home/cyclops/Projects/rpi-rgb-led-matrix/fonts/7x14.bdf" # Font file

# Create a dictionary with the variables
displayparams = {
    "textloopcount": textloopcount,
    "direction": direction,
    "redcolor": random.randint(0,255),
    "greencolor": random.randint(0,255),
    "bluecolor": random.randint(0,255),
    "rows":32,
    "speed": 5,
    "cols": 64,
    "brightness": 100,
    "xposition": xposition,
    "yposition": yposition,
    "xoffset": xoffset,
    "yoffset": yoffset,
    "startingxposition": startingxposition,
    "startingyposition": startingyposition,
    "fontfile": fontfile
}

# Create an instance of Newsticker
Newsticker.populateItems()
print(Newsticker.items)

#CricketScores.get_cricket_scores()
#print(CricketScores.scores)

def scroll(displayparams, disp):
    time.sleep(0.5)
    randomRGBColor(displayparams)
    scrolltext.ScrollText(disp, displayparams)
    txt = re.sub("'", "\\'", disp)
    run_text = scrolltext.ScrollText(txt, displayparams)
    if not run_text.process():
        run_text.print_help()

def randomRGBColor(displayparams):
    displayparams["redcolor"] = random.randint(0,255)
    displayparams["greencolor"] = random.randint(0,255)
    displayparams["bluecolor"] = random.randint(0,255)

if __name__ == "__main__":

    scroll(displayparams, CurrentDateTime.get_current_datetime())
    #scroll(displayparams, StockPrices.get_stock_prices(["TSLA", "NVDA", "AMZN", "MSFT"]))
    scroll(displayparams, CryptoPrices.get_bitcoin_price_usd())
    scroll(displayparams, RandomJoke.get_random_joke())
    scroll(displayparams, Quotes.get_random_quote())
    scroll(displayparams, WordOfTheDay.fetchWordOfTheDay())
    #scroll(displayparams, CricketScores.get_cricket_scores())
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    scroll(displayparams, Trivia.generateTrivia())
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    scroll(displayparams, NumbersAPI.get_random_trivia())
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    scroll(displayparams, CountryFacts.print_random_country())
    scroll(displayparams, Weather.get_weather())
    scroll(displayparams, NationalToday.get_today_event())
    scroll(displayparams, CurrentDateTime.get_current_datetime())

    for disp in Newsticker.items:
        scroll(displayparams, disp)

    # Get a list of all PNG files in the ./flags folder
    #png_files = glob.glob("./flags/*.png")

    # Select a random PNG file
    #random_png = random.choice(png_files)

    # Display the random PNG file using ImageScroller class from image-scroller.py
    #image_scroller = ImageScroller(displayparams)
    #image_scroller.display_image(random_png)