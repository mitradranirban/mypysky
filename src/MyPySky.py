"""
MyPySky Pygame Programs
Simpson College Computer Science

Main module for platform scroller.

Modified from:
http://programarcadegames.com/python_examples/sprite_sheets/

"""

import pygame
from pygame.locals import *
import os


# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)

# Screen dimensions
SCREEN_WIDTH  = 1054
SCREEN_HEIGHT = 594
TILEX = 100
TILEY = 100

class Player(pygame.sprite.Sprite):
    """ This class represents the player at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0



    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None
    loot_list = pygame.sprite.Group()

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

       
        # Load all the right facing images into a list
        for i in range(1,9):
            image = pygame.image.load(os.path.join('images','child'+str(i)+'.png'))
            self.walking_frames_r.append(image)


        # Load all the right facing images, then flip them
        # to face left.
        for i in rangei(1,9)
            :mage = pygame.image.load(os.path.join('images','child'+str(i)+'.png'))
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)


        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        # Set Baseline score, health and collide delta 

        self.health = 10
        self.damage = 0
        self.collide_delta = 0
        self.jump_delta = 6
        self.score = 1
        
    def update(self
        """ Move the player. """
        # Gravity
     

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # see if we collect any star
        loot_hit_list = pygame.sprite.spritecollide(self, self.loot_list, False)
        for loot in loot_hit_list:
            self.loot_list.remove(loot)
            self.score += 1
        

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
    

""" Module for managing platforms. """


def load_image(self, width, height):
        """ load a single image from image folder and make a pygame sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Load the sprite from images folder
        pygame.image.load(os.path.join('images',image)).convert()

        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)

        # Return the image
        return image



GRASS = 'grass.png'
STONE = 'stone.png'
ICE = 'ice.png'
SAND = 'sand.png'
CLOUD = 'cloud.png'
MANTA = 'manta.png'
JELLYFISH = 'jellyfish.png'
CANDLE = 'candle.png'
 

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, xlocation, ylocation, imagewidth, imageheight, image):
        """ Platform constructorfrom individual images. """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('images',image)).convert()
        self.image.set_colorkey(BLACK)                                   
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

class Level():

    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    loot_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.loot_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.loot_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.loot_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for loot in self.loot_list:
            loot.rect.x += shift_x 
    

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
       
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"home.png")).convert()
        self.background.set_colorkey(WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [GRASS, 400, 500],
                  [SAND, 528, 500],
                  [STONE, 640, 500],
                  [ICE, 800, 400],
                  [ICE, 900, 400],
                  [STONE, 1200,500],
                  [STONE, 1400,500],
                  [STONE, 1600,500],
                  [STONE, 1900,500]
                   ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[1],platform[2], TILEX, TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        

      


# Create platforms for the level 2
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"isle.png")).convert()
        self.background.set_colorkey( BLUE)
        self.level_limit = -2600

        # Array with type of platform, and x, y location of the platform.
        level = [ [  STONE, 500, 550 ],
                  [  STONE, 600, 450],
                  [  STONE, 700, 350],
                  [  SAND, 900, 450],
                  [  STONE, 1100, 300],
                  [  STONE, 1300, 280],
                  [  STONE, 1650, 280],
                  [  GRASS, 1750, 400],
                  [  GRASS, 1850, 450]]


        # Go through the array above and add platforms
        for platform in level:
            block =   Platform(platform[1],platform[2], TILEX, TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block =   MovingPlatform(1350,280, TILEX, TILEY,  CLOUD)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add loot
        level = [ [  CANDLE, 700, 300],
                  [  CANDLE, 1700, 300]
                 ]
        for platform in level:
            block =   Platform(platform[1],platform[2], TILEX, TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.loot_list.add(block)        

  

# Create platforms for the level 3
class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"prairie.png")).convert()
        self.background.set_colorkey( WHITE)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        level = [ [  STONE, 500, 550, ],
                  [  STONE, 570, 550],
                  [  STONE, 640, 550],
                  [  GRASS, 800, 400],
                  [  GRASS, 870, 400],
                  [  GRASS, 940, 400],
                  [  GRASS, 1000, 500],
                  [  GRASS, 1070, 500],
                  [  GRASS, 1140, 500],
                  [  STONE, 1120, 280],
                  [  STONE, 1190, 280],
                  [  STONE, 2060, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block =   Platform(platform[1],platform[2], TILEX, TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

          # Add a custom moving platform
        block =   MovingPlatform(1350,280, TILEX, TILEY,  MANTA)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
      

# Create platforms for the level 4
class Level_04(Level):
   
    """ Definition for level 4. """

    def __init__(self, player):
        """ Create level 4. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"forest.png")).convert()
        self.background.set_colorkey(WHITE)
        self.level_limit = -2000

        # Array with type of platform, and x, y location of the platform.
        level = [ [  STONE, 500, 550, ],
                  [  STONE, 600, 550],
                  [  STONE, 700, 550],
                  [  GRASS, 800, 400],
                  [  GRASS, 900, 400],
                  [  GRASS, 1000, 400],
                  [  GRASS, 1000, 500],
                  [  GRASS, 1100, 500],
                  [  GRASS, 1200, 500],
                  [  STONE, 1600, 300],
                  [  STONE, 1700, 300],
                  [  STONE, 1800, 300],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block =   Platform(platform[1],platform[2], TILEX, TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

           # Add a custom moving platform
        block =   MovingPlatform(1500,300,TILEX,TILEY,  JELLYFISH)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_05(Level):

    """ Definition for level 5. """
    def __init__(self, player):
        """ Create level 5. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"valley.png")).convert()
        self.level_limit = -2000


class Level_06(Level):
   
    """ Definition for level 6. """

    def __init__(self, player):
        """ Create level 6. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"wasteland.png")).convert()
        self.background.set_colorkey( WHITE)
        self.level_limit = -2500



class Level_07(Level):
   
    """ Definition for level 7. """

    def __init__(self, player):
        """ Create level 7. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"vault.png")).convert()
        self.background.set_colorkey( WHITE)
        self.level_limit = -2500
        


class Level_08(Level):
    
    """ Definition for level 8. """

    def __init__(self, player):
        """ Create level 8. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"eden.png")).convert()
        self.level_limit = -2500
        


class Level_09(Level):

    """ Definition for level 9. """

    def __init__(self, player):
        """ Create level 9. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"orbit.png")).convert()
        self.level_limit = -2500
        

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("MyPySky python based sky fan art game")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
    level_list.append(Level_05(player))
    level_list.append(Level_06(player))
    level_list.append(Level_07(player))
    level_list.append(Level_08(player))
    level_list.append(Level_09(player))


    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 140
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    player.go_left()
                if event.key == K_d or event.key == K_RIGHT:
                    player.go_right()
                if event.key == K_w or event.key == K_UP:
                    player.jump()
                if event.key == K_q:
                    done = True 

            if event.type == pygame.KEYUP:
                if event.key == K_a or event.key == K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == K_d or event.key == K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
