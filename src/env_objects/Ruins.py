from src.env_objects.enum import TileType
from src.env_objects import EnvObject


class Ruins(EnvObject.EnvObject):
    def __init__(self, pos):
        super(Ruins, self).__init__()
        self.pos = pos
        self.type = TileType.TileType.RUINS
        