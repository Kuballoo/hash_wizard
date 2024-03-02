from colorama import Fore, Style
from universal_data import *
from tqdm import tqdm
import itertools
import os

'''
    Inner loop of generating passwords of one size
'''
def inner_loop(pbar, file, alphabet, length):
    combinations = itertools.product(alphabet, repeat=length)
    for combination in combinations:
        password = ''.join(combination)
        file.write(password + '\n')
        pbar.update(1)

'''
    Function generating dictionary with passwords and saving them to file
'''
def dictionary_generator():
    print_heading('----- Dictionary generator -----')
    alphabet = set(input_data(str, 'Enter your alphabet: '))
    min_length = input_data(int, 'Enter minimum length: ')
    max_length = input_data(int, 'Enter maximum length: ')
    file_name = input_data(str, 'Enter txt file path: ')
    savign_option = input_data(str, 'Saving options: every lenght in another files[1], intelligent cutting[2], one file[3]: ')
    # Removing and sorting set and shoothing them to list
    if ' ' in alphabet:
        alphabet.remove(' ')
    alphabet = sorted(list(alphabet))

    if min_length > max_length:
        robo = min_length
        min_length = max_length
        max_length = robo
    if not file_name.endswith('.txt'):
        file_name += '.txt' 
    total_combinations = sum(len(alphabet) ** length for length in range(min_length, max_length + 1))

    directory = os.path.join(os.getcwd(), file_name[:-4])  # Constructing directory path
    os.makedirs(directory, exist_ok=True)

     # Saving option if
    if savign_option=='1':
        # Generating and saving passwords for each length in separate files
        for length in range(min_length, max_length + 1):
            length_file_name = f'{file_name[:-4]}_length_{length}.txt'  # Constructing file name
            file_path = os.path.join(directory, length_file_name)  # Constructing full file path
            with open(file_path, 'w') as file:
                pbar = tqdm(total=len(alphabet) ** length, desc=f"Generating passwords of length {length}")
                inner_loop(pbar, file, alphabet, length)
                pbar.close()
    elif savign_option=='2':
        max_chars_per_file = input_data(int, 'Enter size of one file (in MB): ')
        max_chars_per_file = max_chars_per_file*1024*1024

        total_combinations = sum(len(alphabet) ** length for length in range(min_length, max_length + 1))

        current_chars = 0
        current_file_index = 1
        file_path = os.path.join(directory, f"{file_name[:-4]}_{current_file_index}.txt")

        pbar = tqdm(total=total_combinations, desc=f"Generating passwords")
        for length in range(min_length, max_length + 1):
            with open(file_path, 'w') as file:
                combinations = itertools.product(alphabet, repeat=length)
                for combination in combinations:
                    password = ''.join(combination)
                    file.write(password + '\n')
                    current_chars += len(password) + 1  # Add 1 for newline character
                    pbar.update(1)
                    if current_chars >= max_chars_per_file:
                        current_chars = 0
                        current_file_index += 1
                        file_path = os.path.join(directory, f"{file_name[:-4]}_{current_file_index}.txt")
                        file.close()
                        file = open(file_path, 'w')
        pbar.close()
    else:
        file_path = os.path.join(directory, file_name)  # Constructing full file path
        # Saving all passwords in a single file
        with open(file_path, 'w') as file:
            pbar = tqdm(total=total_combinations, desc="Generating passwords")
            for length in range(min_length, max_length + 1):
                inner_loop(pbar, file, alphabet, length)
            pbar.close()
    file.close()
    print(Fore.GREEN + f'Passwords saved to {directory}, passwords count: {total_combinations}')  # Informing user about successful saving
        
    input(Fore.RED + 'Press enter to continue...' + Style.RESET_ALL)
