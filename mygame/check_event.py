import sys
from bullet import Bullet
from bullet import Double_Bullet
import pygame
def check_event(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('exit')
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_down_event(event,ship)
        elif event.type==pygame.KEYUP:
            check_up_event(event,ship)

def check_down_event(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    if event.key==pygame.K_LEFT:
        ship.moving_left=True
    if event.key==pygame.K_SPACE and len(ship.bullets)<ship.ai_settings.bullet_nums:
        if ship.bullets_grade==0:
            new_bullet=Bullet(ship.ai_settings,ship.screen,ship)
        elif ship.bullets_grade==1:
            new_bullet=Double_Bullet(ship.ai_settings,ship.screen,ship)
        ship.bullets.add(new_bullet)
def check_up_event(event,ship):
    if event.key==pygame.K_LEFT:
        ship.moving_left=False;
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False;
