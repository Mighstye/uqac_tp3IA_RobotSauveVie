"""
Enum for all the possible type of Tile and a String version of them to make them possible to print
Thus, our Expert system use these String versions
"""


from enum import Enum


class TileType(Enum):
    DUST = 'D'
    FIRE = 'F'
    HUMAN = 'H'
    ROBOT = 'A'
    RUINS = 'R'
    WARM = 'W'
    UNKNOWN = '?'
