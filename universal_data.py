from os import name, system
from colorama import Fore, Style, Back

MAIN_BANNER = (Fore.GREEN + '''###########################
#       HASH WIZARD       #
###########################\n''' + Style.RESET_ALL)


''' 
    Define our clear function
'''
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


'''
    Universal function to enter data. Data is validate and whole exceptions will be catch
    type - on which type variable should be projected
    string_to_show - text to show in input
'''
def input_data(type, string_to_show):
    try:
        data = type(input(Fore.CYAN + string_to_show + Style.RESET_ALL))
    except Exception as e:
        print(Fore.RED + f'ERROR: {e}')
        input('Press enter to continue...' + Style.RESET_ALL)
        return 0

    return data

'''
    Function clearing, printing main banner and prinitng lower_heading with str (lower_heading) inside
'''
def print_heading(lower_heading):
    clear()
    print(MAIN_BANNER)
    print(Fore.BLUE + lower_heading + Style.RESET_ALL)
    