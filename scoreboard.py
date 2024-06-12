from turtle import Turtle

# Create a scoreboard to track each players points and declare a winner at 5 points
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-80, 220)
        self.write(self.l_score, align="center", font=("Courier", 50, "bold"))
        self.goto(80, 220)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold"))
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def l_winner(self):
        self.goto(0, 0)
        self.write("Player 1 wins!", align="center", font=("Courier", 60, "bold"))
    
    def r_winner(self):
        self.goto(0, 0)
        self.write("Player 2 wins!", align="center", font=("Courier", 60, "bold"))
        