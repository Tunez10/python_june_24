'''
write a program that takes a list or range of numbers.
1. checks if the number is an odd number or an even number.
2. Below
    checks if the number is divisible by 3 and print (fizz)
    checks if the number is divisible by 5 and print (Buzz)
    checks if the number is divisible by both 3 and 5, print (fizzBuzz)
    if not divisible by any, print the number.
'''

# def program():
#     data = [1, 10, 12, 17, 15, 7, 20, 30]


#     for i in data:
#         if i % 2 == 0:
#             print(f'{i} - Even')
#         else:
#             print(f'{i} - Odd')


#     for i in data:
#         if i % 3 == 0 and i % 5 == 0:
#             print(f'FizzBuzz {i}')

#         elif i % 3 == 0:
#             print(f'Fizz  {i}')
        
#         elif i % 5 == 0:
#             print(f'Fuzz {i}')
        
#         elif i % 5 != 0 or i % 3 != 0:
#             print(f'{i} - not divisible for both')

# program()






'''
create a list of at least 5 states and capital
write a program that collects user option 1 - 4
1. Displays all states and capital
2. Add new state and capital to the list
3. Edit a particular state and its capital
4. Delete a particular state and its capital
'''

def program():
    State_Capital = {
        'Oyo' : 'Ibadan',
        'Lagos' :'Ikeja',
        'Plateu' : 'Jos',
        'Kogi' : 'Lokoja',
        'Delta' : 'Asaba'
    }
    print('''
    WHAT DO YOU WANT TO PERFORM?
          
        1. Display all states and capital
        2. Add new state and capital to the list
        3. Edit a particular state and its capital
        4. Delete a particular state and its capital
        ''')
    option = input('Enter your option: ')

    if option == '1':
        print(State_Capital)
        program()

    elif option == '2':
        AddState = input('Enter the State in words: ')
        AddCapital = input('Enter the Capital in words: ')
        State_Capital[f'{AddState}'] = f'{AddCapital}'
        print(State_Capital)

    elif option == '3': 
        select = input('type the word "list" to display all states their capital: ')

        if select == 'list':
            print(State_Capital)

            Edit = input('Enter in words the particular state to edit: ')

            for i in State_Capital:
                if Edit == i:
                    State_Capital[i] = f'{Edit}'
                else:
                    print('Please correctly select from one of the states')

                    
        

        else :
            print('you have entered an incorrect word')

program()    



    
