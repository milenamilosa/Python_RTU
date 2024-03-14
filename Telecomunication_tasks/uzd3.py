import turtle

def draw_bar(t, height):
# """ Get turtle t to draw one bar, of height. """
    t.begin_fill() # Added this line
    t.left(90)
    t.forward(height)
    t.write(" "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() # Added this line
    t.penup()
    t.forward(10)
    t.pendown()
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

my_graph = turtle.Turtle() # Create my_graph and set some attributes
# color = ""
my_graph.color("blue", "red")
my_graph.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    if (a<100):
        my_graph.color("blue", "green")
    elif (a>=100 and a <=200):
        my_graph.color("blue", "yellow")
    elif (a>200):
        my_graph.color("blue", "red")
    draw_bar(my_graph, a)

wn.mainloop()