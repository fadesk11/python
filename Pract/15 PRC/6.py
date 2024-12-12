import turtle

turtle.bgcolor("black")
colors = ["red", "magenta", "cyan", "violet", "purple","white"]
turtle.pensize(3)
for i in range(12):
    turtle.color(colors[i%len(colors)])
    turtle.circle(60)
    turtle.left(30)
turtle.done()
