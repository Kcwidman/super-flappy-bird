from game import *
from test import *

if len(sys.argv) > 1:
    test = Test()
    test.run()
    test.print_results()
else:
    game = Game()
    game.main()