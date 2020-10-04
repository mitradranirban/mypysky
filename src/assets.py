# file to load necessary assets for running game 
#/usr/bin/env python3
try:

    import sys

    import random

    import math

    import os

    import getopt

    import pygame
    
    import pygame.truetype 

    from socket import *

    from pygame.locals import *

except ImportError, err:

    print "couldn't load module. %s" % (err)

    sys.exit(2)
    
    def load_sound(name):
    """ Load sound object"""
    fullname = os.path.join('sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)

    except pygame.error, message:
        print 'Cannot load sound file:', fullname
        raise SystemExit. message
    return sound.play()
        
       def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()
