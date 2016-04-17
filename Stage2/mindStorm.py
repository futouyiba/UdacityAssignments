import turtle
import time

brad = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")
brad.shape("triangle")
brad.color("blue")
brad.speed(10)

def drawParallelogram(startAngle,length):
    brad.forward(length)
    brad.left(startAngle)
    brad.forward(length)
    brad.left(180-startAngle)
    brad.forward(length)
    brad.left(startAngle)
    brad.forward(length)
    brad.left(180-startAngle)

divideAngle = 9
axisAngle = 0
while axisAngle < 360:
    drawParallelogram(30,100)
    axisAngle += divideAngle
    brad.left(divideAngle)

time.sleep(10)