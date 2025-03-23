# Christian Wilson
# 3/22/2025
# P3LAB
# Calculate the entered amount into optimal denominations.

# Gaining user input as float.
money_amount = float(input('Enter the amount of money as a float: $'))

# Converting the entered amount into an integer.
total_amount = int(money_amount * 100)

# Defining the denominations in their integer forms.
dollars = 100
quarters = 25
dimes = 10
nickels = 5
pennies = 1

# Calculating the amount of Dollars.
dollar_amount = total_amount // dollars
total_amount = total_amount - (dollar_amount * dollars)

# Calculating the amount of Quarters.
quarter_amount = total_amount // quarters
total_amount = total_amount - (quarter_amount * quarters)

# Calculating the amount of Dimes.
dime_amount = total_amount // dimes
total_amount = total_amount - (dime_amount * dimes)

# Calculating the amount of Nickels.
nickel_amount = total_amount // 5
total_amount = total_amount - (nickel_amount * nickels)

# Calculating the amount of Pennies.
penny_amount = total_amount // pennies
total_amount = total_amount - (penny_amount * pennies)

# Printing the results in either Plural, Singular, or No Change forms.
if dollar_amount == 1:
    print(f'{dollar_amount} Dollar')
elif dollar_amount > 0:
    print(f'{dollar_amount} Dollars')

if quarter_amount == 1:
    print(f'{quarter_amount} Quarter')
elif quarter_amount > 0:
    print(f'{quarter_amount} Quarters')

if dime_amount == 1:
    print(f'{dime_amount} Dime')
elif dime_amount > 0:
    print(f'{dime_amount} Dimes')

if nickel_amount == 1:
    print(f'{nickel_amount} Nickel')
elif nickel_amount > 0:
    print(f'{nickel_amount} Nickels')

if penny_amount == 1:
    print(f'{penny_amount} Penny')
elif penny_amount > 0:
    print(f'{penny_amount} Pennies')

if money_amount == 0:
    print('No Change')




