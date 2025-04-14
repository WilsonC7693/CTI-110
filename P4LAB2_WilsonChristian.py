# Christian Wilson
# 4/13/2025
# P4LAB2
# Use for and while loop to make a multiplication table


# Defining the variable run_again as yes.
run_again = 'yes'

# Determines that as long as the answer is 'yes' the loop will continue but will stop if the answer is 'no'.
while run_again != 'no':
    
    # Get integer from the user.
    user_num = int(input('Enter an integer: '))
    print()    
    # Determining of the entered integer is positive.
    if user_num >= 0:
            
        # Display the multiplication table from the range of 1-12 for the entered value.
        for item in range(1, 13):
            print(f'{user_num} * {item} = {user_num * item}')

    # Displaying the program does not accept negative numbers
    else:
        print('This program does not handle negative numbers.')

    # Asks the user would he like to continue the program or stop it.
    print()
    run_again = input('Would you like to run the program again? ')
    print()

# The Loop has been broken because the user entered 'no'.
print('Exiting program...')


