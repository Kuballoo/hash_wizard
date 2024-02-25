from colorama import Fore, Style
from universal_data import *
from tqdm import tqdm
import itertools
import os

'''
    Function generating dictionary with passwords and saving them to file
'''
def dictionary_generator():
    print_heading('----- Dictionary generator -----')
    alphabet = set(input_data(str, 'Enter your alphabet: '))
    min_length = input_data(int, 'Enter minimum length: ')
    max_length = input_data(int, 'Enter maximum length: ')
    file_name = input_data(str, 'Enter txt file path: ')
    multiple_files = input_data(bool, 'Do you want save every lenght in another files? [y/n] ')
    # Removing and sorting set and shoothing them to list
    alphabet.remove(' ')
    alphabet = sorted(list(alphabet))

    if min_length > max_length:
        robo = min_length
        min_length = max_length
        max_length = robo
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    total_combinations = sum(len(alphabet) ** length for length in range(min_length, max_length + 1))
     # If user chooses to save in separate files
    if multiple_files=='y':
        # Creating directory if it doesn't exist
        directory = os.path.join(os.getcwd(), file_name[:-4])  # Constructing directory path
        os.makedirs(directory, exist_ok=True)
        # Generating and saving passwords for each length in separate files
        for length in range(min_length, max_length + 1):
            length_file_name = f'{file_name[:-4]}_length_{length}.txt'  # Constructing file name
            file_path = os.path.join(directory, length_file_name)  # Constructing full file path
            with open(file_path, 'w') as file:
                pbar = tqdm(total=len(alphabet) ** length, desc=f"Generating passwords of length {length}")
                combinations = itertools.product(alphabet, repeat=length)
                for combination in combinations:
                    password = ''.join(combination)
                    file.write(password + '\n')
                    pbar.update(1)
                pbar.close()
        print(Fore.GREEN + f'Passwords saved to {directory}')  # Informing user about successful saving
    else:
        # Saving all passwords in a single file
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
