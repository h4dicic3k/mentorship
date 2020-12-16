import turtle
screen = turtle.Screen()
screen.bgcolor("yellow")
kaplumbaga = turtle.Turtle(shape="turtle")
kaplumbaga.circle(50)

kaplumbaga.penup()
kaplumbaga.setposition(-120,0)
kaplumbaga.pendown()
kaplumbaga.circle(50)

kaplumbaga.penup()
kaplumbaga.setposition(60,60)
kaplumbaga.pendown()
kaplumbaga.circle(50)

kaplumbaga.penup()
kaplumbaga.setposition(-60,60)
kaplumbaga.pendown()
kaplumbaga.circle(50)

kaplumbaga.penup()
kaplumbaga.setposition(-180,60)
kaplumbaga.pendown()
kaplumbaga.circle(50)

turtle.getscreen()._root.mainloop()