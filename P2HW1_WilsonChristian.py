# Christian Wilson
# 3/15/2025
# P2HW1
# Calculate and display travel expenses

# Display the function of the program.
print('This program calculates and displays travel expenses\n')

# Get User's input.
num_budget = float(input('Enter Budget: ',))
print()
destination = input('Enter your travel destination: ')
print()
num_gas = float(input('How much do you think you will spend on gas? '))
print()
num_hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
num_food = float(input('Last, how much do you need for food? '))

# Calculate the remaining balance.
num_balance = num_budget - (num_gas + num_hotel + num_food)
print()

# Display the output section header '------------Travel Expenses------------'
print('------------Travel Expenses------------')

# Displays the travel expenses in an aligned format.
print(f'Location:           {destination}')
print(f'Initial Budget:     ${num_budget:.2f}')
print(f'Fuel:               ${num_gas:.2f}')
print(f'Accomadation:       ${num_hotel:.2f}')
print(f'Food:               ${num_food:.2f}')
print('---------------------------------------')
print()
# Display the result of num_budget - num_gas - num_hotel - num_food  stored in a variable called num_balance on the right of 'Remaining Balance:'
print(f'Remaining Balance:  ${num_balance:.2f}')
 
 
 
