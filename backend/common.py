import hashlib
import uuid

def concat_and_hash(string1: str, string2: str) -> uuid:
    '''
    Concatenate the strings and hash. 
    Convert hashed string to a UUID and return
    '''
    concatenated = string1 + string2
    hash = hashlib.sha256(concatenated.encode())
    hash_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, hash.hexdigest())
    print(hash_uuid)
    return hash_uuid