from src.env_objects.expert_sys.KnowledgeBase import KnowledgeBase
from src.env_objects import Dust, Fire, Warm, Robot, Human, Ruins, EnvObject
from src.env_objects.enum import Directions
from src.envi import Environment
import random
import os


class Game:

    def __init__(self, iteration):
        self.env = Environment.Environment(3 + iteration)
        self.end = None
        self.moveList = []
        self.stringState = 'Unknown'
        self.robotMap = [[[] for i in range(3 + iteration)] for j in range(3 + iteration)]

        knowledgeBase = KnowledgeBase(3 + iteration)

        while self.env.checkEndCondition() is None:
            """C"EST ICI QU'ON MET L'IA MESSIEURS"""

            print(self.env.robot.pos)
            # if isinstance(self.env.robot.neighboor[0][0], Dust.Dust):

            self.mapExploration()
            self.__printRobotMap()

            # print("les voisins : "+str(self.env.robot.neighboor[0][0].type.value))
            randomizer = random.randint(0, 3)
            if 0 == randomizer:
                self.env.robot.move('N')
                self.moveList.append("Moved North")
            elif 1 == randomizer:
                self.env.robot.move('E')
                self.moveList.append("Moved East")
            elif 2 == randomizer:
                self.env.robot.move('S')
                self.moveList.append("Moved South")
            elif 3 == randomizer:
                self.env.robot.move('W')
                self.moveList.append("Moved West")
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

    def __placeInMap(self, pos, element, directionString):
        if isinstance(Directions.Directions(directionString), Directions.Directions):
            direction = Directions.Directions(directionString)
            if Directions.Directions.NORTH == direction:
                if element.type.value not in self.robotMap[pos[0] - 1][pos[1]]:
                    self.robotMap[pos[0] - 1][pos[1]].append(element.type.value)
            if Directions.Directions.EAST == direction:
                if element.type.value not in self.robotMap[pos[0]][pos[1] + 1]:
                    self.robotMap[pos[0]][pos[1] + 1].append(element.type.value)
            if Directions.Directions.SOUTH == direction:
                if element.type.value not in self.robotMap[pos[0] + 1][pos[1]]:
                    self.robotMap[pos[0] + 1][pos[1]].append(element.type.value)
            if Directions.Directions.WEST == direction:
                if element.type.value not in self.robotMap[pos[0]][pos[1] - 1]:
                    self.robotMap[pos[0]][pos[1] - 1].append(element.type.value)

    def __printRobotMap(self):
        for line in self.robotMap:
            for item in line:
                print(item, end='')
            print()
