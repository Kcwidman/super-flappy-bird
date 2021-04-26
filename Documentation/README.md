README

This is a recreation of Flappy Bird coded for Project 4 of EECS 448 in Python using the Pygame module. All the required game documentation can be found in the Project 4 Documentation folder under Documentation.
It has been modified from the classic game to include powerups and a level system. 

Requirements:

	1.	Approval from GTA

How the project works is as follows:

	1.	Game Setup

		a.	On loading the game, a screen appears with the caption Flappy Bird. The screen has a background image and a scrolling bar below.

		b.	A bird with flapping wings is shown along with a menu from which you can select different levels of difficulty, an easy mode and a normal mode.

	2.	Running the game

		a.	To run the game directly:
			i.	Install the pygame module from the official pygame website, and run the game from the terminal with the command "python run.py" or "python3 run.py" depending on your installation of python.

		b.	To run the game using an IDE like Pycharm:
			i.	Go to File -> Settings -> Project: super-flappy-bird -> Python Interpreter and click the ‘+’ icon on the bottom left corner of the table.
			ii.	Search for the pygame module and click Install Package.
			iii. To run the game for the first time go to the run class [run.py] and select the Run menu option from the taskbar. Select Run from the options and run run.py
            
        c.  To run the test suite:
            i. Open the terminal at the source folder (super-flappy-bird).
            ii. Install pygame module first if you havent already (pip install pygame).
            iii. Run the game with the command "python3 run.py t" or "python run.py t" depending on your installation of python. To tun the command from the Pycharm IDE, go to the terminal in pycharm and sun the command "run.py -t"

            NOTE: The game would open a black screen for about 20 seconds, after which it would print to terminal the tests and their pass/fail conditions.

    3.	Playing the Game

		a.	Select any level, easy mode or hard mode by clicking on your selection. 
        
        b.  Use the SPACE key to jump the bird and avoid the pipes coming your way.

        c.  To obtain powerups, steer the bird into the powerup icons present on the game screen. Upon collision, the bird will gain the power-up. You may have more than one powerup at a time.

        d. You can play any level in the easy mode as well by simply clicking the letter "E" key.

    4. Powerups

        a. Ghost Mode Powerup:
            i.  To obtain this, steer the bird into the ghost icon.
            ii. This mode will allow you to pass through pipes unobstructed.
        
        b. Firepower Powerup:
            i.  To obtain this, steer bird into the fire icon.
            ii. This mode will allow you to shoot projectiles onto oncoming pipes with the press of the letter "F" key.
            iii.    Once a pipe is hit with two projectiles, it will be destroyed.

        c. Score Multiplier Powerup:
            i.  To obtain this, steer bird into the star icon.
            ii. This mode will double your score as you pass through pipes.
        
        d. Coins:
            i. Coins are littered throughout the game. Compete with your friends and see who can get the most!

    5.	Game End

		a.	If the bird hits a pipe, or the scrolling bar at the bottom of the screen, you lose the game.
 
