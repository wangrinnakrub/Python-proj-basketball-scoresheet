import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.fillcolor('red')
t.begin_fill()
for i in [300,200,300,200]:
    t.forward(i)
    t.circle(20, 90)
t.end_fill()

t.up
t.goto(120,65)
t.down

t.fillcolor('white')
t.begin_fill()
for i in [30,120,120]:
    t.left(i)
    t.forward(100)
t.end_fill()

turtle.done()
