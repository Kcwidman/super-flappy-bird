from constants import *
from orb import *
from pipe import *
from powerUps import *
class Level:
#this class reads in from the file and creates objects and places them into a list
#inside the game class, the level object can be created, then the game can copy the objects
#and load them into the game
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
        #load orbs
            elif self.flag == "orbs":
                data = s.split()
                orb_type = data[0]
                x_loc = int(data[1])
                y_loc = int(data[2])

                if orb_type == "coin":
                    self.orbs.append( Coin(x_loc, y_loc) )
                if orb_type == "firePower":
                    self.orbs.append( FirePower(x_loc, y_loc) )
                if orb_type == "ghost":
                    self.orbs.append( Ghost(x_loc, y_loc) )
                if orb_type == "scoreMult":
                    self.orbs.append( ScoreMult(x_loc, y_loc) )
        #load pipes
            elif self.flag == "pipes":
                data = s.split()
                self.pipes.append(Pipe(int(data[0]), int(data[1])))

        f.close()


    