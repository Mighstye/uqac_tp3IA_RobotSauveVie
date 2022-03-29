from src.env_objects.enum import TileType
from src.env_objects import EnvObject


class Warm(EnvObject.EnvObject):
    def __init__(self, pos):
        super(Warm, self).__init__()
        self.pos = pos
        self.type = TileType.TileType.WARM
