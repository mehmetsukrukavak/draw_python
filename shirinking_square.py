import turtle

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("Light green")
drawing_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shirinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

size = 350
while size > 10:
    shirinkingSquare(size)
    size = size - 20


turtle.done()
