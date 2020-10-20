import pygame
import random
import os
import constants
import levels


class Enemy(pygame.sprite.Sprite):

    ''' Spawn an enemy '''
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images',img))
        self.movey = 0
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

               
    def move(self):
        ''' enemy movement '''
        distance = random.randint(10,40)
        speed = random.randint(1,4)
        self.movey += 1.2
    
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0
       
        self.counter += 1

        if not self.rect.y >= constants.SCREEN_HEIGHT-constants.TILEX:
            self.rect.y += self.movey

        plat_hit_list = pygame.sprite.spritecollide(self, levels.platform_list, False)
        for p in plat_hit_list:
            self.movey = 0
            if self.rect.y > p.rect.y:
                self.rect.y = p.rect.y+constants.TILEY
            else:
                self.rect.y = p.rect.y-constants.TILEY

     