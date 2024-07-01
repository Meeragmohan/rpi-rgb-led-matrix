#!/usr/bin/env python
import time
import sys

from samplebase import SampleBase
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image


class ScrollImage(SampleBase):
    def __init__(self, image_file, *displayparams):
        super(ScrollImage, self).__init__(image_file, *displayparams)
        #print(displayparams)
        self.displayparams = displayparams

        self.image = Image.open(image_file)

        # Configuration for the matrix
        self.options = RGBMatrixOptions()
        # use the input parameters to set the matrix options
        self.options.rows = self.displayparams[0]["rows"]
        self.options.cols = self.displayparams[0]["cols"]
        self.options.chain_length = 1
        self.options.hardware_mapping = 'adafruit-hat'
        self.options.brightness = self.displayparams[0]["brightness"]

        self.matrix = RGBMatrix(options=self.options)
        self.image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

    def run(self):  # Add the "self" parameter
        if self.displayparams[0]["xposition"] == "center":
            x_pos = self.matrix.width / 2
        elif self.displayparams[0]["xposition"] == "left":
            x_pos = self.displayparams[0]["xoffset"]
        elif self.displayparams[0]["xposition"] == "right":
            x_pos = self.matrix.width - self.displayparams[0]["xoffset"]
        else:  # Default to middle
            x_pos = self.matrix.width / 2

        if self.displayparams[0]["yposition"] == "middle":
            y_pos = (self.matrix.height / 2) + (self.image.height / 4)
        elif self.displayparams[0]["yposition"] == "up":
            y_pos = self.matrix.height - (self.image.height / 4)
        elif self.displayparams[0]["yposition"] == "down":
            y_pos = self.matrix.height
        else:  # Default to middle
            y_pos = (self.matrix.height / 2) + (self.image.height / 4)

        # Calculate the offset to center the image
        offset_x = (self.matrix.width - self.image.width) // 2
        offset_y = (self.matrix.height - self.image.height) // 2
        dispImage = self.image.convert('RGB')
        for i in range(self.matrix.width + self.image.width):
            offset_x = i - self.image.width
            self.matrix.SetImage(dispImage, offset_x, offset_y)
            time.sleep(0.02)
        
        offset_x = (self.matrix.width - self.image.width) // 2
        for i in range(self.matrix.height + self.image.height):
            offset_y = i - self.image.height
            self.matrix.SetImage(dispImage, offset_x, -offset_y)
            time.sleep(0.04)