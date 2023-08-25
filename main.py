
from turtle import  *
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0,1)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

GAME_IS_ON = True

while GAME_IS_ON:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food)< 15:
            food.refresh()
            snake.extend()
            scoreboard.score_update()

    for segment in snake.SNAKE_BODY:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            GAME_IS_ON = False
            scoreboard.game_over()


    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        GAME_IS_ON = False
        scoreboard.game_over()








screen.exitonclick()


