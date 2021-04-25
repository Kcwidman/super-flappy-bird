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
        self.new_test_init("TEST 1: pipes move across screen")
        x1 = self.game.pipelist[0].x_loc
        self.game.test_main(1)
        x2 = self.game.pipelist[0].x_loc
        self.append_results(x1 - x2 == VEL)

        self.new_test_init("TEST 2: bird colliding with pipe ends game")
        self.game.easy_mode = True
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC + 50, 300))
        self.game.test_main(60)
        self.append_results(self.game.game_over == True)

        self.new_test_init("TEST 3: bird passing through pipe increments score")
        self.game.easy_mode = True
        score1 = self.game.Score.score
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC, BIRD_START_Y_LOC + 30))
        self.game.test_main(30)
        passed = score1 + 1 == self.game.Score.score
        self.append_results(passed)

        self.new_test_init("TEST 4: score multiplier increases the score by 2 on passing through pipes")
        self.game.easy_mode = True
        self.game.scoreMult_mode = True
        score1 = self.game.Score.score
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC, BIRD_START_Y_LOC + 30))
        self.game.test_main(30)
        passed = score1 + 2 == self.game.Score.score
        self.append_results(passed)
        
        self.new_test_init("TEST 5: level complete if the final pipe passes through the edge")
        self.game.easy_mode = True
        self.game.level_mode = True
        self.game.pipelist.clear()
        self.game.pipelist.insert(0, Pipe(50, BIRD_START_Y_LOC + 30))
        self.game.test_main(100)
        self.append_results(self.game.level_complete)

        self.new_test_init("TEST 6: bird colliding with floor ends game")
        self.game.birdObj.y_loc = FLOOR - 50
        self.game.test_main(60)
        self.append_results(self.game.game_over)

        self.new_test_init("TEST 7: Bird Jumps on pressing spacebar")
        self.game.birdObj.y_loc = 500
        self.game.birdObj.jump_bird()
        self.game.test_main(10)
        passed = bool
        if self.game.birdObj.y_loc < 500:
            passed = True
        else:
            passed = False
        self.append_results(passed)

        self.new_test_init("TEST 8: bird cannot jump above the screen dimensions")
        self.game.birdObj.y_loc = 0
        self.game.birdObj.jump_bird()
        self.game.test_main(1)
        passed = self.game.birdObj.y_loc >= 0
        self.append_results(passed)

        self.new_test_init("TEST 9: bird collides with orbs")
        self.game.easy_mode = True
        self.game.orblist.append(ScoreMult(BIRD_START_X_LOC + 50, BIRD_START_Y_LOC))
        self.game.test_main(60)
        self.append_results(self.game.orblist == [])

        self.new_test_init("TEST 10: ghost mode allows bird to pass through pipes")
        self.game.easy_mode = True
        self.game.ghost_mode = True
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC + 50, 300))
        self.game.test_main(60)
        self.append_results(self.game.game_over == False)

        self.new_test_init("TEST 11: coin value increases on collision with coin")
        self.game.easy_mode = True
        self.game.orblist.append(Coin(BIRD_START_X_LOC + 50, BIRD_START_Y_LOC))
        self.game.test_main(60)
        self.append_results(self.game.Score.coin_count == 1)

        self.new_test_init("TEST 12: collision with fire power orb activates fire power mode")
        self.game.easy_mode = True
        self.game.orblist.append(FirePower(BIRD_START_X_LOC + 50, BIRD_START_Y_LOC))
        self.game.test_main(60)
        self.append_results(self.game.firePower_mode == True)

        self.new_test_init("TEST 13: firing projectile collides with pipe and lowers health")
        self.game.easy_mode = True
        self.game.firePower_mode = True
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC + 100, 300))
        self.game.fire()
        self.game.test_main(40)
        check1 = self.game.pipelist[0].health == 1
        self.append_results(check1)

        self.new_test_init("TEST 14: 2 hits to a pipe destroys it")
        self.game.easy_mode = True
        self.game.firePower_mode = True
        self.game.pipelist.clear()
        self.game.pipelist.insert(0, Pipe(BIRD_START_X_LOC + 150, 300))
        self.game.fire()
        self.game.test_main(30)
        self.game.fire()
        self.game.test_main(50)
        print(self.game.pipelist)
        self.append_results(self.game.pipelist == [])


