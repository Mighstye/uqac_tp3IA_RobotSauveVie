from src.env_objects.enum import TileType
from src.env_objects import EnvObject


class Fire(EnvObject.EnvObject):
    def __init__(self, pos):
        super(Fire, self).__init__()
        self.pos = pos
        self.type = TileType.TileType.FIRE
