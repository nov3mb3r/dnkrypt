key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, n):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()


def decrypt(ciphertext, n):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

if __name__ == '__main__':
    import sys

