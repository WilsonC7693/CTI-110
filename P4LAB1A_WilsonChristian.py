# Christian Wilson
# 4/5/2025
# P4LAB1A
# Using turtle to make a square and triangle.

import turtle # Allows us to use turtles.
win = turtle.Screen() # Creates a playground for turtles.
turt = turtle.Turtle() # Create a turtle, assign to turt.

# Drawing the Square.
for i in range(4):
   turt.forward(100)
   turt.left(90)
   
# Spaces the shapes apart.
turt.penup() # This picks the pen up without a line.
turt.forward(150) # This moves the pen without a line.
turt.pendown() # This puts the pen down to begin a line.

# Drawing the Triangle
for x in range(3):
    turt.forward(100)
    turt.left(120)

# End commands
win.mainloop() # Wait for user to close window.
