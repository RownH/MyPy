import pygame
from pygame.sprite import Sprite
from settings import Settings
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        self.y-=self.speed_factor;
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

class Double_Bullet(Bullet):
    def __init__(self,ai_settings,screen,ship):
        super().__init__(ai_settings,screen,ship)
        self.rect2=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height);
        self.rect2.centerx=ship.rect.centerx-10
        self.rect.centerx=ship.rect.centerx+10
        self.rect2.top=ship.rect.top;
        self.y2=float(self.rect2.y)
    
    def update(self):
        self.y-=self.speed_factor;
        self.y2-=self.speed_factor;
        self.rect.y=self.y;
        self.rect2.y=self.y2;
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect);
        pygame.draw.rect(self.screen,self.color,self.rect2);
    