import sys
import pygame
from settings import Settings
from ship import Ship
from check_event import check_event
from update_screen import update_screen
from alient import Anlien
def run_game():
    pygame.init()
    init_Settings=Settings(1200,800,(230,230,230))
    screen=pygame.display.set_mode((init_Settings.Window_width(),init_Settings.Window_height()))
    ship=Ship(init_Settings,screen)
    anlient=Anlien(init_Settings,screen)
    pygame.display.set_caption('fly battle')
    while True:
        check_event(ship)
        update_screen(init_Settings,screen,ship,anlient)
run_game()
