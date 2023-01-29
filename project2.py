import turtle

pen = turtle.Pen()
turtle.speed(1500)

while True:
    direction = input("Enter direction (forward/backward/left/right): ")

    if direction == "forward":
        pen. forward(100)
    elif direction == "backward":
        pen.backward(100)
    elif direction == "left":
        pen.left(90)
        pen. forward(100)
    elif direction == 'right':
        pen.right(90)
        pen.forward(100)
