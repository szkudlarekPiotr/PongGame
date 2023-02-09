import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.bgcolor('black')
screen.title("PONG!")
screen.setup(800, 600)
screen.tracer(0)
poly = ((20, 0), (0, 0), (0, 100), (20, 100))
screen.register_shape('rectangle', poly)

player1 = Paddle()
player1.set_player(-370, 50)
player2 = Paddle()
player2.set_player(385, 50)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.move_down, "s")
screen.onkey(player2.move_down, "k")
screen.onkey(player1.move_up, 'w')
screen.onkey(player2.move_up, 'i')

running = True
while running:
    screen.update()
    time.sleep(0.1)
    ball.move()
    ball.wall_collision()
    ball.paddle_collision(player1)
    ball.paddle_collision(player2)

    if ball.if_scored(scoreboard):
        player1.set_player(-370, 50)
        player2.set_player(385, 50)
        if scoreboard.update_scoreboard():
            running = False

    elif ball.if_scored(scoreboard):
        player1.set_player(-370, 50)
        player2.set_player(385, 50)
        if scoreboard.update_scoreboard():
            running = False

screen.exitonclick()
