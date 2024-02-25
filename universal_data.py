from os import name, system
from colorama import Fore, Style, Back
import hashlib

MAIN_BANNER = (Fore.GREEN + f'''###########################
#       {Fore.MAGENTA}HASH WIZARD{Fore.GREEN}       #
###########################\n''' + Style.RESET_ALL)

# Dictionary saving hash functions
hash_functions = {
    (1, 0): hashlib.sha1,
    (2, 1): hashlib.sha224,
    (2, 2): hashlib.sha256,
    (2, 3): hashlib.sha384,
    (2, 4): hashlib.sha512,
    (3, 1): hashlib.sha3_224,
    (3, 2): hashlib.sha3_256,
    (3, 3): hashlib.sha3_384,
    (3, 4): hashlib.sha3_512,
    (4, 0): hashlib.md5
}
hash_functions_str = {
    (1, 0): 'sha1',
    (2, 1): 'sha224',
    (2, 2): 'sha256',
    (2, 3): 'sha384',
    (2, 4): 'sha512',
    (3, 1): 'sha3_224',
    (3, 2): 'sha3_256',
    (3, 3): 'sha3_384',
    (3, 4): 'sha3_512',
    (4, 0): 'md5'
}
hashes_length = {
    (1, 0): 40,
    (2, 1): 56,
    (2, 2): 64,
    (2, 3): 96,
    (2, 4): 128,
    (3, 1): 56,
    (3, 2): 64,
    (3, 3): 96,
    (3, 4): 128,
    (4, 0): 32
}


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
    