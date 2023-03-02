# This program Calculates and displays travel expenses with float values
# March 1, 2023
# CTI-110 P2HW1 - Travel 
# Jason Powell
#

print('This program calculates and displays travel expenses')
print()
my_budget = float(input('Enter Budget: '))
print()
my_travel = input('Enter your travel destination: ')
print()
my_gas = float(input('How much do you think you will spend on gas?: '))
print()
my_hotel = float(input('Approximately, how much will you need for accomodation/hotel?: '))
print()
my_food = float(input('Last, how much do you need for food?: '))
print()
print('---------------Travel Expenses-------------------')
print(f'Location:          {my_travel}')
print(f'Initial Budget:    ${my_budget}')
print(f'Fuel               ${my_gas}')
print(f'Accomodation:      ${my_hotel}')
print(f'Food:              ${my_food}')
print('-------------------------------------------------')
rem_bal = my_budget - my_gas - my_hotel - my_food
print(f'Remaining Balance: ${rem_bal}')




  
 
