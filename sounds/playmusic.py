#!/usr/bin/python3

import music
import pyglet

music = pyglet.resource.media('music/intro.ogg')
music.play()

def pause(self, symbol, modifiers):
    if symbol == key.m or symbol == key.M:
        self.pyglet.resource.media.music.pause()

pause = pause

pyglet.app.run()

while True:     

# Application events
    events = pyglet.resource.media
    for event in events:
        if event.type == QUIT:
                 QUIT()
