from src.env_objects.enum import TileType


class EnvObject(object):
    def __init__(self):
        self.type = TileType.TileType.UNKNOWN

    def __str__(self):
        return self.type.value
