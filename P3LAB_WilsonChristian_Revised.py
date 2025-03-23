# Christian Wilson
# 3/22/2025
# P3LAB
# Calculate the entered amount into optimal denominations.

# Gaining user input as float.
money_amount = float(input('Enter the amount of money as a float: $'))

# Converting the entered amount into an integer.
total_amount = round(money_amount * 100)

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

if money_amount == 0:
    print('No Change')






