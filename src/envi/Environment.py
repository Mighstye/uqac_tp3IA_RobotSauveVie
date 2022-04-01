from src.utils import Borg
import random
from src.env_objects import Dust, Fire, Human, Robot, Ruins, Warm, EnvObject


class Environment(Borg.Borg):
    def __init__(self, N=-1):
        Borg.Borg.__init__(self)
        if N != -1:
            self.robot = Robot.Robot((0, 0))
            self.envObjRef = EnvObject.EnvObject()
            self.grid = [[[self.envObjRef] for i in range(N)] for j in range(N)]
            self.__generate()

    def __str__(self):
        returnStr = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                for obj in self.grid[i][j]:
                    returnStr = returnStr + obj.__str__()
                returnStr = returnStr + '|'
            returnStr = returnStr + '\n'
        return returnStr

    def robotMove(self, robot):
        self.grid[robot.oldPos[0]][robot.oldPos[1]].remove(self.robot)
        if not self.grid[robot.oldPos[0]][robot.oldPos[1]]:
            self.grid[robot.oldPos[0]][robot.oldPos[1]].append(self.envObjRef)
        try:
            self.grid[robot.pos[0]][robot.pos[1]].remove(self.envObjRef)
        except ValueError:
            pass
        self.grid[robot.pos[0]][robot.pos[1]].append(self.robot)

    def checkEndCondition(self):
        for obj in self.grid[self.robot.pos[0]][self.robot.pos[1]]:
            if isinstance(obj, Fire.Fire) or isinstance(obj, Ruins.Ruins):
                return False
            elif isinstance(obj, Human.Human):
                return True
        return None

    def returnTileContent(self, pos):
        try:
            return self.grid[pos[0]][pos[1]]
        except IndexError:
            return None

    def __generate(self):
        FIRE_COUNT = len(self.grid)//3
        RUINS_COUNT = len(self.grid)//3
        while FIRE_COUNT > 0:
            pos = self.__randomPosInGrid()
            if pos != (0, 0) and pos != (len(self.grid) - 1, len(self.grid) - 1):
                try:
                    self.grid[pos[0]][pos[1]].remove(self.envObjRef)
                except ValueError:
                    pass
                self.grid[pos[0]][pos[1]].append(Fire.Fire(pos))
                FIRE_COUNT -= 1
            else:
                break
            try:
                if pos[0] - 1 > -1:
                    self.grid[pos[0] - 1][pos[1]].append(Warm.Warm(pos))
                    try:
                        self.grid[pos[0] - 1][pos[1]].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
            try:
                if pos[0] + 1 < len(self.grid):
                    self.grid[pos[0] + 1][pos[1]].append(Warm.Warm(pos))
                    try:
                        self.grid[pos[0] + 1][pos[1]].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
            try:
                if pos[1] - 1 > -1:
                    self.grid[pos[0]][pos[1] - 1].append(Warm.Warm(pos))
                    try:
                        self.grid[pos[0]][pos[1] - 1].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
            try:
                if pos[1] + 1 < len(self.grid):
                    self.grid[pos[0]][pos[1] + 1].append(Warm.Warm(pos))
                    try:
                        self.grid[pos[0]][pos[1] + 1].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
        while RUINS_COUNT > 0:
            pos = self.__randomPosInGrid()
            if pos != (0, 0) and pos != (len(self.grid) - 1, len(self.grid) - 1):
                try:
                    self.grid[pos[0]][pos[1]].remove(self.envObjRef)
                except ValueError:
                    pass
                self.grid[pos[0]][pos[1]].append(Ruins.Ruins(pos))
                RUINS_COUNT -= 1
            else:
                break
            try:
                if pos[0] - 1 > -1:
                    self.grid[pos[0] - 1][pos[1]].append(Dust.Dust(pos))
                    try:
                        self.grid[pos[0] - 1][pos[1]].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
            try:
                if pos[0] + 1 < len(self.grid):
                    self.grid[pos[0] + 1][pos[1]].append(Dust.Dust(pos))
                    try:
                        self.grid[pos[0] + 1][pos[1]].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
            try:
                if pos[1] - 1 > -1:
                    self.grid[pos[0]][pos[1] - 1].append(Dust.Dust(pos))
                    try:
                        self.grid[pos[0]][pos[1] - 1].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
            try:
                if pos[1] + 1 < len(self.grid):
                    self.grid[pos[0]][pos[1] + 1].append(Dust.Dust(pos))
                    try:
                        self.grid[pos[0]][pos[1] + 1].remove(self.envObjRef)
                    except ValueError:
                        pass
            except IndexError:
                pass
        try:
            self.grid[0][0].remove(self.envObjRef)
        except ValueError:
            pass
        self.grid[0][0].append(self.robot)
        try:
            self.grid[len(self.grid) - 1][len(self.grid) - 1].remove(self.envObjRef)
        except ValueError:
            pass
        self.grid[len(self.grid) - 1][len(self.grid) - 1].append(Human.Human((len(self.grid) - 1, len(self.grid) - 1)))
        self.robot.askNeighboor()

    def __randomPosInGrid(self):
        returnStatement = random.randint(0, len(self.grid) - 1), random.randint(0, len(self.grid) - 1)
        if returnStatement != (0, 0) and returnStatement != (len(self.grid) - 1, len(self.grid) - 1):
            return returnStatement
        else:
            return self.__randomPosInGrid()
