# 1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def multiple_gcd(*nr):
    'The greatest common divisor of multiple numbers'
    a = gcd(nr[0], nr[1])
    for i in range(2, len(nr)):
        a = gcd(nr[i], a)
    return a


print(multiple_gcd(16, 20, 36, 8))


# 2
def number_of_vowels(string):
    nr_of_vowels = 0
    for letter in string:
        if letter in 'aeiouAEIOU':
            nr_of_vowels += 1
    return nr_of_vowels


print(number_of_vowels('ronaldinho_Dumitrescu'))


# 3
def occurences(big_string, small_string):
    return big_string.count(small_string)


print(occurences('salutsalutsalut', 'salut'))


# 4

def UpperCamelCase_to_lowercase_with_underscores(string):
    new_str = ""
    for i in range(len(string)):
        if 'A' <= string[i] <= 'Z' and i > 1:
            new_str = f'{new_str}_{string[i].lower()}'
        else:
            new_str = f'{new_str}{string[i]}'
    return new_str


print(UpperCamelCase_to_lowercase_with_underscores('LetUsCodeEverybodyDancingAllAround'))


# 5

def spiral_matrix(matrix):
    i = j = 0
    new_str = []
    for i, char in enumerate(matrix[0]):
        new_str.append(char)

    return new_str


print(spiral_matrix([['firs'],['n_lt'],['oba_'],['htyp']]))

#6

def validate_palindrom(nr):
    str_nr = str(nr)
    reverse_nr = str_nr[::-1]
    return str_nr == reverse_nr

print(validate_palindrom(15431))

# 10

def word_count(string):
    number_of_words = 0
    if string:
        number_of_words += 1
    for i in range(1, len(string) - 1):
        if string[i] in " ,;?!.," and string[i + 1] not in " ,;?!.,":
            number_of_words += 1
    return number_of_words

print(word_count('Hello, is this thee number of words required????? '))
