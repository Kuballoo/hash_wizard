import hashlib
from colorama import Fore, Style
from universal_data import *
from tqdm import tqdm

'''
    Hasher function
    
    src - source of inserting strings to hash
    sha_mode - if someone selected sha2 or sha3, selection of specific sha
    alg - select concrete alghoritm
'''
def hasher(src, sha_mode, alg):
    print_heading('----- Hasher -----')

    # Selecting concrete hash function from dictionary
    hash_func = hash_functions.get((alg, sha_mode), None)

    # Here user inserts required data depending on his choice
    if src == 1:
        pdw = input_data(str, 'Enter string to hash: ' )
        # Creating hash_obj - storing selected algorithm
        hash_obj = hash_func(pdw.encode())
        hashed_pass = hash_obj.hexdigest()
        print(f'Your hashed string: {Fore.CYAN + hashed_pass + Style.RESET_ALL}')
    else:
        filename = input_data(str, 'Enter your txt file name: ')
        # Stripping .txt from file
        if filename.endswith('.txt'):
            filename = filename[:-4]
        
        # Opening input and output file and saving hashes to hashed_filename.txt
        try:
            with open((filename + '.txt'), 'r') as file:
                num_lines = sum(1 for line in file)

            with open((filename + '.txt'), 'r') as file:
               with open(f'hashed_{filename}_{hash_functions_str.get((alg, sha_mode), None)}.txt', 'w') as output:
                    with tqdm(total=num_lines, desc="Generating hashes") as pbar:
                        for line in file:
                            line = line.rstrip('\n')
                            hash_obj = hash_func(line.encode())
                            hashed_pass = hash_obj.hexdigest()
                            output.write(hashed_pass + '\n')
                            pbar.update(1)
            print(Fore.GREEN + f'Hashes saved to file hashed_{filename}_{hash_functions_str.get((alg, sha_mode), None)}.txt' + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f'ERROR: {e}' + Style.RESET_ALL)
    
    input(Fore.RED + 'Press enter to continue...' + Style.RESET_ALL)
    