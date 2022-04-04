"""
Rule class : The class that contains all the rules

constructor :
    allRules : a list where all rules are stocked
    append : put all the rule method inside the allRules list

    l : the list used by the methods (The list will mostly contain String Value of Element of a Neighbor)
"""


class Rules:

    # A rule will return an amount of point

    def __init__(self):
        self.allRules = []
        self.allRules.append((self.Fire, 'F'))
        self.allRules.append((self.Dust, 'D'))
        self.allRules.append((self.Human, 'H'))
        self.allRules.append((self.Ruins, 'R'))
        self.allRules.append((self.Warm, 'W'))
        self.l = []

    def assignList(self, li):
        self.l = li

    def Fire(self):  # Check if the list contains a Fire, return 50 points if so
        for elem in self.l:
            if 'F' == elem:
                return 50
        return 0

    def Dust(self):  # Check if the list contains a Dust, return 0 point if so (Still there for fine-tunning purpose)
        for elem in self.l:
            if 'D' == elem:
                return 0
        return 0

    def Human(self):  # Check if the list contains a Human, return 60 points if so
        for elem in self.l:
            if 'H' == elem:
                return 60
        return 0

    def Ruins(self):  # Check if the list contains a Ruin, return -1000 points if so
        for elem in self.l:
            if 'R' == elem:
                return -1000
        return 0

    def Warm(self):  # Check if the list contains a Warm, return 40 points if so
        for elem in self.l:
            if 'W' == elem:
                return 40
        return 0
