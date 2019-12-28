# focus just on line race now
from enum import Enum

class GameMode(Enum):
    marathon = 1
    line_race = 2

class Game:
    timestamp = 0
    mode = 0
    score = 0
    time = 0
    
    def __init__(self):
        pass
