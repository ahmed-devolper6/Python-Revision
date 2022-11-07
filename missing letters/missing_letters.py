import string 

def find_missing_letters(given_letters):
    alpha = string.ascii_letters
    start = alpha.index(given_letters[0])
    for letter in alpha[start:]:
        if letter not in given_letters:
            return letter

    return f'no missing letters'

# letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
case1 = print(find_missing_letters('abd'))
case2 = print(find_missing_letters('ABCDEF'))
case3 = print(find_missing_letters('wxyz'))
