 # Christian Wilson
 # 3/1/2025
 # P1HW1
 # Values should be able to change each time the program runs.






print('-----Calculating Exponents----')

print('\n')
num_b = int(input('Enter an integer as the base value: '))
num_e = int(input('Enter an integer as the exponent: '))
num_p = pow(num_b,num_e)

print('\n')
print(num_b, 'raised to the power of', num_e, 'is', num_p, "!!")

print('\n')
print('-----Addition and Subtraction----')

print('\n')
num_start = int(input('Enter a starting integer: '))
num_add = int(input('Enter an integer to add: '))
num_subtract = int(input('Enter an integer to subtract: '))
num_total = num_start + num_add - num_subtract

print('\n')
print(num_start, '+', num_add, '-', num_subtract, 'is equal to', num_total)
