import string


def shift_alphabet(steps):
    """
    Returns a shifted alphabet (in lower case), or empty list if 'steps' is below 0
    :param steps: The number of steps to shift alphabet
    :return: a list of the shifted alphabet
    """

    if steps < 0:
        return ''

    alphabet = list(string.ascii_lowercase)
    shifted_alphabet = alphabet.copy()
    for i, c in enumerate(alphabet):
        if i + steps >= 26:                                 # if we step past the 'z' in the alphabet
            shifted_alphabet[i] = alphabet[i + steps - 26]  # we subtract by 26 to 'start over again'
        else:
            shifted_alphabet[i] = alphabet[i + steps]
    return shifted_alphabet


def encrypt(text, steps):
    """
    :param text: The text to be encrypted
    :param steps: The number of shifts in alphabet.
    :return: The encrypted text.
    """

    if steps < 0:
        return ''

    alphabet = list(string.ascii_lowercase)
    shifted_alphabet = shift_alphabet(steps)
    text = list(text.lower())

    for i, c in enumerate(text):
        for j, k in enumerate(alphabet):
            if c == k:
                text[i] = shifted_alphabet[j]
    return ''.join(text)


def decrypt(text, steps):
    """
    :param text: The text that will be decrypted
    :param steps: The number of shifts in alphabet for decryption.
    :return: The decrypted text.
    """

    if steps < 0:
        return ''

    alphabet = list(string.ascii_lowercase)
    shifted_alphabet = shift_alphabet(steps)
    text = list(text.lower())

    for i, c in enumerate(text):
        for j, k in enumerate(shifted_alphabet):
            if c == k:
                text[i] = alphabet[j]
    return ''.join(text)


def brute_force(text):
    """
    Brute force a Caesar cipher.
    :param text: The text to brute force.
    :return: A list of candidate plaintext.
    """
    li = []
    alphabet = string.ascii_lowercase
    for index, letter in enumerate(alphabet):
        li.append(list(decrypt(text, index)))
    return li
