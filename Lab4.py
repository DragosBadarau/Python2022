import os
import sys
from os.path import join



# Ex1

def order_extensions(directory) -> list:
    """
    :param directory: the path to the directory from which the files and their extensions are ordered
    :return: a list with all the unique file extensions sorted
    """
    list_of_extensions = []
    for root, directories, files in os.walk(directory):
        for file_name in files:
            ext = os.path.splitext(file_name)[1][1:]
            if ext and ext not in list_of_extensions:
                list_of_extensions.append(ext)
    list_of_extensions.sort()
    return list_of_extensions


print('Ex1 -----------------------------------------------')
print(order_extensions('E:\FACULTATE\Anul3Sem 1\Python\Python2022'))


# Ex2
def each_file_starting_with_A(director, fisier):
    """
    :param director: the path to the director from which the 'A' starting name of files are taken
    :param fisier: where the absolute path of the 'A' starting name of the files is written
    """
    try:
        with open(fisier, "w") as f:
            for el in os.listdir(director):
                name = os.path.join(director, el)
                if os.path.isfile(name) and el.startswith("A"):
                    print(repr(os.path.abspath(name) + os.linesep))
                    f.write(os.path.abspath(name) + os.linesep)
    except Exception as e:
        print(str(e))


print('Ex2 -----------------------------------------------')
print(each_file_starting_with_A('E:\FACULTATE\Anul3Sem 1\Python\Python2022', 'Lab4_ex2.txt'))


# Ex3

def ex3(my_path):
    """
    :param my_path: path to a file or directory
    :return: if is a path to a file: the last 20 characters of the file
                    if is a path to a directory: a list of tuples made of all the unique extensions and how many there are
    """
    if os.path.isfile(my_path):
        with open(my_path, 'r') as r:
            text = r.read()
        if len(text) >= 20:
            return text[-20:]
        else:
            raise Exception("The file does not contain 20 characters!")
    elif os.path.isdir(my_path):
        list_of_extensions = []
        unique_extensions = []
        for root, directories, files in os.walk(my_path):
            for file_name in files:
                ext = os.path.splitext(file_name)[1][1:]
                if ext:
                    list_of_extensions.append(ext)
                    if ext not in unique_extensions:
                        unique_extensions.append(ext)
        tuple_list = []
        for ext in unique_extensions:
            tuple_list.append((ext, list_of_extensions.count(ext)))
        sorted_list = sorted(tuple_list, key=lambda i: i[1], reverse=True)
        return sorted_list
    else:
        print("The path introduced is invalid!")


print('Ex3 -----------------------------------------------')
print(ex3('E:\FACULTATE\Anul3Sem 1\Python\Python2022\Lab4.py'))


# Ex4
def list_of_unique_extensions() -> list:
    """
    :return:list of unique extensions found in the directory given as a command line parameter
    """
    try:
        assert (os.path.isdir(sys.argv[1])), "Invalid director"
        return sorted(list(set([os.path.splitext(el)[1][1:] for el in os.listdir(sys.argv[1]) if
                                os.path.isfile(os.path.join(sys.argv[1], el)) and os.path.splitext(el)[1] != ""])))
    except IndexError:
        print("Not enough arguments!")
    except Exception as e:
        print(str(e))
        return []


print('Ex4 -----------------------------------------------')
print(list_of_unique_extensions())


# Ex5
def search_by_content(target, to_search):
    """
    :param target:the path from which the search begins(directory or file)
    :param to_search: the string searched
    :return: the files that contain the string searched
    """
    try:
        if os.path.isfile(target):
            with open(target, "r") as f:
                data = f.read()
                if to_search in data:
                    return target
            return None
        elif os.path.isdir(target):
            file_list = []
            for root, directories, files in os.walk(target):
                for file_name in files:
                    # print(file_name)
                    new_file = search_by_content(os.path.join(target, file_name), to_search)
                    if new_file:
                        file_list.append(new_file)
            return file_list
    except ValueError:
        print("The first argument must be a path to a directory/file!")


print('Ex5 -----------------------------------------------')
print(search_by_content('E:\FACULTATE\Anul3Sem 1\Python\Python2022', 'print'))


# Ex6
def callback_function(target, to_search, callback):
    """
    :param target:the path from which the search begins(directory or file)
    :param to_search: the string searched
    :param callback: callback function for each error
    :return: the files that contain the string searched
    """
    try:
        return search_by_content(target, to_search)
    except Exception as e:
        callback(e)
        return []


print('Ex6 -----------------------------------------------')
print(callback_function('E:\FACULTATE\Anul3Sem 1\Python\Python2022', 'print', 'smth'))


# Ex7
def get_file_info(path) -> dict:
    """
    :param path:the path to the file
    :return: infos about the file given
    """
    dictionary = {}
    try:
        if os.path.isfile(path):
            dictionary.update({'full_path': os.path.dirname(path),
                               "file_size": os.path.getsize(path),
                               "file_extension": os.path.splitext(path)[1],
                               "can_read": os.access(path, os.R_OK),
                               "can_write": os.access(path, os.W_OK)})
        return dictionary
    except Exception as e:
        print(str(e))


print('Ex7 -----------------------------------------------')
print(get_file_info('E:\FACULTATE\Anul3Sem 1\Python\Python2022\Lab4.py'))


# Ex8
def list_of_all_files(dir_path) -> list:
    """
    :param dir_path:the path from which the search begins;
    """
    file_list = []
    for root, directories, files in os.walk(dir_path):
        for file_name in files:
            file_list.append(join(dir_path, file_name))
    return file_list


print('\nEX8----------------------------------------')
# print(list_of_all_files('E:\FACULTATE'))
