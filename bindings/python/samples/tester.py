import random
import scrollimage as ScrollImage
import scrolltext as ScrollText
import os


direction="left" # 'left', 'right', 'up', 'down', 'no scroll', 'in', 'out'

textloopcount = 1 # Number of times to loop the text
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

# Get a list of all PNG files in the ./flags folder
png_files = [file for file in os.listdir("./flags") if file.endswith(".png")]

# Select a random PNG file from the list
random_png_file = random.choice(png_files)

# Complete the displayparams dictionary with the selected filename
displayparams["filename"] = f"./flags/{random_png_file}"
ScrollImage.ScrollImage(f"./flags/{random_png_file}", displayparams).run()
random_png_file = os.path.splitext(random_png_file)[0]
random_png_file = os.path.splitext(random_png_file)[0].replace("-", " ")
ScrollText.ScrollText(random_png_file, displayparams).run()