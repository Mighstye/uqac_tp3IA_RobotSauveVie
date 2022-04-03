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
        self.posOf4LastVs = []

        while self.env.checkEndCondition() is None:
            """C"EST ICI QU'ON MET L'IA MESSIEURS"""

            # print(self.env.robot.pos)
            # if isinstance(self.env.robot.neighboor[0][0], Dust.Dust):

            listeRegleApplicable, listeVoisins = self.selectionApplicableRule()
            # self.__printknowledgeBase()
            self.appliquerRule(listeRegleApplicable, listeVoisins)
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
                    self.knowledgeBase.listKnowledge[self.env.robot.pos[0] - 1][self.env.robot.pos[1]] = \
                        [value for value in
                         self.knowledgeBase.listKnowledge[self.env.robot.pos[0] - 1][self.env.robot.pos[1]] if
                         value in ['V']]
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'N')
                if 1 == i:
                    self.knowledgeBase.listKnowledge[self.env.robot.pos[0]][self.env.robot.pos[1] + 1] = \
                        [value for value in
                         self.knowledgeBase.listKnowledge[self.env.robot.pos[0]][self.env.robot.pos[1] + 1] if
                         value in ['V']]
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'E')
                if 2 == i:
                    self.knowledgeBase.listKnowledge[self.env.robot.pos[0] + 1][self.env.robot.pos[1]] = \
                        [value for value in
                         self.knowledgeBase.listKnowledge[self.env.robot.pos[0] + 1][self.env.robot.pos[1]] if
                         value in ['V']]
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'S')
                if 3 == i:
                    self.knowledgeBase.listKnowledge[self.env.robot.pos[0]][self.env.robot.pos[1] - 1] = \
                        [value for value in
                         self.knowledgeBase.listKnowledge[self.env.robot.pos[0]][self.env.robot.pos[1] - 1] if
                         value in ['V']]
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'W')
        self.__putOldPosInMap()

    def __putOldPosInMap(self):
        self.posOf4LastVs.append(self.env.robot.oldPos)
        if len(self.posOf4LastVs) > 7:
            self.knowledgeBase.listKnowledge[self.posOf4LastVs[0][0]][self.posOf4LastVs[0][1]].remove('V')
            self.posOf4LastVs.pop(0)
        self.knowledgeBase.listKnowledge[self.env.robot.oldPos[0]][self.env.robot.oldPos[1]].append('V')

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

    def selectionApplicableRule(self):
        self.mapExploration()
        listeRegleApplicable = []
        listeVoisins = self.getVoisinFromMap()
        for voisin in listeVoisins:
            for rule in self.rules:
                if voisin[0] == rule.condition or voisin[0].reverse() == rule.condition:
                    print("New rule : "+str(rule))
                    listeRegleApplicable.append(rule)

        return listeRegleApplicable, listeVoisins

    def appliquerRule(self, rule, listeVoisins):
        possibleMove = []
        for single_rule in rule:
            for cond in single_rule.condition:
                for voisin in listeVoisins:
                    if cond in voisin[0]:
                        direction = voisin[1]
                        if cond == "H":
                            possibleMove.append((direction, 10))
                        elif cond == "Ru":
                            possibleMove.append((self.nextSafeCardinal(direction), 8))
                        elif cond == "F":
                            self.env.robot.extinguish(direction)
                            return
                        elif cond == "D":
                            if "V" not in voisin[0]:
                                possibleMove.append((direction, 4))
                            else:
                                possibleMove.append((direction, 1))
                        elif cond == "W":
                            possibleMove.append((direction, 6))
                        elif cond == "??":
                            if "V" not in voisin[0]:
                                possibleMove.append((direction, 5))
                            else:
                                possibleMove.append((direction, 2))
        bestDir = ''
        best = 0
        for move in possibleMove:
            print("Evaluating "+str(move))
            if move[1] > best:
                print("Move is better !")
                bestDir = move[0]
                best = move[1]
        print("Best choice = "+str(bestDir)+" with "+str(best))
        self.env.robot.move(bestDir)

    def nextSafeCardinal(self, originDirection):
        nextCardIsSafe = False
        card = ''
        originDirectionIndex = self.cardList.index(originDirection)
        while not nextCardIsSafe:
            originDirectionIndex += 1
            if 4 == originDirectionIndex:
                originDirectionIndex = 0
            card = self.cardList[originDirectionIndex]
            if self.getInfoOnDirection(card) is not None and self.getInfoOnDirection(card):
                thisTileIsSafe = True
                for element in self.getInfoOnDirection(card):
                    if element == 'F' or element == 'Ru':
                        thisTileIsSafe = False
                if thisTileIsSafe:
                    nextCardIsSafe = True
        print("Next safe card is "+str(card))
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
