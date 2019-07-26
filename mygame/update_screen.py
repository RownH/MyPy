import pygame
from ship import Ship
def update_screen(ai_seetings,screen,ship):
    screen.fill(ai_seetings.color())
    ship.update()
    ship.blitme()
    pygame.display.flip()
