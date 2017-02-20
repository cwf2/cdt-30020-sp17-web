#!/usr/bin/env python
'''draw a snow-covered mountain'''

# imports
from drawit import Point, Color, Image, PPM, MPImage
import random

# set colors
SKY =       # TODO pick color
MOUNTAIN =  # TODO  "     "
SNOW =      # TODO  "     "

# create the canvas
image =     # TODO create a new image

# draw sky
# TODO draw a rectangle in sky color, filling the image

# draw mountain
peak =      # TODO a new point
for x in    # TODO iterate over all x values
    base_point =  # TODO a point along the bottom of the image
    # TODO draw a line from peak to base_point in mountain color
# TODO draw a circle in sky color to "bite" off the peak

# add snow
for x in      # TODO iterate over all x values
    for y in  # TODO iterate over all y values
        p =   # TODO a new point at x,y
        if    # TODO is the pixel at p equal to mountain color?
            if    # TODO is a random number between 0 and y equal to 0?
                  #       hint: use random.randint(lower, upper)
                  
                # TODO set pixel at p to snow color

# write the image
PPM.write(image, "mountain.ppm")
MPImage.write_png(image, "mountain.png")

