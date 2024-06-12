from turtle import Turtle

MOVE_DISTANCE = 20

# Initialize the paddles and their moving patterns
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.create_paddle()
        self.goto(position)
        
    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
    
    def up(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), self.new_y)
        
    def down(self):
        self.new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), self.new_y)