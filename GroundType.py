from const import *
class GroundType:
    class ground(enum.Enum):
        cliff = 1
        fence = 2
        snag = 3
    def __init__(self, id):
