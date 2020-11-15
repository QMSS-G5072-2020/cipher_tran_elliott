def cipher(text, shift, encrypt=True):
    """
    Each letter is replaced by a letter some fixed number of positions down the alphabet.

    Parameters
    ---
    text: string value that you wish to encrypt or decrypt
    shift: integer value of how many number positions down the alphabet you would like to shift the string
    encrypt: boolean value that is 1 if you wish to encrypt or 0 if you wish to decrypt

    Returns
    ---
    string value that has been encrypted or decrypted


    Examples
    ---
    from cipher_eat2153 import cipher_eat2153
    >>> cipher(text = 'yoda', shift = 1, encrypt = True)
    ['zpeb']
    >>> 
    
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text