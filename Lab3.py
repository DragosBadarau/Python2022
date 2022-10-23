# 1
def lists_operations(l1: list, l2: list) -> list:
    """Returns the union, intersection and difference of two lists as a list of sets"""
    result = (set(l1) & set(l2)), set(l1) | set(l2), set(l1) - set(l2), set(l2) - set(l1)
    return list(result)


print("Ex1 - Operations")
print(lists_operations([1, 5, 10, 20], [2, 10, 20, 30]))


# 2
def appearances(text) -> dict:
    """
    Dictionary with the number of appearances of each character in the given text
    """
    dictionary = {}
    for character in text:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary


print("Ex2 - Dictionary with appearances")
print(appearances("Ana has apples."))


# 3
def different_lst(lst1, lst2):
    """
    :return: True if two lists/tuples lst1 and lst2 are different, False otherwise
    """
    # print(lst1, lst2)
    lst1 = list(lst1)
    lst2 = list(lst2)
    # print(lst1, lst2)
    if len(lst1) != len(lst2):
        # print(len(lst1), len(lst2))
        return True

    for a, b in zip(lst1, lst2):
        if type(a) == type(b):
            if type(a) in (int, float, str):
                if a != b:
                    # print(a, b)
                    return True
            elif type(a) in (list, tuple):
                if different_lst(a, b):
                    return True
            elif type(a) is dict:
                if different_dict(a, b):
                    return True
        else:
            return True
    return False


def different_dict(dict1: dict, dict2: dict):
    """
    :return: True if two dictionaries dict1, dict2 are different, False otherwise
    """
    if len(dict1) != len(dict2):
        return True

    for a, b in zip(dict1, dict2):  # verific cheile pe perechi
        if type(a) == type(b):
            # print(a, b)
            if type(a) in (int, float, str):
                if a != b:
                    # print(a, b)
                    return True
                if type(dict1[a]) == type(dict2[b]):  # verific valorile cheilor pe perechi
                    # print(dict1[a], dict2[b])
                    if type(dict1[a]) in (int, float, str):
                        if dict1[a] != dict2[a]:
                            return True
                    if type(dict1[a]) in (tuple, list):
                        if different_lst(dict1[a], dict2[b]):
                            return True
                    elif type(dict1[a]) is dict:
                        # print("dict again")
                        if different_dict(dict1[a], dict2[b]):
                            return True
                else:
                    return True
            if type(a) is tuple:
                # print("TUPLE" + str(a) + str(b))
                if different_lst(a, b):
                    # print("same tuples")
                    return True
                if type(dict1[a]) == type(dict2[b]):  # verific valorile cheilor pe perechi
                    # print(dict1[a], dict2[b])
                    if type(dict1[a]) in (int, float, str):
                        if dict1[a] != dict2[a]:
                            return True
                    if type(dict1[a]) in (tuple, list):
                        if different_lst(dict1[a], dict2[b]):
                            return True
                    elif type(dict1[a]) is dict:
                        if different_dict(dict1[a], dict2[b]):
                            return True
                else:
                    return True
    return False


print("Ex3 - different dictionaries")
print(different_dict({'smth': {'50': 100, 'pa': 10.2}, 'da': 'da'},
                     {'smth': {'50': 100, 'pa': 10.1}, 'da': 'da'}))
print(different_dict({'smth': [10, [11, 15]], 'kat': {10.99: {'discount': 15}}},
                     {'smth': [10, [11, 15]], 'kat': {10.99: {'discnt': 15}}}))
print(different_dict({(10, 11): 10, 0.4: 15, 'smth': ['key', {'another': 10}]},
                     {(10, 11): 10, 0.4: 15, 'smth': ['key', {'another': 10}]}))


# 4
def build_xml_element(tag, content, **attributes):
    """Builds an XML element with the given parameters"""
    return f'"<{tag} href="{attributes["href"]}_class{attributes["_class"]}" id="{attributes["id"]}">{content}<{tag}>'


print("Ex4 - XML ")
print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))


# 5
def validate_dict(rules, dictionary):
    """
    Returns true or false if the given dictionary respects the given rules
    """
    for dicti in dictionary:
        ok = 0
        for rule in rules:
            if dicti in rule:
                ok = 1
        if ok == 0:
            return False

    for rule in rules:
        left_rule = rule[1]
        mid_rule = rule[2]
        right_rule = rule[3]
        unique_text = dictionary[rule[0]]
        if not (unique_text.startswith(left_rule) and unique_text.endswith(
                right_rule) and mid_rule in unique_text and not unique_text.startswith(
            mid_rule) and not unique_text.endswith(mid_rule)):
            return False
    return True


print("Ex5 - Dictionary with rules")
print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
                    {"key2": "starting the engine in the middle of the winter",
                     "key1": "come inside, it's too cold outside"
                        , "key3": "this is not valid"
                     }))


# 6
def unique_and_duplicate(elements: list) -> tuple:
    """
    :return: tuple representing the unique elements and the number of duplicates
    """
    unique = len(set(elements))
    duplicates = len(elements) - unique
    return unique, duplicates


print("Ex6 - Number of Uniques and Duplicates")
print(unique_and_duplicate([10, 11, 12, 12, 10, 14, 15, 11, 15, 16, 17, 19, 16, 20, 20]))


# 7
def dictionary_from_sets(*s: set) -> dict:
    """Returns all the combinations of two by two sets by using the afferent operation"""
    dictionary = {}
    for i, elem1 in enumerate(s[:len(s) - 1]):
        for elem2 in s[i + 1:]:
            dictionary[str(elem1) + ' | ' + str(elem2)] = elem1.union(elem2)
            dictionary[str(elem1) + ' & ' + str(elem2)] = (elem1.intersection(elem2))
            dictionary[str(elem1) + ' - ' + str(elem2)] = (elem1.difference(elem2))
            dictionary[str(elem1) + ' _ ' + str(elem2)] = elem2.difference(s[i])
    return dictionary


print("Ex7 - dictionary of operations with sets")
print(dictionary_from_sets({1, 5, 10}, {2, 6, 10}, {14, 50}, {50, 5}, {'python'}))


# 8
def loop_in_dictionary(elements: dict) -> list:
    """
    :return: List of objects by adding the value of the key's ('start') value until loop
    """
    iterated_elems = set()
    current_elem = elements['start']
    while current_elem not in iterated_elems:
        iterated_elems.add(current_elem)
        current_elem = elements[current_elem]
    return list(iterated_elems)


print("Ex8 - Loop in the dictionary")
print(loop_in_dictionary({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# 9

def positional_found_in_keyword(*positional, **keywords):
    """
    :param positional: positional arguments
    :param keywords: keywords arguments
    :return: the number of positional arguments whose values can be found among keyword arguments values
    """
    counter = 0
    for elem in positional:
        for key in keywords:
            if keywords[key] == elem:
                counter += 1
    return counter


print("Ex9 - Positional arguments found in keyword arguments")
print(positional_found_in_keyword(1, 2, 3, 4, x=1, y=2, z=3, w=5))
