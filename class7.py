# Mr Sam method for the assignment on state and capital

# CRUD - OPERATION
# C - Create
# R - Read
# U - Update
# D - Delete/ Destroy

State_Capital = [
    {
        'state' : 'Oyo',
        'capital' : 'Ibadan' 
    },
     {
        'state' : 'Lagos',
        'capital' : 'Ikeja' 
    },
     {
        'state' : 'Ogun',
        'capital' : 'Abeokuta' 
    },
     {
        'state' : 'Edo',
        'capital' : 'Benn' 
    },
     {
        'state' : 'Akwa-Ibom',
        'capital' : 'Uyo' 
    },
]

def main(main_list):
    def display(st_list):

        for each_item in st_list:
            pos = st_list.index(each_item)
            print(f'{pos+1}. {each_item['state']} - {each_item['capital']}')
    
    def add():
        new_state = input('Enter the name of the State: ')
        new_Capital = input('Enter the name of the capital: ')
        st_cp = {
            'state' : new_state,
            'capital' : new_Capital
        }
        main_list.append(st_cp)

        display(main_list)
    
    def edit():
        pos = input('Enter the number of the state: ')
        print('')
        st_cp = main_list[int(pos)-1]
        try :
            print(f'{pos}. {st_cp["state"]} - {st_cp["capital"]}')
            ask_state = input('Enter Y to edit state: ')
            new_state = False
            new_capital = False
            if ask_state.casefold() == 'y':
                new_state = input('Enter the name of the new state: ')
                main_list[int(pos)-1]['state'] = new_state
            
            ask_capital = input('Enter Y to edit capital: ')
            if ask_capital.casefold() == 'y':
                new_capital = input('Enter the name of the new capital: ')
                main_list[int(pos)-1]['capital'] = new_capital
            
            if new_state or new_capital:
                print('Edit successful !!!')
            else :
                print('No changes were made')
        except:
            print('Invalid number')
    
    def delete():
        pos = input('Enter the number of the state to delete: ')
        print('')
        try:
            main_list.pop(int(pos)-1)
            print('Delete sucessful')
        except:
            print('Invalid number')
        
    
    announcement = '''
                    CHOOSE OPTION 1 - 4
                    1. To display all state and capital
                    2. To add new state and capital
                    3. To edit a state and its capital
                    4. To delete a state and capital
                    5. To close the program
                '''
    print(announcement)
    option = input('Enter your option: ')
    if option == '1':
        print('Display all states and capital')
        display(main_list)
        main(main_list)
    
    elif option == '2':
        print('Add new state and capital')
        add()
        main(main_list)
    
    elif option == '3':
        print('Edit a particular state and capital')
        edit()
        main(main_list)
    
    elif option == '4':
        print('Delete a particular state and capital')
        delete()
        main(main_list)
    
    elif option == '5':
        print('Thank you for using our service')
        pass
    
    else :
        print('Invalid option, try again')
        main(main_list)


main(State_Capital)

