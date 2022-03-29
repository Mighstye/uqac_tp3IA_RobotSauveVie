from src.env_objects.enum import TileType
from src.env_objects import EnvObject


class Human(EnvObject.EnvObject):
    def __init__(self, pos):
        super(Human, self).__init__()
        self.pos = pos
        self.type = TileType.TileType.HUMAN
        