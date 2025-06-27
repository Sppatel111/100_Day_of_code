import random
from turtle import Turtle, Screen
import time

screen = Screen()
screen.title('Space Invaders')
screen.setup(width=600, height=800)
screen.tracer(0)


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        self.lives = 5
        self.display = Turtle()
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(0, 350)
        self.update_score()

    def update_score(self):
        self.display.clear()
        self.display.write(f"Score: {self.score}  Lives: {self.lives}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def decrease_life(self):
        self.lives -= 1
        self.update_score()


class Aeroplane(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.color('red')
        self.shapesize(2)
        self.penup()
        self.goto(random.randint(-280,280),300)
        self.setheading(270)

    def move(self):
        self.speed('slowest')
        self.forward(1)



class Shot(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_gun(position)

    def create_gun(self, position):
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.color('blue')
        self.setpos(position)

    def right(self):
        new_x = self.xcor() + 20
        if new_x <280:
            self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 20
        if new_x > -280:
            self.goto(new_x, self.ycor())

    def shoot(self):
        bullet = Bullet(self.xcor(), self.ycor() + 20)
        bullets.append(bullet)


class Bullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('circle')
        self.color('green')

        self.penup()
        self.goto(x, y)
        self.setheading(90)

    def move(self):
        self.forward(10)


gun = Shot((0, -300))
scoreboard = ScoreBoard()

bullets = []
aeroplanes = []

for _ in range(5):
    aeroplane=Aeroplane()
    aeroplanes.append(aeroplane)

screen.listen()
screen.onkeypress(gun.right, "Right")
screen.onkeypress(gun.left, 'Left')
screen.onkey(gun.shoot, 'space')

game_is_on = True
while game_is_on:
    screen.update()

    for aeroplane in aeroplanes:
        aeroplane.move()
        time.sleep(0.002)

        if aeroplane.ycor()<-400:
            scoreboard.decrease_life()
            aeroplane.goto(random.randint(-280,280),400)
            if scoreboard.lives <=0:
                game_is_on=False
                scoreboard.display.goto(0,0)
                scoreboard.display.write("Game Over", align="center", font=("Arial", 36, "normal"))

    for bullet in bullets:
        bullet.move()

        for aeroplane in aeroplanes:
            if bullet.distance(aeroplane) < 20:
                bullet.hideturtle()
                bullet.goto(1000, 1000)
                bullets.remove(bullet)
                aeroplane.goto(random.randint(-280, 280), 400)
                scoreboard.increase_score()
                break


screen.mainloop()
