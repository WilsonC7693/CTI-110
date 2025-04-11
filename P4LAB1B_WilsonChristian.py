# Christian Wilson
# 4/5/2025
# P4LAB1B
# Using turtle to draw my initials.

import turtle # Allows us to use turtles.
win = turtle.Screen() # Creates a playground for turtles.
turt = turtle.Turtle() # Create a turtle, assign to turt.

# Defines the size, shape, and color of my pen.
turt.pensize(4)
turt.shape("turtle")
turt.color("Gold")

# Draws my C
turt.backward(300)          
turt.right(90)
turt.backward(300)
turt.left(90)
turt.forward(300)


turt.penup() # This picks the pen up without a line.
turt.forward(200) # This moves the pen without a line.
turt.pendown() # This puts the pen down to begin a line.

   
# Draws my W.
turt.right(80)
turt.forward(300)
turt.left(150)
turt.forward(180)
turt.right(145)
turt.forward(175)
turt.left(150)
turt.forward(310)

# End commands
win.mainloop() # Wait for user to close window.
