import turtle


def draw_shape(some_turtle, radius) :
        some_turtle.circle(radius, 60)
        some_turtle.left(120)
        some_turtle.circle(radius, 60)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("#90ee90")
    petal = turtle.Turtle()
    petal.shape("turtle")
    petal.color("#a47551")
    petal.speed(10)
    petal.width(2)

    the_petals = 15
    the_radius = 150

    for _ in range(the_petals) :
        draw_shape(petal, the_radius)
        petal.left(360 / the_petals)


    stalk = turtle.Turtle()
    stalk.width(3)
    stalk.color("#a47551")
    stalk.shape("turtle")
    stalk.right(90)
    stalk.forward(260)
    window.exitonclick()

draw_flower()

