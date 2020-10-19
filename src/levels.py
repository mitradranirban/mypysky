import pygame
import os
import constants
import platforms

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
        screen.fill(constants.BLUE)
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
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 400, 500],
                  [platforms.SAND, 528, 500],
                  [platforms.STONE, 640, 500],
                  [platforms.ICE, 800, 400],
                  [platforms.ICE, 870, 400],
                  [platforms.STONE, 938,500],
                  [platforms.STONE, 1000,500],
                  [platforms.STONE, 1064,500],
                  [platforms.STONE, 1128,500]
                   ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[1],platform[2],constants.TILEX,constants.TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

      


# Create platforms for the level 2
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"isle.png")).convert()
        self.background.set_colorkey(constants.BLUE)
        self.level_limit = -2600

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE, 500, 550, ],
                  [platforms.STONE, 570, 490],
                  [platforms.STONE, 640, 430],
                  [platforms.GRASS, 800, 564],
                  [platforms.GRASS, 870, 500],
                  [platforms.GRASS, 940, 564],
                  [platforms.GRASS, 1000, 500],
                  [platforms.GRASS, 1070, 500],
                  [platforms.GRASS, 1140, 300],
                  [platforms.STONE, 1120, 280],
                  [platforms.STONE, 1190, 280],
                  [platforms.STONE, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[1],platform[2],constants.TILEX,constants.TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(1350,280,constants.TILEX,constants.TILEY,platforms.CLOUD)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
       

# Create platforms for the level 3
class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"prairie.png")).convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE, 500, 550, ],
                  [platforms.STONE, 570, 550],
                  [platforms.STONE, 640, 550],
                  [platforms.GRASS, 800, 400],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 940, 400],
                  [platforms.GRASS, 1000, 500],
                  [platforms.GRASS, 1070, 500],
                  [platforms.GRASS, 1140, 500],
                  [platforms.STONE, 1120, 280],
                  [platforms.STONE, 1190, 280],
                  [platforms.STONE, 2060, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[1],platform[2],constants.TILEX,constants.TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

          # Add a custom moving platform
        block = platforms.MovingPlatform(1350,280,constants.TILEX,constants.TILEY,platforms.MANTA)
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
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE, 500, 550, ],
                  [platforms.STONE, 564, 550],
                  [platforms.STONE, 628, 550],
                  [platforms.GRASS, 800, 400],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 940, 400],
                  [platforms.GRASS, 1000, 500],
                  [platforms.GRASS, 1064, 500],
                  [platforms.GRASS, 1128, 500],
                  [platforms.STONE, 1400, 280],
                  [platforms.STONE, 1464, 280],
                  [platforms.STONE, 1528, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[1],platform[2],constants.TILEX,constants.TILEY,platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

           # Add a custom moving platform
        block = platforms.MovingPlatform(1500,300,constants.TILEX,constants.TILEY,platforms.JELLYFISH)
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
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500



class Level_07(Level):
    """ Definition for level 7. """

    def __init__(self, player):
        """ Create level 7. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join('images',"vault.png")).convert()
        self.background.set_colorkey(constants.WHITE)
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
        

