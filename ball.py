#!usr/bin/python3.6

import random

# This class represents the ball which will be hit back and forth by the players
class Ball:

	# Parametrised constructor that creates a ball initially centered at (x,y)
	def __init__(self,color,x,y):
		self.color = color
		self.x = x
		self.y = y

		# The change in the ball's displacement over time
		self.x_change = 0
		self.y_change = 0

	def reset_displacement(self):
		while True:
			self.x_change = random.randrange(-5,5)
			self.y_change = random.randrange(-5,5)

			if self.x_change != 0 and self.y_change != 0:
				break