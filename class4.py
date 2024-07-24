'''
A1 = 75 - 100
B2 = 70 - 74
B3 = 65 -69
C4 = 60 - 64
C5 = 55 - 59
C6 = 50 - 54
D7 = 45 - 49
E8 = 40 - 44
F9 = 0 - 39

Write a program that takes user input between 0 - 100 and return the expexted grade.

E.g
your result for score of 57 is C5

Note, use a loop control statement in your program
'''


boundaries = [75, 70, 65, 60, 55, 50, 45, 40, 0]
grades = ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9']

score = input('Enter your score: ' )

# if score.isdigit():
#     print('This is a number')
#     score = int(score)

#     for i, x in zip(boundaries, grades):
#         if score >= i:
#             print(f'your grade is {x}')
#             break
#         else:
#             print('invalid score')


try:
    score = int(score)
    
    if 0 < score <= 100:
        print('student score is valid...')
        for i in boundaries:
            pos = boundaries.index(i)
            if score >= i:
                print(f'Your Grade is {grades[pos]}')

                break
            elif score < 40:
                print(f'Your Grade is {grades[-1]}')
                break
                
        pass
    
    else:
        print('Student score is invalid....')

        pass
        
   
except:
    print(''' 
    you have input an incorrect value....
    check student score again
    ''')
    pass




