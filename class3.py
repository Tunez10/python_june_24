
# person1 = 'Bolade'
# student_list = ['Adebiyi', 'Adewunmi', 'Aishat', 'Fortune', 'Boluwatife'] #this is list
# student_list.append(person1)
# print(student_list)





# for eachItem in student_list: 
#         # print('hello ' + eachItem + ', welcome to class') # '' + eachitem = concatination
        # print(f'hello {eachItem},  welcome to class') #f-string / format-string
#         print('hello', eachItem, 'welcome to class') 


# num = 3
# print(type(num))

# num = str(num)
# print(type(num))

# num1 = 10
# num2 = 17

# if num1 < 7 and num2 < 20:
#         print('condition met')

# if num1 == 10 or num2 < 15:
#         print('condition met')




# English = 70
# maths = 80

# if English >= 50 and maths >= 50:
#         print('Admission Granted')

# else : print('Does nor meet cut-off')





Result = 'B'

if Result =='A':
        print('The code is successful')

elif Result == 'B':
        print('The code execution is successful with little error')

elif Result == 'C':
        print('The code execution is successful with error')

elif Result == 'D':
        print('The code execution is successful with lots of errors')

else: 
        print('The code failed')


# class Task
# 1. UI requires students to have 50% or above in both English and Math to be considered
#    OAU reqiuires students to have at least 50% or more in either English or Math to be considered

#2.   Baby = 0 - 2
#     children = 3 - 12
#     Teen = 13 - 17
#     Youth = 18 - 29
#     Adult = 30 - 45
#     Older Adult = 46 - 70

#     Request user age, and return the age group based on the input.





# Tobi total score
m_score = 60
E_score = 55

if m_score >= 50 and E_score >= 50:
        print('Granted admission into UI') 
elif m_score >= 50 or E_score >50:
        print('Granted admission into OAU')
else : print('Failed to get amission')



# Aishat total score
m_score = 45
E_score = 52

if m_score >= 50 and E_score >= 50:
        print('Granted admission into UI') 
elif m_score >= 50 or E_score >50:
        print('Granted admission into OAU')
else : print('Failed to get amission')



# Fortune's total score
m_score = 49
E_score = 32

if m_score >= 50 and E_score >= 50:
        print('Granted admission into UI') 
elif m_score >= 50 or E_score >50:
        print('Granted admission into OAU')
else : print('Failed to get amission')






Age = input('Enter your age: ')

if Age.isdigit():
        print('The age is a number')
        Age = int(Age)

        if Age >= 0 and Age <= 2:
                print('baby')
      
        elif Age >= 3 and Age <= 12:
                print('Child')

        elif Age >= 13 and Age <= 17:
                print('Teen')

        elif Age >= 18 and Age <= 29:
                print('Youth')

        elif Age >= 30 and Age <= 45:
                print('Adult')

        elif Age >= 46 and Age <= 70:
                print('Older Adult')

        else: 
                print('Does not meet Age requirement')

else:
        print('Please input only numbers')



















