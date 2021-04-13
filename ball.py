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
		self.x_change = random.choice([-5,5])
		self.y_change = random.choice([-5,5])