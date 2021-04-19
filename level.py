from constants import *
from orb import *
from pipe import *
from slowMo import *
class Level:

    def __init__(self, level_num):
        self.orbs = [SlowMo(300, 300)]
        self.pipes = []
        self.flag = None
        file_name = "levels/level" + str(level_num) + ".txt"
#read from file to generate level
        f = open(file_name, "r")
        file_contents = f.read().splitlines()
        for s in file_contents:
            if s == "ORBS":
                self.flag = "orbs"
            elif s == "PIPES":
                self.flag = "pipes"
            elif self.flag == "orbs":
                data = s.split()
                # self.orbs
            elif self.flag == "pipes":
                data = s.split()
                self.pipes.append(Pipe(int(data[0]), int(data[1])))
        f.close()
        # print(self.pipes)


    