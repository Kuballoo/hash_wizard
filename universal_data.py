from os import name, system

MAIN_BANNER = '''###########################
#       HASH WIZARD       #
###########################\n'''


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