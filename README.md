README

This is a recreation of Flappy Bird coded for Project 3 of EECS 448 in Python using the Pygame module. Commented lines and classes not mentioned in the Requirements Engineering Artifact, Design Paradigms document, Software Architecture document, UML Modeling Diagram and Design Patterns are the framework for Project 4 implementation.

Requirements:

	1.	Approval from GTA

How the project works is as follows:

	1.	Game Setup

		a.	On loading the game, a screen appears with the caption Flappy Bird. The screen has a background image and a scrolling bar below. 
		b.	A bird with flapping wings is shown along with instructions on how to start the game.

	2.	Running the game

		a.	To run the game directly:
			i.	Install the pygame module from the official pygame website, and run the game from the terminal as you would run a normal program.

		b.	To run the game using an IDE like Pycharm:
			i.	Go to FIle -> Settings -> Project: super-flappy-bird -> Python Interpreter and click the ‘+’ icon on the bottom left corner of the table.
			ii.	Search for the pygame module and click Install Package.
			iii.	To run the game for the first time go to the game class and press Shift+Alt+F10. Select game and click run.

		c.	To play in easy mode for testing purposes, you can use the up and down arrow keys to move the bird.
		d.	To play the game normally, use the space bar.

3.	Playing the Game

		a.	Use the SPACE key to jump the bird and avoid the pipes coming your way.

4.	Game End

		a.	If the bird hits a pipe, or the scrolling bar at the bottom of the screen, you lose the game.
 
