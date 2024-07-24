
'''
concept of class is an object. 
objects are things that have attributes.
objects in python are called class.
any data in python is an object

everything under a class  is called an instance
init is a default function inside a class. onlt inint must be used to initiate a class
__str__ is used to call an attribute in a class

cli.github.com...to download the app
git-scm.com/download....to download...click on standalone installer 64-bit
vscode..entenstion...Gitlens-Git supercharge to install
'''

# class Dog:
#     name = 'Jack'
#     color = 'Brown'
#     height = '30cm'
#     weight = '20lbs'
#     breed = 'pitbull'

class Dog():
    
    def __init__(self, name, color, height, weight, breed, age):
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight
        self.breed = breed 
        self.age = age
    
    def __str__(self):
        return self.name
    
    def checkSpeed(self):
        if self.breed.caseFold() == 'retrieval':
            return f'{self.name} is a {self.breed}, can run at least 30kmph' 
        
        elif self.breed.caseFold() == 'chihuahua':
            return f'{self.name} is a {self.breed}, can run max 15kmph' 
        
        elif self.breed.caseFold() == 'yorkshire':
            return f'{self.name} is a {self.breed}, can run max 15kmph' 
        
        elif self.breed.caseFold() == 'malinios':
            return f'{self.name} is a {self.breed}, can run at least 35kmph' 
        
        elif self.breed.caseFold() == 'german shepard':
            return f'{self.name} is a {self.breed}, can run at least 35kmph' 
        
        elif self.breed.caseFold() == 'pitbull':
            return f'{self.name} is a {self.breed}, can run at least 25kmph' 
        
        else:
            return f'{self.name} speed cannot be defined'
    
    def aggresivness(self):
         if self.breed.caseFold() == 'retrieval':
            return f'{self.name} is very kind'
          
         elif self.breed.caseFold() == 'chihuahua':
            return f'{self.name} is born to be wicked'
          
         elif self.breed.caseFold() == 'yorkshire':
            return f'{self.name} is friendly'
          
         elif self.breed.caseFold() == 'malinios':
            return f'{self.name} is very aggresive'
          
         elif self.breed.caseFold() == 'german shepard':
            return f'{self.name} is very aggresive'
          
         elif self.breed.caseFold() == 'pitbull':
            return f'{self.name} is max aggresive' 
         
         else:
            return f'{self.name} aggresiveness cannot be chceked'
    

        

dog1 = Dog(
        name = 'Lassy',
        color = 'brown yellow',
        height = 1.3,
        weight = 3,
        breed = 'Basengi',
        age = 12
    )
dog2 = Dog(
        name = 'Scrophy',
        color = 'light brown',
        height = 1,
        weight = 3,
        breed = 'Basengi',
        age = 12
    )
dog3 = Dog(
        name = 'Persie',
        color = 'white',
        height = 2,
        weight = 4,
        breed = 'retrieval',
        age = 7
    )
dog4 = Dog(
        name = 'Jacky',
        color = 'black brown',
        height = 2.8,
        weight = 5,
        breed = 'German shepard',
        age = 9
    )
# print(dog1)





    
