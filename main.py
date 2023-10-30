import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

#square
'''
for i in range(4):
    turtle_instance.forward(250)
    turtle_instance.left(90)
'''
#star
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(250)

'''
#polygon
number_sides = 5
angle = 360 / number_sides
side_length = 250
for i in range(number_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)
'''

turtle.done()