"""
Robot Class :
    Works like all other element except some variables and methods

    New Variables :
        pos : actual pos of the robot
        listpos : list of all pos of the robot
        oldpos : last pos of the robot
        neighboor : list containing copy of neighboor tiles content (Order N -> E -> S -> W)
        env : Reference to the environment

    Methods :
        move(direction) : Move one tile towards the given directions
                          direction : Direction String (see src.env_objects.enum.Directions) (ex : 'N' for North)
        askNeighboor() : Get copy of the neighboor tiles and put them is self.neighboor list
        extinguish(directionString) : Extinguish the fire in a given direction
                                      directionString : Direction String (see src.env_objects.enum.Directions)
                                                        (ex : 'N' for North)
"""


from src.env_objects.enum import TileType, Directions
from src.envi import Environment
from src.env_objects import EnvObject


class Robot(EnvObject.EnvObject):

    def __init__(self, pos):
        super(Robot, self).__init__()
        self.pos = pos
        self.type = TileType.TileType.ROBOT
        self.listpos = []
        self.oldPos = pos
        self.neighboor = [None, None, None, None]  # NORTH -> EAST -> SOUTH -> WEST (Clockwise)
        self.listpos.append(pos)
        self.env = Environment.Environment()

    def move(self, direction):
        if isinstance(Directions.Directions(direction), Directions.Directions):
            move = Directions.Directions(direction)
            moved = False
            if move == Directions.Directions.NORTH:
                if self.pos[0] - 1 > -1:
                    self.oldPos = self.pos
                    self.pos = (self.pos[0] - 1, self.pos[1])
                    moved = True
            elif move == Directions.Directions.SOUTH:
                if self.pos[0] + 1 < len(self.env.grid):
                    self.oldPos = self.pos
                    self.pos = (self.pos[0] + 1, self.pos[1])
                    moved = True
            elif move == Directions.Directions.EAST:
                if self.pos[1] + 1 < len(self.env.grid):
                    self.oldPos = self.pos
                    self.pos = (self.pos[0], self.pos[1] + 1)
                    moved = True
            elif move == Directions.Directions.WEST:
                if self.pos[1] - 1 > -1:
                    self.oldPos = self.pos
                    self.pos = (self.pos[0], self.pos[1] - 1)
                    moved = True
            if moved:
                self.env.robotMove(self)
            if self.listpos[len(self.listpos)-1] != self.oldPos:
                self.listpos.append(self.oldPos)
            self.askNeighboor()

    def askNeighboor(self):
        self.neighboor[0] = self.env.returnTileContent((self.pos[0]-1, self.pos[1]))
        self.neighboor[1] = self.env.returnTileContent((self.pos[0], self.pos[1]+1))
        self.neighboor[2] = self.env.returnTileContent((self.pos[0]+1, self.pos[1]))
        self.neighboor[3] = self.env.returnTileContent((self.pos[0], self.pos[1]-1))

    def extinguish(self, directionString):
        if isinstance(Directions.Directions(directionString), Directions.Directions):
            direction = Directions.Directions(directionString)
            if direction == Directions.Directions.NORTH:
                result = self.env.extinguish((self.pos[0] - 1, self.pos[1]))
            elif direction == Directions.Directions.EAST:
                result = self.env.extinguish((self.pos[0], self.pos[1] + 1))
            elif direction == Directions.Directions.SOUTH:
                result = self.env.extinguish((self.pos[0] + 1, self.pos[1]))
            elif direction == Directions.Directions.WEST:
                result = self.env.extinguish((self.pos[0], self.pos[1] - 1))
        return result
