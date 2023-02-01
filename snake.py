import turtle


MOVE_DISTANCE = 20

class Snake:

    # make body of the snake
    def __init__(self, snake_length):
        self.snake=[]
        x=0
        for i in range(snake_length):
            tim = turtle.Turtle()
            tim.shape('square')
            tim.color('white')
            tim.penup()
            tim.goto(x,0)
            self.snake.append(tim)
            x -= 20
    
    # add one segment at end of snake
    def add_segment(self):
        segment = turtle.Turtle()
        segment.shape('square')
        segment.color('white')
        segment.penup()
        pos = self.snake[-1].position()
        segment.goto(pos)
        self.snake.append(segment)
    
    # move the snake by changing the position of segment to its previous segment position
    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x,y)
        self.snake[0].forward(MOVE_DISTANCE)
    
    def move_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
    
    def move_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
    
    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
    
    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)