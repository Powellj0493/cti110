# This program Calculates and displays travel expenses
# February 16, 2023
# CTI-110 P1HW2 - Travel Expense
# Jason Powell
#

print('This program calculates and displays travel expenses')
print()
my_budget = int(input('Enter Budget: '))
print()
my_travel = input('Enter your travel destination: ')
print()
my_gas = int(input('How much do you think you will spend on gas?: '))
print()
my_hotel = int(input('Approximately, how much will you need for accomodation/hotel?: '))
print()
my_food = int(input('Last, how much do you need for food?: '))
print()
print('---------------Travel Expenses-------------------')
print('Location:',my_travel)
print('Initial Budget:',my_budget)
print()
print('Fuel',my_gas)
print('Accomodation:',my_hotel)
print('Food:',my_food)
print()
print('Remaining Balance:',my_budget - my_gas - my_hotel - my_food)





