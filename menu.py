# This file saves functions with menu lower layer and some const value

'''
    Hierary of menu:
    main - main.py | main menu
    hash_menu - printing menu for hasher and hasher cracker
    sha_menu* - printing available SHA algorithms for SHA2 and SHA3 
        hasher_menu - printing options how many strings user have to hash
        or
        cracker_menu - prinitng options to insert hash to crack

    * - if user selected SHA2 or SHA3
'''

from os import name, system
from universal_data import *



'''
    Printing hasher menu
'''
def hasher_menu():
    print_heading('----- Hasher options -----')
    print('1. Hash one string')
    print('2. Hash dictionary int txt file to txt file')
    print(Fore.RED + '0. Back' + Style.RESET_ALL)

    choice = input_data(int, 'Enter your choice: ')

    match choice:
        case 1:
            return 100
        case 2:
            return 200
        case 0:
            return 0


'''
    Universal function for sha-2 and sha-3 menu showing and returning selected option
'''
def sha_menu(sha_num):
    print_heading(f'----- SHA-{sha_num} selection -----')
    print('1. SHA-224')
    print('2. SHA-256')
    print('3. SHA-384')
    print('4. SHA-512')
    print(Fore.RED + '0. Back' + Style.RESET_ALL)

    choice = input_data(int, '\nEnter your choice: ')
    match choice:
        case 1:
            return 10+sha_num
        case 2:
            return 20+sha_num
        case 3:
            return 30+sha_num
        case 4:
            return 40+sha_num
        case _:
            return 0


'''
    Universal function for printing hash menu and returning selected option

    This is generating int likes:
    xyz
    x - single/file
    y - if it is sha here saves choosen mode
    z - hasher alg

    example returns:
        101 - SHA-1 single string
        132 - SHA-384 single string
        243 - SHA3-512 from file
        204 - MD5 from file
'''
def hash_menu(unknown=False):
    while True:
        print_heading('----- Hash selection -----')
        print('1. SHA-1')
        print('2. SHA-2')
        print('3. SHA-3')
        print('4. MD5')
        print('5. Hash unknown') if unknown else None
        print(Fore.RED + '0. Exit' + Style.RESET_ALL)

        choice = input_data(int, '\nEnter your choice: ')
        option = 0
        match choice:
                case 1:
                    option = 1
                case 2:
                    option = sha_menu(2)    
                case 3:
                    option = sha_menu(3)
                case 4:
                    option = 4
                case 5:
                    option = 5
                    if not unknown:
                        return 0
                case _: 
                    return 0
        if not unknown and option != 0:
            op = hasher_menu()
            if op != 0:
                option += op
                return option
        elif option != 0:
            # When cracker is selected
            pass
    

