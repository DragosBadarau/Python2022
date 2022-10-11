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


print("Ex: 1")
print(multiple_gcd(16, 20, 36, 8))


# 2
def number_of_vowels(string):
    "returns the number of vowels for a given string"
    nr_of_vowels = 0
    for letter in string:
        if letter in 'aeiouAEIOU':
            nr_of_vowels += 1
    return nr_of_vowels


print("Ex: 2")
print(number_of_vowels('ronaldinho_Dumitrescu'))


# 3
def occurences(small_string, big_string):
    "returns the number of occurrences of the first string in the second "
    return big_string.count(small_string)


print("Ex: 3")
print(occurences('salut', 'salutsalutsalut'))


# 4

def UpperCamelCase_to_lowercase_with_underscores(string):
    "Converts a given UpperCamelCase string into lowercase_with_underscores"
    new_str = ""
    for i in range(len(string)):
        if 'A' <= string[i] <= 'Z' and i > 1:
            new_str = f'{new_str}_{string[i].lower()}'
        else:
            new_str = f'{new_str}{string[i]}'
    return new_str


print("Ex: 4")
print(UpperCamelCase_to_lowercase_with_underscores('LetUsCodeEverybodyDancingAllAround'))


# 5

def spiral_matrix(matrix):
    "Given a list of list of characters it prints the string obtained by going through the overall matrix in spiral order"
    i = j = 0
    new_str = []
    aux_l = l = len(matrix)
    ok = True
    while (l):
        while (j < l - 1):
            print(matrix[i][j])
            new_str.append(matrix[i][j])
            j += 1
        while (i < l - 1):
            new_str.append(matrix[i][j])
            i += 1
        while (j > aux_l - l):
            print(matrix[i][j])
            new_str.append(matrix[i][j])
            j -= 1
        while (i > aux_l - l):
            new_str.append(matrix[i][j])
            i -= 1
        l -= 1
        i += 1
        j += 1
    print(new_str)


print("Ex: 5")
print(spiral_matrix([['f', 'i', 'r', 's'], ['n', '_', 'l', 't'], ['o', 'b', 'a', '_'], ['h', 't', 'y', 'p']]))


# 6

def validate_palindrom(nr):
    "Validates if the given number is a palindrome"
    str_nr = str(nr)
    reverse_nr = str_nr[::-1]
    return str_nr == reverse_nr


print("Ex: 6")
print(validate_palindrom(15451))


# 7
def first_number_from_text(string):
    "Returns the first number found in the text givne"
    i = 0
    a = 0
    while i < len(string):
        if '0' <= string[i] <= '9':
            a = a * 10 + int(string[i])
        if a != 0 and not '0' <= string[i] <= '9':
            return a
        i += 1


print("Ex: 7")
print(first_number_from_text('An apple is 123 USD 9012'))


# 8
def number_of_bits(nr):
    "Returns how many bits with value 1 the number given as a parameter has"
    nr_of_bits = 0
    while nr > 0:
        if nr % 2 == 1:
            nr_of_bits += 1
        nr = nr // 2
    return nr_of_bits


print("Ex: 8")
print(number_of_bits(24))


# 9

def common_letter(string):
    "prints the most common letter in the given string "
    dictionary = {}
    string = string.lower()
    for letter in string:
        if letter in dictionary:
            dictionary[letter] += 1
        elif letter != ' ':
            dictionary[letter] = 1
    print(dictionary)
    max_nr_of_occurences = max(dictionary.values())
    letters_with_most_occurences = {k for k, v in dictionary.items() if v == max_nr_of_occurences}
    print(letters_with_most_occurences)


print("Ex: 9")
common_letter('an apple is not a tomato')


# 10

def word_count(string):
    "Returns the number of words in the given string"
    number_of_words = 0
    if string:
        number_of_words += 1
    for i in range(1, len(string) - 1):
        if string[i] in " ,;?!.," and string[i + 1] not in " ,;?!.,":
            number_of_words += 1
    return number_of_words


print("Ex: 10")
print(word_count('Hello, is this thee number of words required????? '))
