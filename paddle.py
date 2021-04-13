#!usr/bin/python3.6

# This class represents a paddle which can be controlled by the player
class Paddle:

	# Parametrised constructor that creates a paddle whose top-left corner is (x,y)
	def __init__(self,color,x,y):
		self.color = color
		self.x = x
		self.y = y

	# Function that lets the paddle move up by a few pixels
	def moveUp(self,pixels):
		self.y -= pixels
		if self.y < 0:
			# If the paddle is going beyond the boundaries of the window
			self.y = 0

	# Function that lets the paddle move down by a few pixels
	def moveDown(self,pixels):
		self.y += pixels
		if self.y > 700:
			# If the paddle is going beyond the boundaries of the window
			self.y = 700