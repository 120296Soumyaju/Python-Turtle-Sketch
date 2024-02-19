from turtle import title

from sketchpy import canvas as gfg

title("Rajmudra")
img = gfg.sketch_from_image("F:\\Python Turtle Sketch\\Chattrapati Shivaji Maharaj\\Swarajya.jpg")
img.draw(threshold=150)
# Here the threshold value is the parameter that is used based on the user's choice