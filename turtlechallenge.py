from turtle import Turtle, Screen, onscreenclick, listen, forward


def dragging(x, y):
    yertle.ondrag(None)
    yertle.setheading(yertle.towards(x, y))
    yertle.goto(x, y)
    yertle.ondrag(dragging)


screen = Screen()

yertle = Turtle('turtle')
yertle.speed('fastest')

yertle.ondrag(dragging)

def move(x, y):
    yertle.penup()
    yertle.setposition(x, y)
    yertle.pendown()


onscreenclick(move)
listen()

forward(0)

screen.mainloop()
