from constants import *
from orb import *
from pipe import *
from slowMo import *
class Level:

    def __init__(self):
        self.orbs = [SlowMo(300, 300)]
        self.pipes = []
        self.flag = None
#read from file to generate level
        f = open("level1.txt", "r")
        for x in f:
            if x == "ORBS":
                self.flag = "orbs"
            elif x == "PIPES":
                self.flag = "pipes"
                print("pipes activated")
            elif self.flag == "orbs":
                data = x.split()
                # self.orbs
            elif self.flag == "pipes":
                data = x.split()
                print(data)
                self.pipes.append(Pipe(data[0]))
        f.close()
        # print(self.pipes)


    