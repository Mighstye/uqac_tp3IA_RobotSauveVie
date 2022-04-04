"""
Environment Class, this class represent the environment

Specs : It uses Borg Idiom, meaning if you instantiate more than one Environment you will only get a reference to the
already created Environment

Constructor :
    Take an int => N (Default N=-1) : If no int are provided that means the Environment is called for reference purpose
    If an int is provided : The environment will create itself
    N -> Dimension of the area

Methods :
    __str__ : Override how the object will be displayed when printed
    robotMove(robot) : Update the position of the robot after a movement (Called by Robot object)
                       robot : Reference to the robot
    checkEndCondition : Return None if no end condition
                        True if the Robot won the round
                        False if the Robot Lose
    returnTileContent(pos) : Return the EnvObject in a Tile of the grid
                             pos : Coordinate of the Tile which the method will return the content from
    __generate : Generate the object (Fire, Warm, Ruins, Dust, Human) in the environment
    __randomPosInGrid : Return a random position in the grid which is not the position of the robot / the human
    removeElement(pos, element) : Remove all occurrence of "element" if the tile situated in "pos"
                                  pos : Tuple for the coordinate
                                  element : Class of the element to remove (ex : Fire.Fire)
    extinguish(pos) : Extinguish Fire in a give pos (Also remove nearly Warm caused by the Fire)
                      pos : Pos of the Fire to extinguish
"""
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
        maxSize = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if len(self.grid[i][j]) > maxSize:
                    maxSize = len(self.grid[i][j])
        returnStr = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                for obj in self.grid[i][j]:
                    returnStr = returnStr + obj.__str__()
                if len(self.grid[i][j]) != maxSize:
                    returnStr = returnStr + ('_' * (maxSize-len(self.grid[i][j])))
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
            if -1 == pos[0] or -1 == pos[1]:
                return None
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
            else:
                break
        while RUINS_COUNT > 0:
            pos = self.__randomPosInGrid()
            if pos != (0, 0) and pos != (len(self.grid) - 1, len(self.grid) - 1):
                try:
                    self.grid[pos[0]][pos[1]].remove(self.envObjRef)
                except ValueError:
                    pass
                self.grid[pos[0]][pos[1]].append(Ruins.Ruins(pos))
                RUINS_COUNT -= 1
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
            else:
                break
        try:
            self.grid[0][0].remove(self.envObjRef)
        except ValueError:
            pass
        self.grid[0][0].append(self.robot)
        try:
            self.grid[len(self.grid) - 1][len(self.grid) - 1].remove(self.envObjRef)
        except ValueError:
            pass
        humanNeedPlacement = True
        while humanNeedPlacement:
            pos = self.__randomPosInGrid()
            if pos != (0, 0):
                legitPos = True
                for elem in self.grid[pos[0]][pos[1]]:
                    if isinstance(elem, Fire.Fire) or isinstance(elem, Ruins.Ruins):
                        legitPos = False
                if legitPos:
                    try:
                        self.grid[pos[0]][pos[1]].remove(self.envObjRef)
                    except ValueError:
                        pass
                    self.grid[pos[0]][pos[1]].append(Human.Human(pos))
                    humanNeedPlacement = False
        self.robot.askNeighboor()

    def __randomPosInGrid(self):
        returnStatement = random.randint(0, len(self.grid) - 1), random.randint(0, len(self.grid) - 1)
        if returnStatement != (0, 0) and returnStatement != (len(self.grid) - 1, len(self.grid) - 1):
            return returnStatement
        else:
            return self.__randomPosInGrid()

    def removeElement(self, pos, element):
        try:
            for elem in self.grid[pos[0]][pos[1]]:
                if isinstance(elem, element):
                    try:
                        self.grid[pos[0]][pos[1]] = list(filter(elem.__ne__, self.grid[pos[0]][pos[1]]))
                    except ValueError:
                        pass
                    except IndexError:
                        pass
                    try:
                        if not self.grid[pos[0]][pos[1]]:
                            self.grid[pos[0]][pos[1]].append(self.envObjRef)
                    except IndexError:
                        pass
        except IndexError:
            pass

    def extinguish(self, pos):
        didExtinguish = False
        posCard = [(pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0]+1, pos[1]), (pos[0], pos[1]-1)]
        try:
            for elem in self.grid[pos[0]][pos[1]]:
                if isinstance(elem, Fire.Fire):
                    didExtinguish = True
        except IndexError:
            pass
        self.removeElement(pos, Fire.Fire)
        for posI in posCard:
            try:
                self.removeElement(posI, Warm.Warm)
            except IndexError:
                pass
        return didExtinguish

