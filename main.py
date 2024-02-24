from menu import hash_menu, clear, MAIN_BANNER
from colorama import Fore, Style
from universal_data import *

import hasher

'''
    Main functions calling another functions
'''
def main():
    while True:
        print_heading('----- Menu -----')
        print('1. Hash cracker')
        print('2. Hasher')
        print('3. Password dictionary generator')
        print(Fore.RED + '0. Exit' + Style.RESET_ALL)
    
        choice = input_data(int, '\nEnter your choice: ')
        
        match choice:
            case 1:
                hash_menu(1)
            case 2:
                op = hash_menu(0)
                hasher.hasher(op//100, (op//10)%10, op%10)
            case 3:
                pass
            case _:
                break



main()
clear()