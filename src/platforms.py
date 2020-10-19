"""
Module for managing platforms.
"""
import pygame
import os 
# import assets
import constants

def load_image(self, width, height):
        """ load a single image from image folder and make a pygame sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Load the sprite from images folder
        pygame.image.load(os.path.join('images',image)).convert()

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image



GRASS = 'grass.png'
STONE = 'stone.png'
ICE = 'ice.png'
SAND = 'sand.png'
CLOUD = 'cloud.png'
MANTA = 'manta.png'
JELLYFISH = 'jellyfish.png'
 

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, xlocation, ylocation, imagewidth, imageheight, image):
        """ Platform constructorfrom individual images. """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('images',image)).convert()
        self.image.set_colorkey(constants.BLACK)                                   
        self.rect = self.image.get_rect()
        self.rect.y = ylocation
        self.rect.x = xlocation


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1

class loot(Platform):
    level = None
    player = None
