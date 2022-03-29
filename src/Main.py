from syst import Game


if __name__ == "__main__":
    state = True
    i = 0
    while state:
        gameRef = Game.Game(i)
        state = gameRef.finalState
        i += 1
    print("Simulation finished, the robot survived for "+str(i)+" round")
