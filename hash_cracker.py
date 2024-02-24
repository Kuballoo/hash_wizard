import hashlib
from tqdm import tqdm

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


'''
    This function find password (if exist in file with public passwords) in public form from entered hash
    If user didnt know which hash alghoritm was used, function iterate on every alg.
'''
def hash_cracker(sha_mode, alg):
    print_heading('----- Hash cracker -----')
    hash_to_crack = input_data(str, 'Enter your hash: ')
    pwds_file = input_data(str, 'Enter file name with passwords to scan: ')
    if not pwds_file.endswith('.txt'):
        pwds_file += '.txt'
    # Selecting concrete hash function from dictionary
    hash_func = hash_functions.get((alg, sha_mode), None)

    # Check if user know which alghoritm we should use
    if hash_func == None:
        try:
            # Count number of lines
            with open(pwds_file, 'r') as file:
                num_lines = sum(1 for line in file)
            
            # Iteration on hash func dictionary and check whole options
            for hash_f_alg, hash_f_sha_mode in hash_functions:
                hash_func = hash_functions.get((hash_f_alg, hash_f_sha_mode), None)
                algorithm_desc = hash_functions_str.get((hash_f_alg, hash_f_sha_mode), 'Unknown Algorithm')
                # Opening txt with passwords for scanning
                with open(pwds_file, 'r') as file:
                    with tqdm(total=num_lines, desc=f'Scanning dictionary for {Fore.CYAN + algorithm_desc + Style.RESET_ALL}', leave=False) as pbar:
                        for line in file:
                            line = line.rstrip('\n')
                            hash_obj = hash_func(line.encode())
                            hashed_pass = hash_obj.hexdigest()
                            # If we find hash same as user hash we show password and end function
                            if hashed_pass == hash_to_crack:
                                print('\n\nYour password is ' + Fore.GREEN + line + Style.RESET_ALL)
                                print(f'Algorithm type {Fore.CYAN + algorithm_desc + Style.RESET_ALL}')
                                input(Fore.RED + 'Press enter to continue...' + Style.RESET_ALL)
                                return True
                            pbar.update(1)
                            pbar.refresh()
        except Exception as e:
            print(Fore.RED + f'ERROR: {e}' + Style.RESET_ALL)
    else:
        try:
            # Same as upper code, without iter on hash dict
            with open(pwds_file, 'r') as file:
                num_lines = sum(1 for line in file)
            with open(pwds_file, 'r') as file:
                 with tqdm(total=num_lines, desc="Scanning dictionary") as pbar:
                        for line in file:
                            line = line.rstrip('\n')
                            hash_obj = hash_func(line.encode())
                            hashed_pass = hash_obj.hexdigest()
                            if hashed_pass == hash_to_crack:
                                print('\nYour password is ' + Fore.GREEN + line + Style.RESET_ALL)
                                print(f'Alghoritm type {Fore.CYAN + hash_functions_str.get((alg, sha_mode), None) + Style.RESET_ALL}')
                                input(Fore.RED + 'Press enter to continue...' + Style.RESET_ALL)
                                return True
                            pbar.update(1)
                            pbar.refresh()
        except Exception as e:
            print(Fore.RED + f'ERROR: {e}' + Style.RESET_ALL)

    # If the entire function is executed, it means that there is no entry with such a hash in the dictionary
    print(Fore.RED + 'Password did not exist in this file' + Style.RESET_ALL)
    input(Fore.RED + 'Press enter to continue...' + Style.RESET_ALL)
    