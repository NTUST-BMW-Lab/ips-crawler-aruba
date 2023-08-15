import hashlib

def create_hash(data):
    # Convert the data to bytes if it's not already in bytes
    if not isinstance(data, bytes):
        data = str(data).encode()

    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256()

    # Update the hash object with the data
    hash_object.update(data)

    # Get the hexadecimal representation of the hash
    hash_value = hash_object.hexdigest()

    return hash_value
