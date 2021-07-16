#Credit to HaltonCoders for the amazing pong code
#Modified and edited by Raytr0

import sys
import pygame
import random

# Text to RGB
# A dictionary where the color word is the key and the rbg equivalent is the value
Colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "darkRed": (55, 0, 0),
    "lightRed": (255, 108, 23),
    "green": (0, 255, 0),
    "darkGreen": (0, 55, 0),
    "blue": (0, 0, 255),
    "darkBlue": (0, 0, 55),
    "navyBlue": (0, 30, 100),
    "lightPurple": (113, 0, 155),
    "darkPurple": (55, 0, 55),
    "lightGrey": (200, 200, 200),
    "paleTurquoise": (175, 238, 238),
    "lightYellow": (255, 240, 23)
}

pygame.init()  # init stands for initialize
clock = pygame.time.Clock()  # Makes a clock in pygame that you can access with the variable 'clock'

# win: window
winWidth, winHeight = 800, 600  # Sets the dimensions of the window
win = pygame.display.set_mode((winWidth, winHeight))  # makes the display(window) with the dimensions you gave
pygame.display.set_caption("Pong")  # sets the name of the window
winColor = pygame.Color('grey12')  # Sets a color for the window that I will use in the future
lineColor = Colors['paleTurquoise']

paddleWidth, paddleHeight = 10, 90  # sets the dimensions of the paddles
paddleColor = Colors['blue']  # the colour of the paddle
paddleSpeed = 5  # the number of pixels the paddle will move by each time

ballDiameter = 16
ballSpeedX = 4
ballSpeedY = 4
ballColor = Colors['red']
ballStartX = winWidth/2 - ballDiameter/2
ballStartY = winHeight/2 - ballDiameter/2
ball = pygame.Rect(ballStartX, ballStartY, ballDiameter, ballDiameter)
# As the height and width are the same, it will be a square


def reset():
    global ballSpeedX, ballSpeedY
    ball.center = (winWidth/2, winHeight/2)
    ballSpeedX *= random.choice((1, -1))
    ballSpeedY *= random.choice((1, -1))


player1Paddle = pygame.rect.Rect(paddleWidth, (winHeight - paddleHeight)//2, paddleWidth, paddleHeight)
player2Paddle = pygame.rect.Rect(winWidth - 2*paddleWidth, (winHeight - paddleHeight)//2, paddleWidth, paddleHeight)
player1score, player2score = 0, 0
scoreFont = pygame.font.Font("freesansbold.ttf", 20)
winFont = pygame.font.Font("freesansbold.ttf", 50)


def reset_game():
    global ballSpeedX, ballSpeedY
    global player1Paddle, player2Paddle
    global player1score, player2score
    ball.center = (winWidth / 2, winHeight / 2)
    ballSpeedX *= random.choice((1, -1))
    ballSpeedY *= random.choice((1, -1))
    player1score = 0
    player2score = 0
    player1Paddle = pygame.rect.Rect(paddleWidth, (winHeight - paddleHeight)//2, paddleWidth, paddleHeight)
    player2Paddle = pygame.rect.Rect(winWidth - 2*paddleWidth, (winHeight - paddleHeight)//2, paddleWidth, paddleHeight)


ballMove = False  # Variable for the whether the ball is moving
while True:
    keysPressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keysPressed[pygame.K_SPACE]:
            ballMove = not ballMove
        if keysPressed[pygame.K_r]:
            reset_game()

    if keysPressed[pygame.K_UP] and player2Paddle.y >= 10:
        player2Paddle.y -= paddleSpeed
    elif keysPressed[pygame.K_DOWN] and player2Paddle.y <= winHeight - (paddleHeight + paddleSpeed + 2):
        player2Paddle.y += paddleSpeed

    if keysPressed[pygame.K_w] and player1Paddle.y >= 10:
        player1Paddle.y -= paddleSpeed
    elif keysPressed[pygame.K_s] and player1Paddle.y <= winHeight - (paddleHeight + paddleSpeed + 2):
        player1Paddle.y += paddleSpeed

    if ballMove:
        ball.x += ballSpeedX
        ball.y += ballSpeedY

        if player1Paddle.colliderect(ball):
            ballSpeedX *= -1
        if player2Paddle.colliderect(ball):
            ballSpeedX *= -1

        if ball.x < 0:
            ballSpeedX = abs(ballSpeedX)
            player2score += 1
            ballMove = False
            reset()
        if ball.y < 0:
            ballSpeedY = abs(ballSpeedY)
        if ball.x + ballDiameter > winWidth:
            ballSpeedX = - abs(ballSpeedX)
            player1score += 1
            ballMove = False
            reset()
        if ball.y + ballDiameter > winHeight:
            ballSpeedY = - abs(ballSpeedY)

    win.fill(winColor)
    pygame.draw.line(win, lineColor, (winWidth//2, 0), (winWidth//2, winHeight))
    pygame.draw.circle(win, lineColor, (winWidth//2, winHeight//2), 50, width=1)
    pygame.draw.ellipse(win, ballColor, ball)
    pygame.draw.rect(win, paddleColor, player1Paddle)
    pygame.draw.rect(win, paddleColor, player2Paddle)

    if player1score == 5:
        player1WinText = scoreFont.render('Player 1 Wins!', False, Colors["white"])
        win.blit(player1WinText, (100, 100))
        resetGameText = scoreFont.render('To play again press "r"', False, Colors["white"])
        win.blit(resetGameText, (100, 400))
        ballMove = False
        ball.center = (winWidth / 2, winHeight / 2)
    elif player2score == 5:
        player2WinText = scoreFont.render('Player 2 Wins!', False, Colors["white"])
        win.blit(player2WinText, (500, 100))
        resetGameText = scoreFont.render('To play again press "r"', False, Colors["white"])
        win.blit(resetGameText, (500, 400))
        ballMove = False
        ball.center = (winWidth / 2, winHeight / 2)

    player1ScoreText = scoreFont.render(str(player1score), False, Colors["white"])
    player2ScoreText = scoreFont.render(str(player2score), False, Colors["white"])
    win.blit(player1ScoreText, (370, 290))
    win.blit(player2ScoreText, (420, 290))

    pygame.display.flip()  # update the pygame window/redraw it
    clock.tick(60)  # in milliseconds