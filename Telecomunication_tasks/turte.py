# 1.uzdevums
import turtle
def draw_star(t):
   for _ in range(5):
        t.forward(100)
        t.right((144))
def draw_complex_shape(t):
   for _ in range(12):
        t.forward(35)
        my_turtle.pendown()
        t.forward(5)
        my_turtle.penup()
        t.forward(10)
        my_turtle.stamp()
        t.backward(50)
        t.right(30)

wn = turtle.Screen()
wn.bgcolor("lightgreen")        
my_turtle = turtle.Turtle()
my_turtle.speed(10)
draw_star(my_turtle)
my_turtle.penup()
my_turtle.goto(200,0)
my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.stamp()
draw_complex_shape(my_turtle)
my_turtle.penup()


# 2.uzdevums
my_turtle.goto(-400,-150)
my_turtle.color("pink")
my_turtle.pensize(5)
for i in range(5):
    for _ in range(5):
        my_turtle.pendown()
        my_turtle.forward(100)
        my_turtle.right((144))
    my_turtle.penup()
    my_turtle.forward(350)
    my_turtle.right((144))

my_turtle.hideturtle()
turtle.done()