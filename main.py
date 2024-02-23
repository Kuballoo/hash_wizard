from menu import hash_menu, clear, MAIN_BANNER
from colorama import Fore, Style




def main():
    while True:
        clear()
        print(Fore.GREEN + MAIN_BANNER + Style.RESET_ALL)
        print(Fore.BLUE + '----- Menu -----' + Style.RESET_ALL)
        print('1. Hash cracker')
        print('2. Hasher')
        print('3. Password dictionary generator')
        print(Fore.RED + '0. Exit' + Style.RESET_ALL)
    
        choice = int(input(Fore.CYAN + '\nEnter your choice: ' + Style.RESET_ALL))
        
        match choice:
            case 1:
                hash_menu(1)
            case 2:
                hash_menu(0)
            case 3:
                pass
            case _:
                break



main()
clear()