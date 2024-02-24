from colorama import Fore, Style
from universal_data import *
from tqdm import tqdm
import itertools

'''
    Function generating dictionary with passwords and saving them to file
'''
def dictionary_generator():
    print_heading('----- Dictionary generator -----')
    alphabet = set(input_data(str, 'Enter your alphabet: '))
    min_length = input_data(int, 'Enter minimum length: ')
    max_length = input_data(int, 'Enter maximum length: ')
    file_name = input_data(str, 'Enter txt file path: ')
    if min_length > max_length:
        robo = min_length
        min_length = max_length
        max_length = robo
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    total_combinations = sum(len(alphabet) ** length for length in range(min_length, max_length + 1))

    with open(file_name, 'w') as file:
        pbar = tqdm(total=total_combinations, desc="Generating passwords")
        for length in range(min_length, max_length + 1):
            combinations = itertools.product(alphabet, repeat=length)
            for combination in combinations:
                password = ''.join(combination)
                file.write(password + '\n')
                pbar.update(1)
        pbar.close()
        
    print(Fore.GREEN + f'Passwords saved to {file_name}, count of passwords {total_combinations}')
    input(Fore.RED + 'Press enter to continue...' + Style.RESET_ALL)
