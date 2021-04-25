from game import *

p = "PASSED"
f = "FAILED"
class Test:

    def __init__(self):
        self.test_results = []

    #if the condition is true, the test passes
    def append_results(self, condition):
        if condition:
            self.test_results[-1] += p
        else:
            self.test_results[-1] += f

    def new_test_init(self, description):
        self.game = Game()
        self.game.test_main(1)
        description += " -> "
        self.test_results.append(description)

    def print_results(self):
        for result in self.test_results:
            print(result)

    def run(self):
        self.new_test_init("TEST 0: bird colliding with pipe ends game")
        self.game.easy_mode = True
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC + 50, 300))
        self.game.test_main(60)
        self.append_results(self.game.game_over)

        self.new_test_init("TEST 1: bird colliding with floor ends game")
        self.game.birdObj.y_loc = FLOOR - 50
        self.game.test_main(60)
        self.append_results(self.game.game_over)

        self.new_test_init("TEST 2: bird passing through pipe increments score")
        self.game.easy_mode = True
        score1 = self.game.Score.score
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC, BIRD_START_Y_LOC + 30))
        self.game.test_main(30)
        passed = score1 + 1 == self.game.Score.score
        self.append_results(passed)

        self.new_test_init("TEST 3: bird cannot jump above the screen dimensions")
        self.game.birdObj.y_loc = 0
        self.game.birdObj.jump_bird()
        self.game.test_main(1)
        passed = self.game.birdObj.y_loc >= 0
        self.append_results(passed)
