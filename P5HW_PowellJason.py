#create menu driven math quiz
#4/27/2023
#CTI-110 P5HW - Math Quiz
#Jason Powell

print('Welcome to Math Quiz''\n')

print('MAIN MENU')
print('--------------------')
print(f'1. Adding Random Numbers')
print(f'2. Subtracting Random Numbers')
print(f'3. Exit''\n')

import math
import random

def add(x,y):
    return(x + y)

def sub(a,b):
    return (a - b)
    

j = 1
t = 2
g = 0
number1 = random.randint(10, 99)
number2 = random.randint(10, 99)
user_in = input(f'Please choose one of the menu options: ')


while user_in != '3':
    if user_in == '1':                # addition loop
        print(f'  {number1}')
        print(f'+ {number2}''\n')
        
        ad_ans = add(number1,number2) # random problem generator
      
        
        print('Enter answer.')
       
        
        ad_user_in = int(input())
        if ad_user_in == 3:
                break
        g = g + 1

        if ad_user_in == ad_ans:
            print('Congratulations!!!! Your answer is correct.')
            print(f'Number of guesses:',{g})
            print()
            print('MAIN MENU')
            print('--------------------')
            print(f'1. Adding Random Numbers')
            print(f'2. Subtracting Random Numbers')
            print(f'3. Exit''\n')

            win_user_in = (input())
            if win_user_in == '3':  
                break
          
        elif ad_user_in < ad_ans:
            print('Sorry, guess is too low''\n')
            
            
        else:
            print('Sorry, guess is too high''\n')
    
    elif user_in == '2':               #subtraction loop
        print(f'  {number1}')
        print(f'- {number2}''\n')
        sub_ans = sub(number1,number2)

        print('Enter answer')

            
        sub_user_in = int(input())
        g = g + 1
        
        if sub_user_in == 3:
            break
            
        if sub_user_in == sub_ans:
            print('Congratulations!!!! Your answer is correct.')
            print(f'Number of guesses:',{g})
            print()
            print('MAIN MENU')
            print('--------------------')
            print(f'1. Adding Random Numbers')
            print(f'2. Subtracting Random Numbers')
            print(f'3. Exit''\n')
            break
          
        elif sub_user_in < sub_ans:
            print('Sorry, guess is too low''\n')
            
            
        else:
            print('Sorry, guess is too high''\n')
    

    else:
        print('unrecognized command')
        break
