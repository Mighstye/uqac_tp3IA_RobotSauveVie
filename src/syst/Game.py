"""
Game Class :
    The class that operate a "Game" (A round in the simulation)

    Constructor :
    Take one int argument -> The Iteration (How many round has been played already)
    env : Reference to the environment
    end : Bool to know if the Game (Round) is finished or not
            None : Not finished
            True : Finished (Robot won)
            False : Finished (Robot lost)
    moveList : List of all the robot movement
    stringState : State of the game as a String ('Unknown' / 'Win' / 'Lose')
    expert : ExpertSystem object

    while loop :
        This is the main loop of a round
        We loop until env.checkEndCondition return something different from None (meaning the round is finished)

        expert.deduction : Make the expert system take a decision

    if/else statement :
        Change the stringState with the actual StringState of the finished game

    print State + Round
    clear the console
    ask the user to press Enter
    self.finalState = [...] take the EndCondition of the game and put it inside the variable
    (Because the Main class need to know if the robot won or losses)
    [End of the constructor - Meaning end of the round]
"""


from src.envi import Environment
from src.env_objects.expert_sys.ExpertSystem import ExpertSystem
import os


class Game:

    def __init__(self, iteration):
        self.env = Environment.Environment(3 + iteration)
        self.end = None
        self.moveList = []
        self.stringState = 'Unknown'
        self.expert = ExpertSystem()

        while self.env.checkEndCondition() is None:
            self.expert.deduction()

        if self.env.checkEndCondition():
            self.stringState = 'Win'
        else:
            self.stringState = 'Lose'
        print("State : " + self.stringState + " - Round " + str(iteration))
        # print(self.env)
        input("Press enter for next Level.")
        os.system('cls')
        self.finalState = self.env.checkEndCondition()
