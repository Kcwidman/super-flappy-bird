from constants import *
from orb import *
from pipe import *
from powerUps import *
class Level:

    def __init__(self, level_num):
        self.orbs = []
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
                orb_type = data[0]
                x_loc = int(data[1])
                y_loc = int(data[2])
                if orb_type == "coin":
                    self.orbs.append( Coin(x_loc, y_loc) )
                if orb_type == "slowMo":
                    self.orbs.append( SlowMo(x_loc, y_loc) )
                if orb_type == "firePower":
                    self.orbs.append( FirePower(x_loc, y_loc) )
            elif self.flag == "pipes":
                data = s.split()
                self.pipes.append(Pipe(int(data[0]), int(data[1])))
        f.close()
        # print(self.pipes)


    