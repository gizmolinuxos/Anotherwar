#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyglet
import pyglet.window.key as key

# width of window,height of window : 1280x720 : 800x600
width = 800
height = 600

# caption i.e title of the window
title = "pyglet"

# creating a window
window = pyglet.window.Window(width, height, title)

# text
text = "Welcome to logo-pyglet"

# creating label:
# font = cooper
# position = 250, 230
# anchor position = center
label = pyglet.text.Label(text,
						font_name ='Cooper',
						font_size = 16,
						x = 350,
						y = 230,
						anchor_x ='center',
						anchor_y ='center')

# creating a batch
batch = pyglet.graphics.Batch()

# loading image
image = pyglet.image.load('logo.png')


# creating sprite object
# it is instance of an image displayed on-screen
sprite = pyglet.sprite.Sprite(image, x = 250, y = 250)

# on draw event
@window.event
def on_draw():
	
	# clear the window
	window.clear()
	
	# draw the label
	label.draw()
	
	# draw the image on screen
	sprite.draw()
	
# key press event	
@window.event
def on_key_press(symbol, modifier):

	# key "C" get press
	if symbol == key.C:
		
		# printing the message
		print("Key : C is pressed")
		
# image for icon
img = image = pyglet.resource.image("logo.png")

# setting image as icon
window.set_icon(img)

# getting resource location
value = pyglet.resource.location("logo.png")

# setting text of label
label.text = str(value)

# start running the application
pyglet.app.run()
