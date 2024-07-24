





def general():
    welcome = input('Please enter your name: ')
    print(f'\nWelcome {welcome.upper()}!!!')
    
    def Exercise():

        print('''
                PRACTICE EXERCISE FOR PYTHON BASICS\n
            1. Write a program that takes a list of integers as input and returns the sum of all the integers in the list.
            2. Write a program that takes a list of integers as input and returns the average of all the integers in the list.
            3. Write a function that takes a string as input and returns the length of the string.
            4. Write a function that takes a list of integers as input and returns the maximmum value in the list.
            5. Write a program that takes a list of integers as input and returns a new list that contains only the even integers from the original list.
            6. Write a program that takes two lists of integers as input and returns a new list that contains the intersection of the two lists (i.e., the elements that are present in both lists).
            7. Write a program that takes a list of integers as input and returns a new list that contains the squares of all the integers in the original list.
            8. Write a function that takes two integers as input and returns the sum of the two integers.
            9. Write a program that takes a list of integers as input and returns the product of all the integers in the list.
            10. Write a prgram that takes a list of strings as input and returns a new list that contains only the strings that start with the letter 'a'.

            ''')
        
    
        select = input('select any from 1 - 10 above to solve:')
        

        def one():
            user = input('Enter different random numbers, with space inbetween: ')
            numbers = (int(x) for x in user.split())
            Addition = sum(numbers)
            print(f'the sum of all integers is {Addition}')
        
        def two():
            user = input('Enter different random numbers, with space inbetween: ')
            numbers = [int(x) for x in user.split()]
            average = sum(numbers) / len(numbers)
            print(f'the average of the list is {average}')
        
        def three():
            user = input('Enter any random word without space in: ')
            answer = len(user.strip())
            print(f'The length of the list is {answer}')
        
        def four():
            user = input('Enter random numbers with space inbetween: ')
            numbers = (int(x) for x in user.split())
            max_value = max(numbers)
            print(f'The maximum value in the list is {max_value}')
        
        def five():
            user = input('Enter both odd and even numbers randomly with space inbetween: ')
            numbers = (int(x) for x in user.split())
            for i in numbers:
                if i % 2 == 0:
                    print(i)

        def six():
            entry_1 = input('Enter random numbers with space inbetween: ')
            split_1 = (int(x) for x in entry_1.split())
    
            entry_2 = input('Enter random numbers with space inbetween: ')
            split_2 = (int(x) for x in entry_2.split())
            result = set(split_1).intersection(set(split_2))
            print(list(result))
        
        def seven():
            user = input('Enter random numbers with space inbetween: ')
            split_1 = (int(x) for x in user.split())
            for i in split_1:
                print((i**2))
        
        def eight():
            user = input('Enter two random numbers only with space inbetween: ')
            numbers = (int(x) for x in user.split())
            addition = sum(numbers)
            print(addition)
        
        def nine():
            user = input('Enter two random numbers only with space inbetween: ')
            numbers = (int(x) for x in user.split())
            product = sum(numbers)
            print(product)
        
        def ten():
            user = input('Enter different words, with at least one of them starting with the leter a: ')
            words = ((x) for x in user.split())
            for i in words:
                if i[0] == 'a':
                    print(f'{i.upper()} - Starts with the letter a')
                    
               
        

          

            
        

           
            
             

        
        if select == '1':
            print('Solving for sum of all integer inputs\n')
            one()
            Exercise()
        
        elif select == '2':
            print('Solving for average of integer inputs\n')
            two()
            Exercise()
        
        elif select == '3':
             print('Solving for length of the string\n')
             three()
             Exercise()

        elif select == '4':
             print('Solving for maximum value in the list\n')
             four()
             Exercise()

        elif select == '5':
             print('Solving for even numbers in the list\n')
             five()
             Exercise()

        elif select == '6':
             print('Solving for intersection of the two list\n')
             six()
             Exercise()
        
        elif select == '7':
            print('Solving for square of all integers in the list\n')
            seven()
            Exercise()
        
        elif select == '8':
            print('solving for the sum of the two integers\n')
            eight()
            Exercise()

        elif select == '9':
            print('solving for the product of all the integers\n')
            nine()
            Exercise()

        elif select == '10':
            print('solving for words that starts with a\n')
            ten()
            Exercise()



            
    Exercise()
general()