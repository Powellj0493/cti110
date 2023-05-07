#P4HW2-Salary
#Jason Powell
#4/18/2023
#This program determines the pay for multiple employees
# input provided by the user

x = "go"
employ_count = 0

while x == "go":
    employ_name1 = input("Enter employee's name or \"Done\" to Terminate: ")
    if employ_name1 !="Done":
        employ_count += 1
        
    if employ_name1 == "Done":
        break
    
    hrs_work = float(input("Enter number of hours worked: "))
    em_pay_rt = float(input("Enter employee's pay rate: "))
    print()
   
# print employee name and headings

    print("Employee name:",employ_name1)
    print()
    print(f'Hours Worked    Pay Rate        OverTime        Overtime Pay    RegHour Pay       Gross Pay')
    print('---------------------------------------------------------------------------------------------')
    
# overtime pay variables

    if hrs_work >= 40:
        over_time = hrs_work - 40
        overt_py = em_pay_rt * over_time * 1.5
        reghr_py = em_pay_rt * 40
        gross_py = reghr_py + overt_py
        
        
# variables for regular pay

    if hrs_work <= 40:
        reghr_py = hrs_work * em_pay_rt
        no_overtm = hrs_work > 40
        gross_no_ovt = reghr_py
        

# print values
        
        print(f'{hrs_work:<15.1f} {em_pay_rt:<15.1f} {no_overtm:<15.1f} {no_overtm:<15.2f} ${reghr_py:<15.2f}  ${gross_no_ovt:<15.2f}''\n')
         
    else:
        print(f'{hrs_work:<15.1f} {em_pay_rt:<15.1f} {over_time:<15.1f} {overt_py:<15.2f}  ${reghr_py:<15.2f} ${gross_py:<15.2f}''\n')
        
print()
print(f'Total number of employees entered: {employ_count}')
print(f'Total amount paid for overtime: ${overt_py}')
print(f'Total amount paid for regular hours: ${reghr_py} ')
print(f'Total amount paid in gross pay: ${gross_py} ')

