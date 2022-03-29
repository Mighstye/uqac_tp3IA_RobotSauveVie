from src.env_objects.enum import TileType
from src.env_objects import EnvObject


class Dust(EnvObject.EnvObject):
    def __init__(self, pos):
        super(Dust, self).__init__()
        self.pos = pos
        self.type = TileType.TileType.DUST

