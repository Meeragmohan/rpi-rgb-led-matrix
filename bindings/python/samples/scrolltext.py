#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import time

class ScrollText(SampleBase):
    def __init__(self, argtext, *displayparams):
        super(ScrollText, self).__init__(argtext, *displayparams)
        #print(displayparams)
        self.displaytext = argtext
        self.displayparams = displayparams
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

        # Configuration for the matrix
        self.options = RGBMatrixOptions()
        # use the input parameters to set the matrix options
        self.options.rows = self.displayparams[0]["rows"]
        self.options.cols = self.displayparams[0]["cols"]
        self.options.chain_length = 1
        self.options.hardware_mapping = 'adafruit-hat'
        self.options.brightness = self.displayparams[0]["brightness"]

        self.matrix = RGBMatrix(options=self.options)

    def run(self):  # Add the "self" parameter
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont(self.displayparams[0]["fontfile"])
        textColor = graphics.Color(self.displayparams[0]["redcolor"], self.displayparams[0]["greencolor"], self.displayparams[0]["bluecolor"])  # Close the opening parenthesis
        pos = offscreen_canvas.width
        dispText = self.displaytext
        print (dispText)

        if self.displayparams[0]["xposition"] == "center":
            x_pos = offscreen_canvas.width / 2
        elif self.displayparams[0]["xposition"] == "left":
            x_pos = self.displayparams[0]["xoffset"]
        elif self.displayparams[0]["xposition"] == "right":
            x_pos = offscreen_canvas.width - self.displayparams[0]["xoffset"]
        else:  # Default to middle
            x_pos = offscreen_canvas.width / 2

        if self.displayparams[0]["yposition"] == "middle":
            y_pos = (offscreen_canvas.height / 2) + (font.height / 4)
        elif self.displayparams[0]["yposition"] == "up":
            y_pos = offscreen_canvas.height - (font.height / 4)
        elif self.displayparams[0]["yposition"] == "down":
            y_pos = offscreen_canvas.height
        else:  # Default to middle
            y_pos = (offscreen_canvas.height / 2) + (font.height / 4)

        len = graphics.DrawText(offscreen_canvas, font, pos,  y_pos, textColor, dispText)

        for _ in range(len+offscreen_canvas.width):
            offscreen_canvas.Clear()
            #offscreen_canvas.brightness = 50
            len = graphics.DrawText(offscreen_canvas, font, pos,  y_pos, textColor, dispText)
            
            pos -= 1

            if (pos + len < 0):
                pos = offscreen_canvas.width
            time.sleep(0.01)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

