from src.env_objects.enum import TileType, Directions
from src.env import Environment
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
            self.__askNeighboor()

    def __askNeighboor(self):
        self.neighboor[0] = self.env.returnTileContent((self.pos[0]-1, self.pos[1]))
        self.neighboor[1] = self.env.returnTileContent((self.pos[0], self.pos[1]+1))
        self.neighboor[2] = self.env.returnTileContent((self.pos[0]+1, self.pos[1]))
        self.neighboor[3] = self.env.returnTileContent((self.pos[0], self.pos[1]-1))
