#!/bin/sh

echo " DOWNLOADING GAME DEPENDANTS --- Python3 and Pip3 Are Main Requirments... "
sleep 4

# Download Python ( Remove # copy/paste or enter commands )
sudo apt-get install --upgrade -y python3

sleep 4

# Install Modules
pip install --upgrade pip pyglet pygame pygame-menu pyopengl transmitter cython nested numpy leveldb pillow opensimplex PyShaders tqdm pyglm ratcave glfw

# Download Tkinter ( Remove # copy/paste or enter commands )
sudo apt-get install -y python3-tk

echo " Done with that... "
sleep 2
