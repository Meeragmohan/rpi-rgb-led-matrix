#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.brightness = 100
options.hardware_mapping = 'adafruit-hat' # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Make image fit our screen.
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# print (image.width, image.height)

# Calculate the offset to center the image
offset_x = (matrix.width - image.width) // 2
offset_y = (matrix.height - image.height) // 2

# Set the image on the matrix with the calculated offset
matrix.SetImage(image.convert('RGB'), offset_x, offset_y)

#matrix.SetImage(image.convert('RGB'),0,10)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
