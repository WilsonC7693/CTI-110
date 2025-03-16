# Christian Wilson
# 3/15/2025
# P2HW2
# Calculating grade average.

# User inputs grades for Modules 1-6.
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Adding the grades entered into a list.
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Adding a whitespace.
print()

# Displaying Results header.
print('------------Results------------')

# Defining the lowest, highest, sum, and average of the entered grades.
low = min(grades)
high = max(grades)
sum_of_all = sum(grades)
avg = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6) / 6

# Determining average based on user's input.
print(f'Lowest Grade:       {low:.1f}')
print(f'Highest Grade:      {high:.1f}')
print(f'Sum of Grades:      {sum_of_all:.1f}')
print(f'Average:            {avg:.2f}')

# Displaying bottom border of the results.
print('----------------------------------------')






