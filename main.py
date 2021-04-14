#!usr/bin/python3.6

import pygame
import random
from colors import Colors
from paddle import Paddle
from ball import Ball

# Initialising the game engine
pygame.init()

# Open a new window
window_width = 1250
window_height = 800
window_size = (window_width,window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong")

# Global variable that keeps track of the individual scores and the score to win
player1_score = 0
player2_score = 0
score_to_win = 10

# Create the paddles for both players
player1_paddle = Paddle(Colors["red"],20,350)
player2_paddle = Paddle(Colors["indigo"],1220,350)

# Create the ball
ball = Ball(Colors["violet"],window_width / 2,window_height / 2)

# Declaring a variable that proceeds the game if there is no outcome
continueGame = True

# Number of pixels the paddles shift by whenever the right key is pressed
paddleShift = 7

# Radius of the ball
ballRadius = 10
# Dimensions of the paddles
paddle_width = 10
paddle_height = 100

# Creating a clock that controls the rate at which the window updates
clock = pygame.time.Clock()

# Main gameplay loop which is only broken when there is some outcome
while continueGame:
	# Main event loop
	for event in pygame.event.get():
		# If the user did something
		if event.type == pygame.QUIT:
			# The user voluntarily closed the window
			continueGame = False

	# Game logic
	# When the user presses either W and S (player 1) or Up and Down arrow keys,
	# The corresponding paddle moves accordingly
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		# If w is pressed, player 1's paddle moves up
		player1_paddle.moveUp(paddleShift)
	if keys[pygame.K_s]:
		# If s is pressed , player 1's paddle moves down
		player1_paddle.moveDown(paddleShift)
	if keys[pygame.K_UP]:
		# If the Up arrow key is pressed, player 2's paddle moves up
		player2_paddle.moveUp(paddleShift)
	if keys[pygame.K_DOWN]:
		# If the Down arrow key is pressed, player 2's paddle moves down
		player2_paddle.moveDown(paddleShift)
	if keys[pygame.K_x]:
		# If the x is pressed, the game closes
		continueGame = False

	# The ball moves according to the change in its displacement
	ball.x += ball.x_change
	ball.y += ball.y_change

	# Bounce the ball if it hits the sides
	if ball.y + ballRadius >= window_height or ball.y - ballRadius <= 0:
		ball.y_change *= -1

	# Bring the ball back to the center of the screen if it goes past the paddles
	if ball.x + ballRadius >= window_width or ball.x - ballRadius <= 0:
		if ball.x + ballRadius >= window_width:
			# Player 1 scores a point
			player1_score += 1
		elif ball.x - ballRadius <= 0:
			# Player 2 scores a point
			player2_score += 1

		# Wait for 1 second before bringing back the ball
		pygame.time.wait(1000)
		ball.x = window_width / 2
		ball.y = window_height / 2
		ball.x_change = random.choice([-5,5])
		ball.y_change = random.choice([-5,5])

	# If the ball hits either one of the paddles, it should be reflected back
	if player1_paddle.y <= ball.y <= player1_paddle.y + paddle_height and ball.x - ballRadius <= player1_paddle.x + paddle_width:
		ball.x_change *= -1
		ball.x = player1_paddle.x + paddle_width + ballRadius
	if player2_paddle.y <= ball.y <= player2_paddle.y + paddle_height and ball.x + ballRadius >= player2_paddle.x:
		ball.x_change *= -1
		ball.x = player2_paddle.x - ballRadius

	# Drawing all the components onto the screen
	# Firstly, fill the window with cyan
	window.fill(Colors["white"])

	# Draws a line in the middle that serves as a half line
	line_start_pos = ((window_width / 2),0)
	line_end_pos = ((window_width / 2),window_height)
	pygame.draw.line(window,Colors["black"],line_start_pos,line_end_pos,3)

	# Displays the scores of both players
	font = pygame.font.Font("8bitOperatorPlus-Regular.ttf",100)
	text = font.render(str(player1_score),1,Colors["gray"])
	window.blit(text,((window_width / 4) - 25,(window_height / 2) - 75))
	text = font.render(str(player2_score),1,Colors["gray"])
	window.blit(text,(((3 * window_width) / 4) - 25,(window_height / 2) - 75))

	# Draws the paddles at either ends of the window
	pygame.draw.rect(window,player1_paddle.color,(player1_paddle.x,player1_paddle.y,paddle_width,paddle_height))
	pygame.draw.rect(window,player2_paddle.color,(player2_paddle.x,player2_paddle.y,paddle_width,paddle_height))

	# Draws the ball wherever it is on the window
	pygame.draw.circle(window,ball.color,(ball.x,ball.y),ballRadius)

	# If there is a winner, display the winner and exit from the game after 5 seconds
	if player1_score == score_to_win:
		# Player 1 is the winner
		font = pygame.font.Font("8bitOperatorPlus-Regular.ttf",50)
		text = font.render("Player 1 is the winner!",1,Colors["brown"])
		window.blit(text,(window_width / 4,window_height / 4))
		pygame.display.flip()
		pygame.time.wait(5000)
		continueGame = False
	if player2_score == score_to_win:
		# Player 2 is the winner
		font = pygame.font.Font("8bitOperatorPlus-Regular.ttf",50)
		text = font.render("Player 2 is the winner!",1,Colors["brown"])
		window.blit(text,(window_width / 4,window_height / 4))
		pygame.display.flip()
		pygame.time.wait(5000)
		continueGame = False

	# Updating the screen with whatever has been drawn so far
	pygame.display.flip()

	# Limit the clock to 60 frames per second
	clock.tick(60)

# Stops the game engine after the user has exited the main gameplay loop
pygame.quit()