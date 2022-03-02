from casting.actor import Actor
from shared.point import Point
import random
class Artifact(Actor):
    
    def __init__(self):
        super().__init__()
        self._gem = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, random.randint(-7, -1))
        
    def get_gem(self):
        return self._gem
    
    def set_message(self, message):
        self._message = message
    
    def move_down(self, max_x, max_y):
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() - self._velocity.get_y()) % max_y
        self._position = Point(x, y)
    
    #def move_down(self, max_x, max_y):
    #    x = (self._position.get_x() + self._velocity.get_x()) % max_x
    #    y = (self._position.get_y() + self._velocity.get_y()) % max_y
    #    self._position = Point(x, y)