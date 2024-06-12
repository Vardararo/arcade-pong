from turtle import Turtle

# Initialize the ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    # Change the direction of the ball when it collides with a wall    
    def bounce_y(self):
        self.y_move *= -1
    
    # Send the ball towards the other player and slightly increase its speed    
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    
    # Reset the ball in center after each goal    
    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()