import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
drawing_area = turtle.Screen()
my_turtle.penup()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

for i in range(3):
    turtle.forward(300)
    turtle.left(120)


turtle.done()
