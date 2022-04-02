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

        while self.env.checkEndCondition() is None:
            """C"EST ICI QU'ON MET L'IA MESSIEURS"""




            print(self.env.robot.pos)
            # if isinstance(self.env.robot.neighboor[0][0], Dust.Dust):


            listeRegleApplicable, listeVoisins = self.selectionApplicableRule()
            self.__printknowledgeBase()
            while listeRegleApplicable != []:
                self.appliquerRule(self.selectionRule(listeRegleApplicable), listeVoisins, listeRegleApplicable)
                listeRegleApplicable.remove(self.selectionRule(listeRegleApplicable))
                print(len(listeRegleApplicable))

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
        listeVoisin = []
        for i in range(len(self.env.robot.neighboor)):
            if self.env.robot.neighboor[i] is not None:
                if 0 == i:
                    voisins = []
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'N')
                        voisins.append(element.type.value)
                    listeVoisin.append([voisins, 'N'])
                if 1 == i:
                    voisins = []
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'E')
                        voisins.append(element.type.value)
                    listeVoisin.append([voisins, 'E'])
                if 2 == i:
                    voisins = []
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'S')
                        voisins.append(element.type.value)
                    listeVoisin.append([voisins, 'S'])
                if 3 == i:
                    voisins = []
                    for element in self.env.robot.neighboor[i]:
                        self.__placeInMap(self.env.robot.pos, element, 'W')
                        voisins.append(element.type.value)
                    listeVoisin.append([voisins, 'W'])
        return listeVoisin


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
        for pos in self.env.robot.listpos:
            if "V" not in self.knowledgeBase.listKnowledge[pos[0]][pos[1]]:
                self.knowledgeBase.listKnowledge[pos[0]][pos[1]].append("V")

    def __printknowledgeBase(self):
        for line in self.knowledgeBase.listKnowledge:
            for item in line:
                print(item, end='')
            print()

    def selectionApplicableRule(self):
        listeRegleApplicable = []
        listeVoisins = self.mapExploration()
        for voisin in listeVoisins:
            for obj in voisin[0]:
                for rule in self.rules:
                    if obj in rule.condition:
                        listeRegleApplicable.append(rule)
        for rule in listeRegleApplicable:
            print(rule.consequence)

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

    def appliquerRule(self, rule, listeVoisins, listeRegleApplicable):
        for cond in rule.condition:
            for voisin in listeVoisins:
                print(voisin)
                if cond in voisin[0]:
                    direction = voisin[1]
                    if cond == "H":
                        self.env.robot.move(direction)
                    elif cond == "F":
                        #eteindre feu
                        print("le robot ne peut pas encore éteindre les flammes :(")
                    elif cond == "??":
                        self.env.robot.move(direction)
                    elif cond == "Ru":
                        print("ruine, le robot n'avance pas")
                    elif cond == "W":
                        self.env.robot.move(direction)




