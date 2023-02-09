from turtle import Turtle
import random

HEADINGS = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fast')
        self.seth(random.choice(HEADINGS))
        self.pu()

    def move(self):
        self.forward(20)

    def wall_collision(self):
        if self.ycor() >= 290 or self.ycor() <= -280:
            if self.heading() == 135 or self.heading() == 315:
                self.seth(self.heading() + 90)
            else:
                self.seth(self.heading() - 90)

    def paddle_collision(self, player):
        pycor = int(player.ycor())
        pxcor = int(player.xcor())
        if int(self.ycor()) in range(pycor - 105, pycor + 5) and int(self.xcor()) in range(pxcor - 20, pxcor):
            if self.heading() == 45 or self.heading() == 225:
                self.seth(self.heading() + 90)
            else:
                self.seth(self.heading() - 90)

    def if_scored(self, scores):
        if self.xcor() >= 420:
            self.reset_ball()
            scores.p1score += 1
            scores.update_scoreboard()
            return True
        elif self.xcor() <= -420:
            self.reset_ball()
            scores.p2score += 1
            scores.update_scoreboard()
            return True

    def reset_ball(self):
        self.goto(0, 0)
        self.seth(random.choice(HEADINGS))
