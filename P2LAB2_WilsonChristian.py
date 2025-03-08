# Christian Wilson
# 3/8/2025
# P2LAB1
# Code that uses a dictionary to store user input and displays output to the user.

# Creating the dictionary.
economy_dict = { 'Camaro' : 18.21,
                 'Prius' : 52.36,
                 'Model S' : 110,
                 'Silverado' : 26
                 }

# Defining keys to equate to the keys of the dictionary.
keys = economy_dict.keys()
print(keys) # Printing the value of keys.
print()# Add a whitespace.

# Prompts the user to enter a vehicle from the list.
car = input('Enter a vehicle to see it\'s mpg: ' )
print()# Add a whitespace.

# Matches the key and value to complete a sentence.
print(f'The {car} gets {economy_dict[car]} mpg.')
print()# Add a whitespace.

# Prompts the user to enter their intended travel distance.
miles_to_drive = float(input(f'How many miles will you drive the {car}? '))
print()# Add a whitespace.

# Defines gallons_needed to eauate to the total of the travel distance divided by the selected vehicles MPG
gallons_needed = float(miles_to_drive / economy_dict[car])
print(f'{gallons_needed :.2} gallon(s) are needed to drive the {car} {miles_to_drive} miles.')




