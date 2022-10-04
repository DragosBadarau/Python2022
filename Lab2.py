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


print(spiral_matrix([['firs'], ['n_lt'], ['oba_'], ['htyp']]))


# 6

def validate_palindrom(nr):
    str_nr = str(nr)
    reverse_nr = str_nr[::-1]
    return str_nr == reverse_nr


print(validate_palindrom(15431))


# 7
def first_number_from_text(string):
    i = 0
    a = 0
    while i < len(string):
        if '0' <= string[i] <= '9':
            a = a * 10 + int(string[i])
        if a != 0 and not '0' <= string[i] <= '9':
            return a
        i += 1


print(first_number_from_text('An apple is 123 USD 9012'))


# 8
def number_of_bits(nr):
    nr_of_bits = 0
    while nr > 0:
        if nr % 2 == 1:
            nr_of_bits += 1
        nr = nr // 2
    return nr_of_bits


print(number_of_bits(24))


# 9

def common_letter(string):
    dictionary = {}
    string = string.lower()
    for letter in string:
        if letter in dictionary:
            dictionary[letter]+=1
        else:
            dictionary[letter]=1
    most_common_letter=max(dictionary,key=dictionary.get)
    print(most_common_letter)


print(common_letter('an apple is not a tomato'))


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
