from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen and set the paddles starting positions
RIGHT_STARTING_POS = (350, 0)
LEFT_STARTING_POS = (-350, 0)

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Arcade Pong Game")
screen.tracer(0)

r_paddle = Paddle(RIGHT_STARTING_POS)
l_paddle = Paddle(LEFT_STARTING_POS)

# Initialize the ball and scoreboard from respective classes
ball = Ball()
scoreboard = Scoreboard()

# Create event listeners for the two paddles
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    
    ball.move()
    
    #Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #Detect collison with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect if a paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
    
    # Game to 5    
    if scoreboard.l_score == 5:
        scoreboard.l_winner()
        game_is_on = False
    elif scoreboard.r_score == 5:
        scoreboard.r_winner()
        game_is_on = False


screen.exitonclick()