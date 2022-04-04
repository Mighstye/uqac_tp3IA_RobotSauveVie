"""
ExpertSystem Class : The class that represent the expert system

Constructor :
    env : Reference to the environment
    rules : Create a new Rules Object

    North/East/South/West : List containing the String version of the object in the according neighbor
    (See src.env_objects.enum.TileTyle for information about String version)

Methods :
    getVoisinInfo :
        Get information about the neighbor and put there in the North/East/South/West list
        If a Neighbor doesn't exist, put an empty list instead

    getVoisinScore :
        Calculate a score for all voisin (The higher the score is the higher the neighbor is interesting to go to)

    deduction :
        Use Neighbor scores to deduce where the robot should go.
        If two neighbor has the same score, the robot go towards a random one between all these
"""


from src.envi.Environment import Environment
from src.env_objects.expert_sys.Rules import Rules
import random


class ExpertSystem:

    def __init__(self):
        # The system contain :
        # - A Reference to the environment
        # - A Rule object containing all the rule
        # - Some list that will contain information about what is in the neighbor tiles
        self.env = Environment()
        self.rules = Rules()

        self.North = []
        self.East = []
        self.South = []
        self.West = []

    def getVoisinInfo(self):  # This method put information about the neighbor in the different list
        self.North = []
        self.East = []
        self.South = []
        self.West = []
        # Iterating through the neighboor object of the robot
        for i in range(len(self.env.robot.neighboor)):
            if self.env.robot.neighboor[i]:
                for elem in self.env.robot.neighboor[i]:
                    # Put the element name (See TileType.py) in the corresponding list
                    if 0 == i:
                        self.North.append(elem.type.value)
                    elif 1 == i:
                        self.East.append(elem.type.value)
                    elif 2 == i:
                        self.South.append(elem.type.value)
                    elif 3 == i:
                        self.West.append(elem.type.value)
            # If the neighbor object is empty (If the neighbor doesn't exist) -> Emptying the list
            else:
                if 0 == i:
                    self.North = []
                elif 1 == i:
                    self.East = []
                elif 2 == i:
                    self.South = []
                elif 3 == i:
                    self.West = []

    # Return the score of a neighbor Tile
    def getVoisinScore(self, voisin):
        score = 0
        applicableRule = []
        # Iterating through the rule in the Rule Object
        for rule in self.rules.allRules:
            # rule[1] = The type of the object the rule apply to (Ex : 'F' if the rule applies to Fire Tile)
            # If the rule is useful for this neighbor (Meaning if rule[1] is in the neighbor list
            if rule[1] in voisin:
                # rule[0] = An actual method which is the rule itself
                # Then we put the rule in a list of all the applicable rule in this case
                applicableRule.append(rule[0])
        # Fill the list with information about the neighborhood
        self.rules.assignList(voisin)
        # Applies all rule to the concerned neighbor and return the final score of it
        for rule in applicableRule:
            score += rule()
        return score

    def deduction(self):
        # We get information about all the neighbor
        self.getVoisinInfo()
        # Calculate the score of all neighbor
        scores = [self.getVoisinScore(x) for x in [self.North, self.East, self.South, self.West]]
        # Take the max score
        maxScore = max(scores)
        bestScoreIndex = []
        # We get the index in the score list of the tile with the best score (There may be more than 1 winning tile)
        for i in range(len(scores)):
            if maxScore == scores[i]:
                bestScoreIndex.append(i)
        # We replace the index with the actual associated cardinals
        # 0 = 'N' | 1 = 'E' | 2 = 'S' | 3 = 'W'
        for i in range(len(bestScoreIndex)):
            if 0 == bestScoreIndex[i]:
                bestScoreIndex[i] = 'N'
            elif 1 == bestScoreIndex[i]:
                bestScoreIndex[i] = 'E'
            elif 2 == bestScoreIndex[i]:
                bestScoreIndex[i] = 'S'
            elif 3 == bestScoreIndex[i]:
                bestScoreIndex[i] = 'W'
        # If there is more than one winning tiles
        if len(bestScoreIndex) > 1:
            # Then we choose a random tile from the winning ones
            direction = random.choice(bestScoreIndex)
            # We try to extinguish if there is a fire, and we move toward the chosen direction
            self.env.robot.extinguish(direction)
            self.env.robot.move(direction)
        # If there is only one winning tile
        else:
            # Then we try to extinguish if there is a fire, and we move toward the winning direction
            self.env.robot.extinguish(bestScoreIndex[0])
            self.env.robot.move(bestScoreIndex[0])
