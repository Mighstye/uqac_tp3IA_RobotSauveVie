"""
Parent objects for all element (Fire, Warm, Ruins, Dust, Human, Robot)
self.type is the type of the element (See src.env_objects.enum.TileType)

Constructor :
    Set the type to Unknown (Default value)

Method:
    __str__ : Return the string name of the type (See src.env_objects.enum.TileType)
"""


from src.env_objects.enum import TileType


class EnvObject(object):
    def __init__(self):
        self.type = TileType.TileType.UNKNOWN

    def __str__(self):
        return self.type.value
