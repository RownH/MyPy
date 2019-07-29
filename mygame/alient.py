import pygame
from pygame.sprite import Sprite
class Anlien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Anlien,self).__init__()
        self.screen=screen;
        self.ai_settings=ai_settings;
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
    def updae(self):
        pass;
    def move_method(self,method):
        pass;

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    