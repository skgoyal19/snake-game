from turtle import Turtle, Screen

# creating Score class to show score and game status
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.goto(0,280)
        self.score = 0
        self.write(arg=f'Score : {self.score}', align='center', font=('Ariel', 18, 'normal'))

    # function to update the score
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score : {self.score}', align='center', font=('Ariel', 18, 'normal'))
    
    # function to show game over status
    def game_over(self):
        self.goto(0,0)
        self.write(arg='Game Over', align='center', font=('Ariel', 28, 'normal'))
