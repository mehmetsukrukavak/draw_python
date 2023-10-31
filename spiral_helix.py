import turtle

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("Light green")
drawing_screen.title("Python Turtle")


turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

turtle_colors = ["red", "purple", "white", "black", "green", "yellow"]


for i in range(10):
    turtle_instance.color(turtle_colors[i % len(turtle_colors)])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.done()