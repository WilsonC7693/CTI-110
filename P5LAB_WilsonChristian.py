# Christian Wilson
# 4/19/2025
# P5LAB
# Use of loops, functions and module import to complete assignments

# Genertating the random number.
import random

# Defining the function that will conduct denomination determining.
def disperse_change(total_amount):
    
    # Converting the entered amount into an integer.
    total_amount = round(total_amount * 100)

    # Calculating the amount of Dollars.
    dollar_amount = total_amount // 100
    total_amount = total_amount - (dollar_amount * 100)

    # Calculating the amount of Quarters.
    quarter_amount = total_amount // 25
    total_amount = total_amount - (quarter_amount * 25)

    # Calculating the amount of Dimes.
    dime_amount = total_amount // 10
    total_amount = total_amount - (dime_amount * 10)

    # Calculating the amount of Nickels.
    nickel_amount = total_amount // 5
    total_amount = total_amount - (nickel_amount * 5)

    # Defining the amount of Pennies.
    penny_amount = total_amount

    # Printing the results in either Plural, Singular, or No Change forms.
    if dollar_amount > 0:
        if dollar_amount == 1:
            print(f'{dollar_amount} Dollar')
        else:
            print(f'{dollar_amount} Dollars')

    if quarter_amount > 0:
        if quarter_amount == 1:
            print(f'{quarter_amount} Quarter')
        else:
            print(f'{quarter_amount} Quarters')

    if dime_amount > 0:
        if dime_amount == 1:
            print(f'{dime_amount} Dime')
        else:
            print(f'{dime_amount} Dimes')

    if nickel_amount > 0:
        if nickel_amount == 1:
            print(f'{nickel_amount} Nickle')
        else:
            print(f'{nickel_amount} Nickels')

    if penny_amount > 0:
        if penny_amount == 1:
            print(f'{penny_amount} Penny')
        else:
            print(f'{penny_amount} Pennies')

    if total_amount == 0:
        print('No Change')


# Creating the main function where the main logic of the code will go.
def main():
    
    # Generating the amount owed.
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f'You owe ${amount_owed:.2f}')

    # Creating a variable to represent the money put into self-checkout.
    money_inserted = float(input('How much cash will you put in the self-checkout? '))

    # Calculating the change the customer recieves.
    total_amount = money_inserted - amount_owed
    print(f'Change is: ${total_amount:.2f}')
    print()

    # Calling the disperse change function.
    disperse_change(total_amount)

# Calling the main function
main()







