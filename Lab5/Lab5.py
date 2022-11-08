# Ex2
def keyword_arg_val(*args, **kwargs):
    sum = 0
    for kw in kwargs.keys():
        sum += int(kwargs[kw])
    return sum

def fy_function_ann(*args, **kwargs):
    return sum(list(map(lambda value: value, kwargs.values())))

print("Ex2 ----------------------------")
print("The sum of the values in anonymous function: ", fy_function_ann(1, 2, c=3, d=4))
print(keyword_arg_val(1, 2, c=3, d=4))

# Ex3

"""
3 methods to generate a list with all the vowels in the given string
"""


def method1(string_given):
    return [c for c in string_given if c in "aeiouAEIOU"]


def method2(string_given):
    vowels = []
    for char in string_given:
        if char in "aeiouAEIOU":
            vowels.append(char)
    return vowels


def method3(string_given):
    return list(filter(lambda c: c in "aeiouAEIOU", string_given))


print("Ex3 ----------------------------")
print(method1("Programming in Python is fun"))
print(method2("Programming in Python is fun"))
print(method3("Programming in Python is fun"))


# Ex4
def only_the_dictionaries(*args) -> list:
    """
    :return: list containing only the args which are dict with minimmum 2 keys and at least one string with minimmum 3 char
    """
    d = []
    for elem in args:
        if type(elem) is dict and len(str(elem)) >= 2:
            for k in elem.keys():
                if len(str(k)) >= 3:
                    d.append(elem)
                    break
    return d


print("Ex4 ----------------------------")
print(only_the_dictionaries({1: 2, 3: 4, 5: 6},
                            {'a': 5, 'b': 7, 'c': 'e'},
                            {2: 3},
                            [1, 2, 3],
                            {'abc': 4, 'def': 5},
                            3764,
                            {'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                            {1: 1, 'test': True}))


# Ex5

def only_numbers(list_input: list) -> list:
    """
    :param list_input: list with elements
    :return: a list with all the numbers found in the list given as a parameter
    """
    list_nr = []
    for element in list_input:
        if isinstance(element, int) or isinstance(element, float):
            list_nr.append(element)
    return list_nr


print("Ex5 ----------------------------")
print(only_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


# Ex6
def even_odd_pairs(list_integers: list) -> list:
    """
    :param list_integers: list of equal random ordered number of even and odd numbers
    :return: list of pairs (tuples of 2) of the i-th even number and i-th odd number
    """
    final_tuples = []
    even_nr = []
    odd_nr = []
    for element in list_integers:
        if element % 2 == 0:
            even_nr.append(element)
        else:
            odd_nr.append(element)
    for i in range(len(even_nr)):
        final_tuples.append((even_nr[i], odd_nr[i]))
    return final_tuples


print("Ex6 ----------------------------")
print(even_odd_pairs([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))


# Ex7

def fibonacci_list(n: int) -> list:
    """
    :param n: integer
    :return: list of the first n fibonacci numbers
    """
    list_of_fibo = [0]
    b = 1
    i = 0
    while i <= n:
        list_of_fibo.append(b)
        a = b
        b += a
        i += 1
    return list_of_fibo


def sum_digits(x):
    return sum(map(int, str(x)))


def process(**kwargs) -> list:
    """
    :param kwargs:list of parameters: filters(list of predicates), limit(amount of numbers), offset(skip e number of entries)
    :return:list of processed numbers according to the rules in the keyword args
    """
    list_after_filter = []
    fib = fibonacci_list(1000)
    list_after_filter_2 = []
    list_offset = []
    final_list = []
    for key, value in kwargs.items():
        if key == "filters":
            for predicate in value:
                list_i = []
                for nr in fib:
                    if predicate(nr) is True:
                        list_i.append(nr)
                list_after_filter.append(list_i)
            for i in range(1, len(list_after_filter)):
                for element1 in list_after_filter[i - 1]:
                    for element2 in list_after_filter[i]:
                        if element1 == element2:
                            list_after_filter_2.append(element1)
        elif key == "offset":
            for i in range(value):
                list_after_filter_2.pop(0)
                list_offset = list_after_filter_2
        elif key == "limit":
            for i in range(value):
                final_list.append(list_offset[i])

    return final_list


print("Ex7 ----------------------------")
print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], offset=2,
    limit=2))

# Ex8
# a)
print("Ex8 a)----------------------------")


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def f(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)

    return f


augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(10))
augmented_add_numbers = print_arguments(add_numbers)
print(augmented_add_numbers(3, 4))

# b)
print("Ex8 b) ----------------------------")


def multiply_output(function):
    def f(*args, **kwargs):
        return 2 * function(*args, **kwargs)

    return f


def multiply_by_three(x):
    return x * 3


augmented_multiply_by_three = multiply_output(multiply_by_three)
print(augmented_multiply_by_three(10))

# c)
print("Ex8 c) ----------------------------")


def augment_function(function, decorators):
    def f(*args, **kwargs):
        result = function
        for deco in decorators:
            result = deco(result)
        return result(*args, **kwargs)

    return f


decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
print(decorated_function(3, 4))


# Ex9

def operations(pairs: list) -> list:
    """
    :param pairs: list of pairs of integers
    :return: list of dictionaries for each pair with the sum,prod and pow of each pair numbers
    """
    list_of_operations = []
    for p in pairs:
        x, y = p
        list_of_operations.append({'sum': sum(p),
                                   ' prod': x * y,
                                   'pow': pow(x, y)})
    return list_of_operations


print("Ex9 ----------------------------")
print(operations([(5, 2), (19, 1), (30, 6), (2, 2)]))
