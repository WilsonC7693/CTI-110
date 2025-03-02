# Christian Wilson
# 3/2/2025
# P1HW2
# Calculate and display travel expenses

# Display the function of the program.
print('This program calculates and displays travel expenses\n')

# Input the budget amount on the right of 'Enter Budget: ' and store it in a variable called num_budget  
num_budget = int(input('Enter Budget: ',))

# Add a blank line (Whitespace)
print()

# Input the destination on the right of 'Enter your travel destination: ' and store it in a variable called destination 
destination = input('Enter your travel destination: ')

# Add a blank line (Whitespace)
print()

# Input the amount intended to use on gas on the right of 'How much do you think you will spend on gas? ' and store it in a variable called num_gas
num_gas = int(input('How much do you think you will spend on gas? '))

# Add a blank line (Whitespace)
print()

# Input the amount intended to use on accomodations on the right of 'Approximately, how much will you need for accomodation/hotel? ' and store it in a variable called num_hotel
num_hotel = int(input('Approximately, how much will you need for accomodation/hotel? '))

# Add a blank line (Whitespace)
print()

# Input the amount intended to use on food on the right of 'Last, how much do you need for food? ' and store it in a variable called num_food
num_food = int(input('Last, how much do you need for food? '))

# Subtract num_gas, num_hotel, and num_food from num_budget and store the result in a variable called num_balance
num_balance = num_budget - num_gas - num_hotel - num_food

# Add a blank line (Whitespace)
print()

# Display the output section header '------------Travel Expenses------------'
print('------------Travel Expenses------------')

# Display the previously entered destination, in a variable called destination, on the right of 'Location:'
print('Location:', destination)

# Display the previously entered budget amount, in a variable called num_budget, on the right of 'Initial Budget:'
print('Initial Budget:', num_budget)

# Add a blank line (Whitespace)
print()

# Display the previously entered fuel expense, in a variable called num_gas, on the right of 'Fuel:'
print('Fuel:', num_gas)

# Display the previously entered accomodations expense, in a variable called num_hotel, on the right of 'Accomadation:'
print('Accomadation:', num_hotel)

# Display the previously entered food expense, in a variable called num_food, on the right of 'Food:'
print('Food:', num_food)

# Add a blank line (Whitespace)
print()

# Display the result of num_budget - num_gas - num_hotel - num_food  stored in a variable called num_balance on the right of 'Remaining Balance:'
print('Remaining Balance:', num_balance)
 
 
 
