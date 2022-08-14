#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyglet
import sounds.music
import data.assets
from data.graphics import *
from data.scenemanager import SceneManager
from data.controllers import Controllers

# Start the Server
"import net"

def main():
    # The pyglet.resource module handles efficient loading of assets:
    # Setup the main music
    # "Errors with Asstes or Sounds,need fixed below... "
    pyglet.resource.path = ['data/assets', 'sounds/music', 'sounds/main']
    pyglet.resource.reindex()
    music = pyglet.resource.media('intro.ogg')
    music.play()

    # Create the main game Window, and set it's icon:
    config = Config(alpha_size=ALPHA_SIZE, double_buffer=DOUBLE_BUFFER)
    window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption=TITLE,
                                  resizable=RESIZABLE, fullscreen=FULLSCREEN, vsync=VSYNC)
    window.set_icon(pyglet.resource.image('logo.png'))

    # Create an instance of the SceneManager, and schedule it to update:
    scene_manager = SceneManager(window=window)
    pyglet.clock.schedule_interval(scene_manager.update, 1.0 / TICKS_PER_SEC)

    # Setup some OpenGL settings (from data.game.settings.graphics,Opengl), and start the game loop:
    setup_opengl()

# "If Errors with Gstreamer bus,you need to fix below... "
    "Gst.Bus.async_signal_func ()"
    "gobject.Mainloop()"
    pyglet.app.run()

if __name__ == '__main__':
    main()
