# 1
def fibo(n):
    """
    Returns the first n fibonacci numbers as a list
    """
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    lista = [0, 1]
    for i in range(2, n):
        lista.append(lista[i - 1] + lista[i - 2])
    return lista


print("Ex1 - Fibonacci ")
print(fibo(12))


# 2
def is_prime(x):
    if x <= 1:
        return False
    if 2 == x:
        return True
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
    return True


def prime_numbers(initial_list):
    ' Returns the prime numbers of a list '
    new_list = [nr for nr in initial_list if is_prime(nr)]
    return new_list


print("Ex2 - Only the prime numbers ")
print(prime_numbers([10, 17, 25, 29, 13, 22, 100]))

# 3
print("Ex3 - Union, Commons, Dif1, Dif2")


def list_operations(list1, list2):
    'Returns the union, difference and the common members of two lists'
    global ok, i
    union = list(list1)
    for elem in list2:
        if elem not in union:
            union.append(elem)

    common = []
    for elem in list2:
        if elem in list1:
            common.append(elem)

    unique_list1 = []
    for elem in list1:
        if elem not in list2:
            unique_list1.append(elem)

    unique_list2 = []
    for elem in list2:
        if elem not in list1:
            unique_list2.append(elem)

    return union, common, unique_list1, unique_list2


print(list_operations([0, 1, 2, 3, 4], [2, 4, 6, 7, 8]))


# 4
def compose(musical_notes, moves, start_position):
    'Returns the musical notes obtained by moving through a list with a list of moves'
    song = []
    l=len(musical_notes)
    song.append(musical_notes[start_position])
    for move in moves:
        start_position+=move
        song.append(musical_notes[start_position%l])
    return song
print("Ex4 - Song created with musical notes")
print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
# 5
def replace_elem(matrix):
    'Returns the matrix with zeros under the main diagonal'
    zeros=-1
    for elem in matrix:
        zeros+=1
        for index,each_elem in enumerate(elem):
            if index<zeros:
                elem[index]=0
    return matrix
print("Ex5 - Matrix with zeros under the main diagonal")
print(replace_elem([[1,2,3,4],[5,6,7,8],[10,10,10,10]]))
# 6
def char_with_n_appearances(n, *all_lists):
    'Returns only the elements that appear n times in all the lists'
    final_list = []
    dictionar = {}
    for lst in all_lists:
        for character in lst:
            if character in dictionar:
                dictionar[character] += 1
            else:
                dictionar[character] = 1
    for key in dictionar:
        if dictionar.get(key) == n:
            final_list.append(key)
    return final_list


print("Ex6 - char with n appearances")
print(char_with_n_appearances(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))


# 7
def validate_palindrom(nr):
    "Validates if the given number is a palindrome"
    str_nr = str(nr)
    reverse_nr = str_nr[::-1]
    return str_nr == reverse_nr

def palindroms(numbers):
    "Returns the number of palindrome numbers and the greatest palindrome from a given list"
    final_list=[]
    max_palindrome = 0
    palindrome_counter=0
    for number in numbers:
        if validate_palindrom(number):
            palindrome_counter+=1
            if number>max_palindrome:
                max_palindrome=number
    final_list.append(palindrome_counter)
    final_list.append(max_palindrome)
    return(tuple(final_list))
print('Ex 7 - nr of palindromes and the greatest palindrome')
print(palindroms([10,11,171,121,333,5005,404,9]))
# 8
def ascii_divisible(x=1, flag=True, *all_lists):
    'Returns each list with the characters that have ASCII code divisible with x if the flag is true, the others if not'
    final_list = []
    for each_list in all_lists:
        aux_list = []
        for letter in each_list:
            if flag:
                if ord(letter) % x == 0:
                    aux_list.append(letter)
            else:
                if ord(letter) % x != 0:
                    aux_list.append(letter)
        final_list.append(aux_list)
    return final_list


print("Ex 8 - ASCII")
print(ascii_divisible(2, False, "test", "hello", "lab002"))


# 9
def can_not_see(seats):
    "Returns the seats that have a smaller value than any seat in the front row "
    unlucky=[]
    for index,row in enumerate(seats):
        for column, value in enumerate(row):
            aux=index-1
            while(aux>=0):
                if(seats[aux][column]>value):
                    aux=0
                    unlucky.append((index,column))
                aux-=1
    return unlucky

print("Ex 9 - Stadium")

print(can_not_see([[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]] ))
# 10
def zip_tuple1(*lists):
    final_list = []
    most_elem = max([len(x) for x in lists])

    for i in range(most_elem):
        position_list = []
        for lst in lists:
            while len(lst) < most_elem:
                lst.append(None)
            position_list.append(lst[i])
        final_list.append(tuple(position_list))
    return final_list


print("Ex 10 - Zip")
print(zip_tuple1([1, 2, 3], [5, 6, 7], ["a", "b"]))


# 11

def sort_by_3rd_character_of_second_elem(*tuple):
    'Returns the tuples sorted by the 3rd char of the second elem of each tuple'
    return sorted(tuple, key=lambda x: x[1][2])


print("Ex 11 - sort by 3rd char tuple")
print(sort_by_3rd_character_of_second_elem(('abc', 'bcd'), ('abc', 'zza')))

# 12
def Rhymes(list):
    "Returns the words from the list grouped by rhyme"
    new_list = []
    for word in list:
        small_list = []
        last_2_chars = word[-1] + word[-2]
        #list.remove(word)
        for word2 in list:
            last_2_chars_second = word2[-1] + word2[-2]
            if last_2_chars_second == last_2_chars:
                small_list += [word2]
               # list.remove(word2)
        if new_list.count(small_list) == 0:
            new_list += [small_list]
    return new_list

print("Ex 12 - Ryhmes")
print(Rhymes(['ana', 'banana', 'carte', 'arme', 'parte']))