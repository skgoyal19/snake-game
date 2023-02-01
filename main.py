# importing modules and classes
import turtle
import time
from snake import Snake
from food import Food
from score import Score

# creating screen object
scr = turtle.Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.title('Welcome to Snake Game')

scr.tracer(0)

game_on = True

# creating snake body object with snake class
snake = Snake(5)
# create food object
food = Food()
# create score object to tarck score
score = Score()

# movement of snake on each key press
scr.listen()
scr.onkey(fun=snake.move_up, key='Up')
scr.onkey(fun=snake.move_down, key='Down')
scr.onkey(fun=snake.move_left, key='Left')
scr.onkey(fun=snake.move_right, key='Right')

# turn on the game
while game_on:
    scr.update()
    # update time of screen for snake speed
    time.sleep(0.15)
    # move the snake by defined unit
    snake.move()

    # detect if the snake catches food, here snake.snake[0] is head of snake
    if snake.snake[0].distance(food) < 15:
        food.random_position()
        score.update_score()
        # increase snake length
        snake.add_segment()
    
    # game over if snake collide with wall
    if snake.snake[0].xcor()>290 or snake.snake[0].xcor()<-290 or snake.snake[0].ycor()>290 or snake.snake[0].ycor()<-290:
        score.game_over()
        game_on = False
    
    # game over of snake head collide with own body
    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            game_on = False
            score.game_over()
    


scr.exitonclick()