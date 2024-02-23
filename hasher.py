import hashlib


def hasher(src, sha_mode, alg):
    hash_obj = None
    if alg == 1: 
        hash_obj = hashlib.sha1()
    elif alg == 2: 
        if sha_mode == 1:
            hash_obj = hashlib.sha224()
        elif sha_mode == 2:
            hash_obj = hashlib.sha256()
        elif sha_mode == 3:
            hash_obj = hashlib.sha384()
        elif sha_mode == 4:
            hash_obj = hashlib.sha512()    
    elif alg == 3: 
        if sha_mode == 1:
            hash_obj = hashlib.sha3_224()
        elif sha_mode == 2:
            hash_obj = hashlib.sha3_256()
        elif sha_mode == 3:
            hash_obj = hashlib.sha3_384()
        elif sha_mode == 4:
            hash_obj = hashlib.sha3_512()
    elif alg == 4:
        hash_obj = hashlib.md5()


    if src == 1:
        pdw = str(input('Enter string to hash: '))
    

    else:
        pass