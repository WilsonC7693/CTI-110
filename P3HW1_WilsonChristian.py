# Christian Wilson
# 3/30/2025
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.


# User inputs grades for six modules.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determining the lowest, highest , and total of the entered grades.
low = min(grades)
high = max(grades)
total = sum(grades)

# Determining the average of the entered grades.
avg = total/len(grades)

# Displaying the lowest, highest, total, and average of all entered grades.
print('-----------Results------------')
print(f'Lowest Grade:      {low:.1f}')
print(f'Highest Grade:     {high:.1f}')
print(f'Sum of Grades:     {total:.1f}')
print(f'Average:           {avg:.2f}')
print('---------------------------------------')

# Displaying a letter grade based upon the average.
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
        print('Your grade is: B')
elif avg >= 70:
      print('Your grade is: C')
elif avg >= 60:
        print('Your grade is: D')
else:
    print('Your grade is: F')




