'''
对游戏进行设置
窗口宽度,高度
敌人数目等
'''
class Settings():
    def __init__(self,width,height,color):
        self.__width=width;
        self.__height=height;
        self.__color=color;
        self.ship_speed_factor=1.5

        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullet_nums=5;
    def Window_width(self):
        return self.__width;
    
  
    def Window_height(self):
        return self.__height;
  
    def color(self):
        return self.__color;




