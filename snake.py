
POSITIONS=[(0,0),(-20,0),(-40,0)]
from turtle import *
class Snake:

    def __init__(self) -> None:
        self.SNAKE_BODY = []
        self.create_snake()
        self.head = self.SNAKE_BODY[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_body(position)



    def add_body(self,position):
        snake = Turtle()
        snake.color("white")
        snake.penup()
        snake.shape("square")
        snake.goto(position)
        self.SNAKE_BODY.append(snake)

    def extend(self):
        self.add_body(self.SNAKE_BODY[-1].position())

    def move(self):
        for part in range(len(self.SNAKE_BODY) - 1, 0, -1):
            self.new_xcor = self.SNAKE_BODY[part - 1].xcor()
            self.new_ycor = self.SNAKE_BODY[part - 1].ycor()
            self.SNAKE_BODY[part].goto(self.new_xcor, self.new_ycor)
        self.SNAKE_BODY[0].forward(20)

    def up(self):
        if self.SNAKE_BODY[0].heading() != 270:
            self.SNAKE_BODY[0].setheading(90)

    def down(self):
        if self.SNAKE_BODY[0].heading() != 90:
            self.SNAKE_BODY[0].setheading(270)

    def left(self):
        if self.SNAKE_BODY[0].heading() != 0:
            self.SNAKE_BODY[0].setheading(180)

    def right(self):
        if self.SNAKE_BODY[0].heading() != 180:
            self.SNAKE_BODY[0].setheading(0)








