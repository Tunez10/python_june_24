import math



#FUNCTION IN PYTHON

# def greet():
    # print('Hello World')

# greet()

# def greetStudent(name):
    # print(f'Hello {name} welcome to class')

# # greetStudent('Bolu')
# greetStudent('Tunez')
# greetStudent('Aishat')
# greetStudent('Adeniyi')

# def addNum(num1, num2):
#     result = num1 + num2
#     # print(result)

# addNum(43,64)

# def subNum(num1, num2):
#     result = num1 - num2
#     # print(result)

# subNum(67,20)

# def divNum(num1, num2):
#     result = num1 / num2
#     print(result)

# divNum(1500,10)











'''write a program that performs an arithmetic function on two numbers based on user options'''

# operations = ['add', 'subtract', 'multiply', 'divide']

# user = input('select an operation as seen (add, subtract, multiply, divide): ')

# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')

# for i in operations:
#     if user == operations[0]:
#         num1 = int(num1)
#         num2 = int(num2)
#         def addSum(num1, num2):
#             result = num1 + num2
#             print(result)
#         addSum(num1, num2)
#         break
#     elif user == operations[1]:
#         num1 = int(num1)
#         num2 = int(num2)
#         def subNum(num1, num2):
#             result = num1 - num2
#             print(result)
#         subNum(num1, num2) 
#         break
#     elif user == operations[2]:
#         num1 = int(num1)
#         num2 = int(num2)
#         def mulNum(num1, num2):
#             result = num1 * num2
#             print(result)
#         mulNum(num1, num2)
#         break
#     elif user == operations[3]:
#         num1 = int(num1)
#         num2 = int(num2)
#         def divNum(num1, num2):
#             result = num1 / num2
#             print(result)
#         divNum(num1, num2)
#         break

#     else:
#         print('Cannot perform operation')
#         break



'''write a temperature converter program, fehrenheit to celcius and vice versa'''

# option = input('Enter "1" to convert \u00B0C to \u00B0F OR "2" to convert \u00B0F to \u00B0C: ')
# temp = input('Enter temperature in digits: ')

# if option.isdigit():
#     option = int(option)

#     if option == 1:
#         if temp.isdigit():
#             temp = int(temp)
#             print('this number is valid')
        
#             def c_to_f(temp):
#                 result = (temp * 9/5) + 32
#                 print(f'{round(result, 1)}\u00B0F' )
#             c_to_f(temp)
#         else:
#             print('please input temperature number in digits')
    
#     elif option == 2:
#         if temp.isdigit():
#             temp = int(temp)
#             print('This number is valid')

#             def f_to_c(temp):
#                 result = (temp - 32) * 5/9
#                 print(f'{round(result, 1)}\u00B0C')
#             f_to_c(temp)
#         else:
#             print('please input temperature number in digits') 
#     else:
#         print('Please input either number "1" or "2" to convert temperature')


'''write a program that converts dollar to naira and vice versa, using 1640 naira to a dollar as exchange rate'''

# Mr SAM method on operations om two 

def myProgrm():
    print('welcome to our software !!!!')
    print('''
        CHOOSE THE NUMBER OF YOUR OPTION BELOW:
          1. perform an arithmetic operation
          2. perform a Temperature conversion
          3. perform a curency conversion
          4. close program
        ''')
    option = input('Enter your option: ')

    if option =='1':
        print('perform an arithmetic operation.\n\n')
        print('''
            ENTER THE SYMBOL FOR YOUR OPERATION BELOW:
              1. ADDITION            +
              2. SUBTRACTION         -
              3. MULTIPLICATION      *
              4. DIVISION            /
              5. SQUARE ROOT            
            ''')
        op_list = ['+', '-', '*', '/']
        operation = input('Enter operation symbol: ')
        num1 = input('Enter first nmber: ')


        if operation.strip() in op_list:
             num2 = input('Enter second number: ')
             print('\n')
             try:
                 print(eval(num1+operation+num2))
             except:
                 print('you have entered an invalid value\n\n')
                 pass
             myProgrm()
        elif operation == '5':
            print('performing square root')

            try:
                print(round(math.sqrt((int(num1)))))
                print('\n')
            except:
                print('you have entered an invalid value\n\n')
        myProgrm()
    
    elif option == '2':
        print('perform a temperature conversion')
        myProgrm()
    
    elif option == '3':
        print('perform a currency conversion')
        myProgrm()
    
    else:
        print('Thank you for using our program.')
        pass


myProgrm()




        








