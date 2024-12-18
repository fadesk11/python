import turtle

colors = ["red", "cyan", "green", "black", "purple", "magenta"]
for i in colors:
    turtle.color(i)
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
turtle.done()
