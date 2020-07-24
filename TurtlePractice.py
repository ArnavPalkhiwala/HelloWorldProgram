import turtle
import math

turt = turtle.Turtle()

turt.getscreen().bgcolor("dark blue")

turt.color("orange", "black")

turt.speed(10)

def star(turtle, size):
	if size <=10:
		return
	else:
		for i in range(5):
			turtle.forward(size)
			star(turtle, size * .5)
			turtle.left(216)


star(turt, 100)

turtle.done()