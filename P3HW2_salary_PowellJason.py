#CTI-110
#P3HW2-Salary
#Jason Powell
#3/23/2023

#This program determines the pay for an employee

# input provided by the user

employ_name = input("Enter employee's name: ")
hrs_work = float(input("Enter number of hours worked: "))
em_pay_rt = float(input("Enter employee's pay rate: "))

print('---------------------------------------')

# print employee name and headings 

print("Employee name:",employ_name)
print(f'Hours Worked   Pay Rate   OverTime   Overtime Pay      RegHour Pay      Gross Pay')

# overtime pay variables

over_time = hrs_work - 40
overt_py = em_pay_rt * over_time * 1.5

# variables for regular pay
reghr_py = hrs_work * em_pay_rt 
gross_py = reghr_py + overt_py
no_overtm = hrs_work > 40
gross_no_ovt = reghr_py

# print values
if hrs_work >= 40:
    reghr_py = em_pay_rt * 40
    gross_py = reghr_py + overt_py
if hrs_work < 40:
    print(f'{hrs_work:.1f}           {em_pay_rt:.1f}        {no_overtm:.1f}       {no_overtm:.2f}          ${reghr_py:.2f}          ${gross_no_ovt:.2f}')
else:
    print(f'{hrs_work:.1f}           {em_pay_rt:.1f}        {over_time:.1f}       {overt_py:.2f}            ${reghr_py:.2f}          ${gross_py:.2f}')


