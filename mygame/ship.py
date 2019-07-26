import pygame
from settings import Settings
from pygame.sprite import Group
from bullet import Bullet
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.ai_settings=ai_settings
        self.center=float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.bullets_grade=1;
        self.bullets=Group()
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        for bullt in self.bullets.sprites():
            if bullt.rect.bottom>=0:
                bullt.update()
                bullt.draw_bullet()
            else:
                self.bullets.remove(bullt)
                print(self.bullets)
    def update(self):
        if self.moving_right:
           if self.rect.centerx<self.screen.get_width():
                self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left:
            if self.rect.centerx>0:
                self.center-=self.ai_settings.ship_speed_factor
        if self.moving_up:
            pass
        if self.moving_down:
            pass 
        self.rect.centerx=self.center
