from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("black")
        self.left(90)
        self.refresh_position()
    def refresh_position(self):
        self.goto(STARTING_POSITION)
    def move(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)
    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False