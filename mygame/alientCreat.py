from pygame.sprite import Group
from alient import Anlien
class creatAnliens():
    def __init__(self,ai_settings,screen):
        self.alients=Group()
        self.settings=ai_settings
        self.screen=screen
        self.vertical=1;
    def creatMethod(self,rand):
        pass;
    def creatMthod1(self):
        alien=Anlien(self.settings,self.screen)
        alien_width=alien.rect.width
        available_space_x=self.settings.screen_width-2*alien_width
        number_aliens_x=int(available_space_x/(2*alien_width))
        for num in range(number_aliens_x):
            alien=Anlien(self.settings,self.screen)
            alien.x=alien_width+2*alien_width*num
            alien.rect.x=alien.x
            self.alients.add(alien)
    def update(self):
        
