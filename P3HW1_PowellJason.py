#CTI-110
#P3HW1- List
#Jason Powell
#3/22/2023

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print()
print('-------------Results--------------')

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
average = (sum)/6

# Print the lowest, highest, sum and average for grades

print(f'Lowest Grade:    {low:.1f}')
print(f'Highest Grade:   {high:.1f}')
print(f'Sum of Grades:   {sum:.1f}')
print(f'Average:         {average:.2f}')
print('----------------------------------')

# determine letter grade for average

if average >= 90:
    print('Your grade is: A')
elif (average >= 80 and average < 90):
    print('Your grade is: B')
elif (average >= 70 and average < 80):
    print('Your grade is: C')
elif (average >= 60 and average < 70):
    print('Your grade is: D')
else:
    print('Your grade is: F') 
