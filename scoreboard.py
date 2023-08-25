from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.penup()
        self.hideturtle()
        self.goto(-3, 270)
        self.color("white")
        self.write(f"Score:{self.SCORE}",font=("Arial",20),align="center")

    def score_update(self):
        self.clear()
        self.SCORE+=1
        self.write(f"Score:{self.SCORE}", font=("Arial", 20),align="center")

    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER",font=("Arial",24,"bold"),align="center")


