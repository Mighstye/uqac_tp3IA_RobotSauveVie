from src.env_objects.expert_sys.KnowledgeBase import KnowledgeBase
from src.env_objects import Dust, Fire, Warm, Robot, Human, Ruins, EnvObject
from src.env_objects.enum import Directions
from src.env_objects.expert_sys.Rules_base import Rules_base
from src.envi import Environment
import random
import os


class Game:

    def __init__(self, iteration):
        self.env = Environment.Environment(3 + iteration)
        self.end = None
        self.moveList = []
        self.stringState = 'Unknown'
        self.knowledgeBase = KnowledgeBase(3 + iteration)
        self.rules_base = Rules_base()
        self.rules = self.rules_base.rulesOfGame()
        self.cardList = ['N', 'E', 'S', 'W']

        while self.env.checkEndCondition() is None:
            """C"EST ICI QU'ON MET L'IA MESSIEURS"""

            # print(self.env.robot.pos)
            # if isinstance(self.env.robot.neighboor[0][0], Dust.Dust):

            listeRegleApplicable, listeVoisins = self.selectionApplicableRule()
            # self.__printknowledgeBase()
            self.appliquerRule(self.selectionRule(listeRegleApplicable), listeVoisins)
            listeRegleApplicable.remove(self.selectionRule(listeRegleApplicable))
                # print(len(listeRegleApplicable))

            print("End turn")
            print(self.env)

            # print("les voisins : "+str(self.env.robot.neighboor[0][0].type.value))
            # randomizer = random.randint(0, 3)
            # if 0 == randomizer:
            #     self.env.robot.move('N')
            #     self.moveList.append("Moved North")
            # elif 1 == randomizer:
            #     self.env.robot.move('E')
            #     self.moveList.append("Moved East")
            # elif 2 == randomizer:
            #     self.env.robot.move('S')
            #     self.moveList.append("Moved South")
            # elif 3 == randomizer:
            #     self.env.robot.move('W')
            #     self.moveList.append("Moved West")

        if self.env.checkEndCondition():
            self.stringState = 'Win'
        else:
            self.stringState = 'Lose'
        print("State : " + self.stringState)
        print("Move list :")
        for move in self.moveList:
            print(move)
        print(self.env)
        input("Press enter for next Level.")
        os.system('cls')
        self.finalState = self.env.checkEndCondition()

    def mapExploration(self):
        for i in range(len(self.env.robot.neighboor)):
            if self.env.robot.neighboor[i] is not None:
                if 0 == i:
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'N')
                if 1 == i:
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'E')
                if 2 == i:
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'S')
                if 3 == i:
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'W')
        self.__notePosInMap()

    def getVoisinFromMap(self):
        pos = self.env.robot.pos
        voisin = [(self.knowledgeBase.returnTileContent((pos[0] - 1, pos[1])), 'N'),
                  (self.knowledgeBase.returnTileContent((pos[0], pos[1] + 1)), 'E'),
                  (self.knowledgeBase.returnTileContent((pos[0] + 1, pos[1])), 'S'),
                  (self.knowledgeBase.returnTileContent((pos[0], pos[1] - 1)), 'W')]
        return voisin

    def __placeInMap(self, pos, element, directionString):
        if isinstance(Directions.Directions(directionString), Directions.Directions):
            direction = Directions.Directions(directionString)
            if Directions.Directions.NORTH == direction:
                if element.type.value not in self.knowledgeBase.listKnowledge[pos[0] - 1][pos[1]]:
                    self.knowledgeBase.listKnowledge[pos[0] - 1][pos[1]].append(element.type.value)
            if Directions.Directions.EAST == direction:
                if element.type.value not in self.knowledgeBase.listKnowledge[pos[0]][pos[1] + 1]:
                    self.knowledgeBase.listKnowledge[pos[0]][pos[1] + 1].append(element.type.value)
            if Directions.Directions.SOUTH == direction:
                if element.type.value not in self.knowledgeBase.listKnowledge[pos[0] + 1][pos[1]]:
                    self.knowledgeBase.listKnowledge[pos[0] + 1][pos[1]].append(element.type.value)
            if Directions.Directions.WEST == direction:
                if element.type.value not in self.knowledgeBase.listKnowledge[pos[0]][pos[1] - 1]:
                    self.knowledgeBase.listKnowledge[pos[0]][pos[1] - 1].append(element.type.value)

    def __printknowledgeBase(self):
        for line in self.knowledgeBase.listKnowledge:
            for item in line:
                print(item, end='')
            print()

    def __notePosInMap(self):
        pos = self.env.robot.oldPos
        if "V" not in self.knowledgeBase.listKnowledge[pos[0]][pos[1]]:
            self.knowledgeBase.listKnowledge[pos[0]][pos[1]].append("V")

    def selectionApplicableRule(self):
        self.mapExploration()
        listeRegleApplicable = []
        listeVoisins = self.getVoisinFromMap()
        print(listeVoisins)
        for voisin in listeVoisins:
            for rule in self.rules:
                if voisin[0] == rule.condition or voisin[0].reverse() == rule.condition:
                    print("New rule : "+str(rule))
                    listeRegleApplicable.append(rule)

        return listeRegleApplicable, listeVoisins

    def selectionRule(self, applicableRule):
        ruleSelectionnee = 0
        for rule in applicableRule:
            if "H" in rule.condition:
                ruleSelectionnee = rule
            elif "F" in rule.condition:
                ruleSelectionnee = rule
            elif "??" in rule.condition:
                ruleSelectionnee = rule
            elif "Ru" in rule.condition:
                ruleSelectionnee = rule
            elif "W" in rule.condition:
                ruleSelectionnee = rule
            elif "D" in rule.condition:
                ruleSelectionnee = rule

        return ruleSelectionnee

    def appliquerRule(self, rule, listeVoisins):
        for cond in rule.condition:
            for voisin in listeVoisins:
                # print(voisin)
                if cond in voisin[0]:
                    direction = voisin[1]
                    if cond == "H":
                        print("H detected in "+direction)
                        self.env.robot.move(direction)
                        return
                    elif cond == "Ru":
                        print("Ru detected in "+direction)
                        self.env.robot.move(self.nextSafeCardinal(direction))
                        return
                    elif cond == "F":
                        print("F detected in " + direction)
                        self.env.robot.extinguish(direction)
                        return
                    elif cond == "D":
                        print("D detected in " + direction)
                        if "V" not in voisin[0]:
                            self.env.robot.move(direction)
                            return
                    elif cond == "W":
                        print("W detected in " + direction)
                        self.env.robot.move(direction)
                        return
                    elif cond == "??":
                        print("?? detected in " + direction)
                        self.env.robot.move(direction)
                        if "V" not in voisin[0]:
                            self.env.robot.move(direction)
                            return

    def nextSafeCardinal(self, originDirection):
        nextCardIsSafe = False
        card = ''
        originDirectionIndex = self.cardList.index(originDirection)
        while not nextCardIsSafe:
            originDirectionIndex += 1
            if 4 == originDirectionIndex:
                originDirectionIndex = 0
            card = self.cardList[originDirectionIndex]
            if self.getInfoOnDirection(card) is not None:
                thisTileIsSafe = True
                for element in self.getInfoOnDirection(card):
                    if element == 'F' or element == 'Ru':
                        thisTileIsSafe = False
                if thisTileIsSafe:
                    nextCardIsSafe = True
        return card

    def getInfoOnDirection(self, directionString):
        pos = self.env.robot.pos
        if isinstance(Directions.Directions(directionString), Directions.Directions):
            direction = Directions.Directions(directionString)
            if Directions.Directions.NORTH == direction:
                try:
                    return self.knowledgeBase.listKnowledge[pos[0] - 1][pos[1]]
                except IndexError:
                    return None
            if Directions.Directions.EAST == direction:
                try:
                    return self.knowledgeBase.listKnowledge[pos[0]][pos[1] + 1]
                except IndexError:
                    return None
            if Directions.Directions.SOUTH == direction:
                try:
                    return self.knowledgeBase.listKnowledge[pos[0] + 1][pos[1]]
                except IndexError:
                    return None
            if Directions.Directions.WEST == direction:
                try:
                    return self.knowledgeBase.listKnowledge[pos[0]][pos[1] - 1]
                except IndexError:
                    return None
