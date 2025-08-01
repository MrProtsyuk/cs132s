import turtle

def drawSquare(turtle_length, t, ui):
    t.forward(turtle_length)
    t.right(90)
    t.forward(turtle_length)
    t.right(90)
    t.forward(turtle_length)
    t.right(90)
    t.forward(turtle_length)

def recursiveCall(turtle_length, t, ui):
    t.forward(turtle_length)
    if ui > 0:
        drawSquare(turtle_length // 2, t, ui - 1)
    t.left(90)
    t.forward(turtle_length)
    t.left(90)
    t.forward(turtle_length)
    if ui > 0:
        drawSquare(turtle_length // 2, t, ui - 1)
    t.left(90)
    t.forward(turtle_length)

# Main function that takes user input and draws the I
def main():
    user_input = int(input("Enter recursion levels: "))
    t_win = turtle.Screen()
    t_win.bgcolor("Black")
    t = turtle.Turtle()
    t.hideturtle()
    t.color("White")
    t.speed(0)
    t.left(45)
    t.down()
    turtle_length = 100
    drawSquare(turtle_length, t, user_input + user_input + 1)
    t_win.exitonclick()
main()