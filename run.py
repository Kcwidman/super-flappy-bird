from game import *
from test import *

#highest order file of the project
#it runs the main game loop or the test suite, depending on what was passed in as arguments on command line
if len(sys.argv) > 1:
    test = Test()
    test.run()
    test.print_results()
else:
    game = Game()
    game.main()