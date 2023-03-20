from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"



# When the turtle hits a car, GAME OVER should be displayed in the centre.
# If you get stuck, check the video walkthrough in Step 7.

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(180, 260)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(180, 260)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER \nYour final Score: {self.score}", align=ALIGN, font=FONT)
