# HOMEWORK04 for CS132SP_2025
import turtle

# Much of this was expounded upon from the example of 
# the tree branches in 4.7

# Draws the top of the I, think of it as the branch of the tree
def drawI(turtle_length, t, ui):
    if ui >= 0:
        t.forward(turtle_length)
        t.right(90)
        # Recursive call
        drawI(turtle_length // 1.4 , t, ui - 1)
        t.left(180)
        drawDot(t)
        # Recursive call
        drawI(turtle_length // 1.4 , t, ui - 1)
        t.right(90)
        drawDot(t)
        t.backward(turtle_length)   

# Draws the dot at the end of the I
def drawDot(t):
    t.dot(3, "White")

# Main function that takes user input and draws the I
def main():
    user_input = int(input("Enter recursion levels: "))
    t_win = turtle.Screen()
    t_win.bgcolor("Black")
    t = turtle.Turtle()
    t.hideturtle()
    t.color("White")
    t.speed(0)
    t.left(90)
    t.down()
    drawDot(t)
    turtle_length = 120
    # Draws the first half of the I
    # User input is doubled and then added 1 to make the I match the example
    drawI(turtle_length, t, user_input + user_input + 1)
    # Flips the turtle around at the center
    t.left(180)
    # Draws the second half of the I
    drawI(turtle_length, t, user_input + user_input + 1)
    t_win.exitonclick()
main()