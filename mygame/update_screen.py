import pygame
from ship import Ship
from alient import Anlien
def update_screen(ai_seetings,screen,ship,anlien):
    screen.fill(ai_seetings.color())
    ship.update()
    ship.blitme()
    anlien.blitme()
    pygame.display.flip()
