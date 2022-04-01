from src.env_objects.expert_sys.KnowledgeBase import KnowledgeBase
from src.env_objects import Dust, Fire, Warm, Robot, Human, Ruins, EnvObject
from src.envi import Environment
import random
import os


class Game:

    def __init__(self, iteration):
        self.env = Environment.Environment(3 + iteration)
        self.end = None
        self.moveList = []
        self.stringState = 'Unknown'
        self.possibleMove = [0,1,2,3]
        self.robotMap = [[[] for i in range(3+iteration)] for j in range(3+iteration)]


        knowledgeBase = KnowledgeBase(3+iteration)




        while self.env.checkEndCondition() is None:
            """C"EST ICI QU'ON MET L'IA MESSIEURS"""

            print(self.env.robot.pos)
            print(self.env.robot.neighboor)
            #if isinstance(self.env.robot.neighboor[0][0], Dust.Dust):


            self.mapExploration()

            #print("les voisins : "+str(self.env.robot.neighboor[0][0].type.value))
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
            #self.env.robot.neighboor
            #self.env.robot.listpos
            #self.env.robot.oldPos
        if self.env.checkEndCondition():
            self.stringState = 'Win'
        else:
            self.stringState = 'Lose'
        print("State : "+self.stringState)
        print("Move list :")
        for move in self.moveList:
            print(move)
        print(self.env)
        input("Press enter for next Level.")
        os.system('cls')
        self.finalState = self.env.checkEndCondition()




    def mapExploration(self):
        i = 0
        direction = ["N", "E", "S", "W"]
        if self.env.robot.neighboor[0] != None:
            for object in self.env.robot.neighboor[i]:
                rien = True
                if isinstance(object, Dust.Dust):
                    rien = False
                    print("il y a une poussière !")
                    if direction[i] == "N" and self.env.robot.pos[0] - 1>0:
                        print(self.env.robot.pos[0] - 1)
                        self.robotMap[self.env.robot.pos[0] - 1][self.env.robot.pos[1]].append("D")
                    if direction[i] == "E" and self.env.robot.pos[1] + 1<len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] + 1].append("D")
                    if direction[i] == "S" and self.env.robot.pos[0] + 1<len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0] + 1][self.env.robot.pos[1]].append("D")
                    if direction[i] == "W" and self.env.robot.pos[1] - 1>0:
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] - 1].append("D")
                if isinstance(object, Ruins.Ruins):
                    rien = False
                    print("il y a des ruines !")
                    if direction[i] == "N" and self.env.robot.pos[0] - 1 > 0:
                        self.robotMap[self.env.robot.pos[0] - 1][self.env.robot.pos[1]].append("R")
                    if direction[i] == "E" and self.env.robot.pos[1] + 1 < len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] + 1].append("R")
                    if direction[i] == "S" and self.env.robot.pos[0] + 1 < len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0] + 1][self.env.robot.pos[1]].append("R")
                    if direction[i] == "W" and self.env.robot.pos[1] - 1 > 0:
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] - 1].append("R")
                if isinstance(object, Fire.Fire):
                    rien = False
                    print("il y a un feu !")
                    if direction[i] == "N" and self.env.robot.pos[0] - 1 > 0:
                        self.robotMap[self.env.robot.pos[0] - 1][self.env.robot.pos[1]].append("F")
                    if direction[i] == "E" and self.env.robot.pos[1] + 1 < len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] + 1].append("F")
                    if direction[i] == "S" and self.env.robot.pos[0] + 1 < len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0] + 1][self.env.robot.pos[1]].append("F")
                    if direction[i] == "W" and self.env.robot.pos[1] - 1 > 0:
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] - 1].append("F")
                if isinstance(object, Warm.Warm):
                    rien = False
                    print("il y a de la chaleur !")
                    if direction[i] == "N" and self.env.robot.pos[0] - 1 > 0:
                        self.robotMap[self.env.robot.pos[0] - 1][self.env.robot.pos[1]].append("W")
                    if direction[i] == "E" and self.env.robot.pos[1] + 1 < len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] + 1].append("W")
                    if direction[i] == "S" and self.env.robot.pos[0] + 1 < len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0] + 1][self.env.robot.pos[1]].append("W")
                    if direction[i] == "W" and self.env.robot.pos[1] - 1 > 0:
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] - 1].append("W")
                if isinstance(object, Human.Human):
                    rien = False
                    print("il y a un humain !")
                    if direction[i] == "N" and self.env.robot.pos[0] - 1>0:
                        self.robotMap[self.env.robot.pos[0] - 1][self.env.robot.pos[1]].append("H")
                    if direction[i] == "E" and self.env.robot.pos[1] + 1<len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] + 1].append("H")
                    if direction[i] == "S" and self.env.robot.pos[0] + 1<len(self.env.grid):
                        self.robotMap[self.env.robot.pos[0] + 1][self.env.robot.pos[1]].append("H")
                    if direction[i] == "W" and self.env.robot.pos[1] - 1>0:
                        self.robotMap[self.env.robot.pos[0]][self.env.robot.pos[1] - 1].append("H")
                if rien:
                    print("la voix est libre !")
                i+=1
            print(self.robotMap)









