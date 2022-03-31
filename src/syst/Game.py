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
        self.baseDeConnaissances = [[[] for i in range(3+iteration)] for j in range(3+iteration)]




        while self.env.checkEndCondition() is None:
            """C"EST ICI QU'ON MET L'IA MESSIEURS"""

            print(self.env.robot.neighboor)
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





