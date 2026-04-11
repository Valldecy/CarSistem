import turtle

t = turtle.Turtle()
t.speed(3)

# Corpo do carro
t.color("red")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.end_fill()

# Parte de cima 
t.penup()
t.goto(50, 50)
t.pendown()

t.color("darkred")
t.begin_fill()
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.end_fill()

# Rodas
for x in [40, 160]:
    t.penup()
    t.goto(x, -10)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

turtle.done()