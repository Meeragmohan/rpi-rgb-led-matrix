import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# Set up the RGB matrix options
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # Change this if needed

# Create the RGB matrix
matrix = RGBMatrix(options=options)

# Create a canvas to draw on
canvas = matrix.CreateFrameCanvas()

# Set the font and color for the text
font = graphics.Font()
font.LoadFont("../../../fonts/7x14.bdf")  # Replace with the path to your font file
color = graphics.Color(127, 255, 127)  # Replace with your desired color

# Get the input text from the user
text = input("Enter the text to display: ")

# Calculate the width of the text
text_width = graphics.DrawText(canvas, font, 0, 0, color, text)

# Set the initial position of the text
x = matrix.width

# Loop to scroll the text
while True:
    # Clear the canvas
    canvas.Clear()

    # Draw the text at the current position
    graphics.DrawText(canvas, font, x, 16, color, text)

    # Update the position of the text
    x -= 1

    # If the text has scrolled off the screen, reset the position
    if x + text_width < 0:
        x = matrix.width

    # Swap the canvas to the matrix
    canvas = matrix.SwapOnVSync(canvas)

    # Delay for a short period to control the scrolling speed
    time.sleep(0.05)