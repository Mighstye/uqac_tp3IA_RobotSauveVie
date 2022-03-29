from src.envi import Environment
import random
import os


class Game:

    def __init__(self, iteration):
        self.env = Environment.Environment(3 + iteration)
        self.end = None
        self.moveList = []
        self.stringState = 'Unknown'
        while self.env.checkEndCondition() is None:
            """C"EST ICI QU'ON MET L'IA MESSIEURS"""
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
        print("State : "+self.stringState)
        print("Move list :")
        for move in self.moveList:
            print(move)
        print(self.env)
        input("Press enter for next Level.")
        os.system('cls')
        self.finalState = self.env.checkEndCondition()
