from turtle import Turtle, Screen
import time

# sk=Turtle()
# for i in range(4):
#     sk.forward(50)
#     sk.right(90)


screen = Screen()
screen.title('Breakout Game')
screen.setup(width=600, height=800)
screen.tracer(0)

# bricks
COLORS = ['green', 'yellow', 'orange']


class Bricks(Turtle):
    def __init__(self):

        super().__init__()
        self.all_bricks = []
        self.hideturtle()

    def create_brick(self):
        y = 100
        for color in COLORS:
            for row in range(2):
                x = -265
                y += 25
                while x < 300:
                    new_brick = Turtle('square')
                    new_brick.penup()
                    new_brick.shapesize(stretch_wid=1, stretch_len=3)
                    new_brick.color(color)
                    new_brick.goto(x, y)
                    self.all_bricks.append(new_brick)
                    x += 65


# paddle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.color('black')
        self.setpos(position)

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())


# balls

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('blue')
        self.goto(x=0, y=-280)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=-280)
        self.move_speed = 0.1
        self.bounce_y()


# scoreboard

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.score = 0
        self.lives = 3
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 350)
        self.write(f"Score:{self.score}", align='center', font=("Courier", 30, "bold"))
        self.goto(180, 350)
        self.write(f"Lives: {self.lives}", align='center', font=("Courier", 30, "bold"))

    def update_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(" Game Over", align='center', font=("Courier", 30, "bold"))


# main


bricks = Bricks()
paddle = Paddle((0, -300))
ball = Ball()
scoreboard = Scoreboard()
bricks.create_brick()

screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 280 or ball.xcor() < - 280:
        ball.bounce_x()

    if ball.distance(paddle) < 30 and ball.ycor() > -300:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_position()
        scoreboard.update_lives()
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_is_on = False

    for brick in bricks.all_bricks:
        if ball.distance(brick) < 35:
            ball.bounce_y()
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            scoreboard.point()

screen.exitonclick()
