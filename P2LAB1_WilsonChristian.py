# Christian Wilson
# 3/8/2025
# P2LAB1
# Program that will calculate the diameter, circumference, and area of a circle.

# Defining the radius entered by the user.
circle_radius = float(input('What is the radius of the circle? ' ))
print() # Adding a whitespace

# Defining the value of PI
PI = float(3.14159)
circle_diameter = float(2 * circle_radius) # Calculate circle_diameter
circle_circumf = float(2 * PI * circle_radius) # Calculate circle_circumf
circle_area = float(PI * (circle_radius ** 2)) # Calculate circle_area

# Displays the value of the diameter based on the radius inputted by the user.
print(f'The diameter of the circle is {circle_diameter:.1f} ')
print() # Adding a whitespace

# Displays the value of the circumference based on the radius inputted by the user.
print(f'The circumference of the circle is {circle_circumf:.2f}')
print() # Adding a whitespace

# Displays the value of the area based on the radius inputted by the user.
print(f'The area of the circle is {circle_area:.3f} ')

