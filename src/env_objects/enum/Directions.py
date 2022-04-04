"""
Enum for the Directions and there String version
For example, the Robot class use String version of these directions
"""


from enum import Enum


class Directions(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'
