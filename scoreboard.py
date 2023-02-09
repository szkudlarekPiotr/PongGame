from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fastest')
        self.setheading(270)
        self.setpos(0, 275)
        self.hideturtle()
        self.p1score = 0
        self.p2score = 0
        self.update_scoreboard()

    def draw_middle_line(self):
        self.setpos(0, 275)
        while self.ycor() >= -300.0:
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)

    def update_scoreboard(self):
        self.clear()
        self.draw_middle_line()
        self.goto(-40, 250)
        self.write(f'{self.p1score}', font=FONT)
        self.goto(24, 250)
        self.write(f'{self.p2score}', font=FONT)
        if self.p1score == 10 or self.p2score == 10:
            self.game_over()
            return True

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 48, "normal"))
