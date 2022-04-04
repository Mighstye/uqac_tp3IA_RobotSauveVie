"""
Rule class : The class that contains all the rules

constructor :
    allRules : a list where all rules are stocked
    append : put all the rule method inside the allRules list

    l : the list used by the methods (The list will mostly contain String Value of Element of a Neighbor)
"""
from src.env_objects.enum.TileType import TileType

class Rules:

    # A rule will return an amount of point

    def __init__(self):
        self.allRules = []
        self.allRules.append((self.Fire, TileType.FIRE.value))
        self.allRules.append((self.Dust, TileType.DUST.value))
        self.allRules.append((self.Human, TileType.HUMAN.value))
        self.allRules.append((self.Ruins, TileType.RUINS.value))
        self.allRules.append((self.Warm, TileType.WARM.value))
        self.l = []

    def assignList(self, li):
        self.l = li

    def Fire(self):  # Check if the list contains a Fire, return 50 points if so
        for elem in self.l:
            if TileType.FIRE.value == elem:
                return 50
        return 0

    def Dust(self):  # Check if the list contains a Dust, return 0 point if so (Still there for fine-tunning purpose)
        for elem in self.l:
            if TileType.DUST.value == elem:
                return 0
        return 0

    def Human(self):  # Check if the list contains a Human, return 60 points if so
        for elem in self.l:
            if TileType.HUMAN.value == elem:
                return 60
        return 0

    def Ruins(self):  # Check if the list contains a Ruin, return -1000 points if so
        for elem in self.l:
            if TileType.RUINS.value == elem:
                return -1000
        return 0

    def Warm(self):  # Check if the list contains a Warm, return 40 points if so
        for elem in self.l:
            if TileType.WARM.value == elem:
                return 40
        return 0
