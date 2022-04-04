"""
Main class : The class that manage the whole simulation

It will create new Game Object until the robot lose.
Each newly created Game will take place in a larger environment (+1 each round)

variable :
    state = True (Boolean meaning if we should continue creating new game)
    i = 0 (iteration)

while loop :
    creating new Game that will play entirely before the program can go to the next line
    (Because the game play in the Game constructor)

state = gameRef.finalState (We get the finalState of the Game [True if robot won | False if it loses]
[Continue until the robot lose one round]

print how many round the robot lasted
"""


from syst import Game


if __name__ == "__main__":
    state = True
    i = 0
    while state:
        gameRef = Game.Game(i)
        state = gameRef.finalState
        i += 1
    print("Simulation finished, the robot survived for "+str(i)+" round")

