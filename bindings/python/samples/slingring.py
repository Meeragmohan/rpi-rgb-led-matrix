import random
import re
import time
import scrolltext as scrolltext
import newsticker as Newsticker
import randomjoke as RandomJoke
import os
import glob
import scrollimage as ScrollImage
#import cricketscores as CricketScores
import weather as Weather
import currentdatetime as CurrentDateTime
import nationaltoday as NationalToday
import stockprices as StockPrices
import quotes as Quotes
import trivia as Trivia
import numbersapi as NumbersAPI
import countryfacts as CountryFacts
import cryptoprices as CryptoPrices
import wordoftheday as WordOfTheDay
import aviationinfo as AviationInfo
import movieposter as MoviePoster
import funfact as FunFact

#!/usr/bin/env python

basepath="/home/cyclops/Projects/rpi-rgb-led-matrix/bindings/python/samples/"
imagepath = "/home/cyclops/Projects/rpi-rgb-led-matrix/bindings/python/samples/images/"
flagpath="/home/cyclops/Projects/rpi-rgb-led-matrix/bindings/python/samples/flags/"
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
    txt = re.sub("\'", "'", disp)
    run_text = scrolltext.ScrollText(txt, displayparams)
    if not run_text.process():
        run_text.print_help()

def randomRGBColor(displayparams):
    displayparams["redcolor"] = random.randint(0,255)
    displayparams["greencolor"] = random.randint(0,255)
    displayparams["bluecolor"] = random.randint(0,255)

if __name__ == "__main__":

    scroll(displayparams, CurrentDateTime.get_current_datetime())
    random_movie=MoviePoster.get_random_movie(basepath)
    ScrollImage.ScrollImage(MoviePoster.get_movie_poster(random_movie['id'], basepath), displayparams).run()
    scroll(displayparams, "Movie: " + random_movie['title'])
    ScrollImage.ScrollImage(MoviePoster.get_movie_poster(random_movie['id'], basepath), displayparams).run()
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    #scroll(displayparams, AviationInfo.get_metar_data("KBNA,KSTL,KORD"))
    ScrollImage.ScrollImage(f"{imagepath}calendar.png", displayparams).run()
    scroll(displayparams, NationalToday.get_today_event())
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    ScrollImage.ScrollImage(f"{imagepath}stocks1.jpg", displayparams).run()
    scroll(displayparams, StockPrices.get_tinga_stock_prices(["TSLA", "NVDA", "AMZN", "MSFT", "TEAM"]))
    ScrollImage.ScrollImage(f"{imagepath}bitcoin.png", displayparams).run()
    scroll(displayparams, CryptoPrices.get_bitcoin_price_usd())
    ScrollImage.ScrollImage(f"{imagepath}joke.png", displayparams).run()
    scroll(displayparams, RandomJoke.get_random_joke(basepath))
    ScrollImage.ScrollImage(f"{imagepath}quote.png", displayparams).run()
    scroll(displayparams, Quotes.get_random_quote())
    ScrollImage.ScrollImage(f"{imagepath}funfact.png", displayparams).run()
    scroll(displayparams, FunFact.get_random_fact(basepath))
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    ScrollImage.ScrollImage(f"{imagepath}word.jpeg", displayparams).run()
    scroll(displayparams, WordOfTheDay.fetchWordOfTheDay())
    #scroll(displayparams, CricketScores.get_cricket_scores())
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    ScrollImage.ScrollImage(f"{imagepath}trivia.png", displayparams).run()
    scroll(displayparams, Trivia.generateTrivia(basepath))
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    ScrollImage.ScrollImage(f"{imagepath}math.jpeg", displayparams).run()
    scroll(displayparams, NumbersAPI.get_random_trivia(basepath))
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    ScrollImage.ScrollImage(f"{imagepath}country.png", displayparams).run()

    try:
        countryinfo=CountryFacts.print_random_country()
        countryflagname = countryinfo['country-name'].replace(" ", "-") 
        ScrollImage.ScrollImage(f"{flagpath}{countryflagname}.png", displayparams).run()
        scroll(displayparams, countryinfo["country-capital"])
        ScrollImage.ScrollImage(f"{flagpath}{countryflagname}.png", displayparams).run()
    except Exception as e:
        print(f"Error: {e}")

    ScrollImage.ScrollImage(f"{imagepath}weather.jpg", displayparams).run()
    scroll(displayparams, Weather.get_weather())
    scroll(displayparams, CurrentDateTime.get_current_datetime())
    ScrollImage.ScrollImage(f"{imagepath}bbc.png", displayparams).run()
    for disp in Newsticker.items:
        scroll(displayparams, disp)

    scroll(displayparams, CurrentDateTime.get_current_datetime())
    scroll(displayparams, CurrentDateTime.get_current_datetime())