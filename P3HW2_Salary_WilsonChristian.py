# Christian Wilson
# 3/30/2025
# P3HW2_Salary_
# Calculate amount employee should be paid.

# Prompt the user to input the name of the employee.
em_name = input("Enter employee's name: ")

# Prompt the user to input the number of hours the employee worked .
hours_worked = float(input('Enter number of hours worked: '))

# Prompt the user to input the employee's pay rate.
pay_rate = float(input("Enter employee's pay rate: "))

# Asses if the employee has worked overtime.
if hours_worked > 40:
    #Calculates the overtime hours.
    over_hours = hours_worked - 40
else:
    over_hours = 0

# Calculate the amount owed to the employee for overtime hours.
over_pay = over_hours * 1.5 * pay_rate

# Calculate the amount the employee should be paid for regular hours worked.
reg_pay = 40 * pay_rate

# Calculate the total amount to be paid to the employee.
gross_pay = reg_pay + over_pay
print("-------------------------------------")

# Display the result
print('Employee Name:\t', em_name)
print()
print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay        Gross Pay')
print('-------------------------------------------------------------------------------------------------')
print(f'{hours_worked:<13.1f}  {pay_rate:<10.1f}  {over_hours:<10.1f}  {over_pay:<18.2f}  ${reg_pay:<16.2f}  ${gross_pay:<15.2f}')
