import hashlib
from colorama import Fore, Style
from universal_data import *

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

'''
    Hasher function
    
    src - source of inserting strings to hash
    sha_mode - if someone selected sha2 or sha3, selection of specific sha
    alg - select concrete alghoritm
'''
def hasher(src, sha_mode, alg):
    clear()
    print(Fore.GREEN + MAIN_BANNER + Style.RESET_ALL)
    print(Fore.BLUE + f'----- Hasher -----' + Style.RESET_ALL)

    # Selecting concret hash function from dictionary
    hash_func = hash_functions.get((alg, sha_mode), None)

    # Here user inesrt required data depending on his choice
    if src == 1:
        pdw = str(input(Fore.CYAN + 'Enter string to hash: ' + Style.RESET_ALL))
        # Creating hash_obj - storing selected alghoritm
        hash_obj = hash_func(pdw.encode())
        hashed_pass = hash_obj.hexdigest()
        print(f'Your hashed string: {hashed_pass}')
    else:
        filename = str(input(Fore.CYAN + 'Enter your txt file name: ' + Style.RESET_ALL))
        # Striping .txt from file
        if filename.endswith('.txt'):
            filename = filename[:-4]
        
        # Opening input and output file and saving hashes to hashed_filename.txt
        try:
            with open((filename + '.txt'), 'r') as file:
               with open('hashed_' + filename + '.txt', 'w') as output:
                    for line in file:
                        line = line.rstrip('\n')
                        hash_obj = hash_func(line.encode())
                        hashed_pass = hash_obj.hexdigest()
                        output.write(hashed_pass + '\n')
            print(Fore.GREEN + f'Hashes saved to file hashed_{filename}.txt' + Style.RESET_ALL)
        except Exception as e:
            print(f'ERROR: {e}')
    
    input(Fore.RED + 'Press enter to continue...' + Style.RESET_ALL)

