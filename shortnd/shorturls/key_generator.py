ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
BASE = len(ALPHABET)

def gen_key(url_id=None):
    digits = []
    number = int(url_id)

    while number >= BASE:
        digits.insert(0, ALPHABET[number % BASE - 1])
        number = number // BASE
    
    if number != 0:
        digits.insert(0, ALPHABET[number - 1])
    
    return ''.join(digits)
