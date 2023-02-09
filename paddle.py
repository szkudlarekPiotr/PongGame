from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('rectangle')
        self.color('white')
        self.seth(270)
        self.pu()
        self.hideturtle()

    def set_player(self, xcor, ycor):
        self.setx(xcor)
        self.sety(ycor)
        self.showturtle()

    def move_down(self):
        if self.ycor() <= -175:
            pass
        else:
            self.forward(20)

    def move_up(self):
        if self.ycor() >= 295:
            pass
        else:
            self.backward(20)
