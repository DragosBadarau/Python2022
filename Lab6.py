import re
import os


# ex1
def word_extractor(text: str):
    """
    :param text: string of characters
    :return: the words from the given parameter
    """
    words = re.findall("[A-z0-9]+", text)
    if words:
        return words


print(word_extractor("Here is the givVen  , text!!!"))


# ex2

def matchy_substrings(regex_string, text, x):
    """
    :param regex_string: regex string
    :param text: text string
    :param x: number
    :return: the substrings of length x from the given text that match the regex
    """
    return list(filter(lambda word: len(word) == x, re.findall(regex_string, text)))


# ex3

def at_least_one_matchy(text_chars, list_of_regular_exp):
    """
    Write a function that receives as a parameter a string of text characters and a list of regular expressions
    :param text:
    :param list_of_re:
    :return: a list of strings that match on at least one regular expression given as a parameter.
    """
    return [word for word in text_chars if any([re.search(r, word) for r in list_of_regular_exp])]


# ex 4

def elements_from_xml(path_to_xml, attrs):
    """
    :param path_to_xml: path to a xml document
    :param attrs: dictionary
    :return: the tags with the corresponding values from the dictionary
    """
    result = []
    with open(path_to_xml, "r") as f:
        data = f.read()
        for elem in re.findall("<\w+.*?>", data):
            if all([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", elem, flags=re.I) for item in attrs.items()]):
                result.append(elem)
    return result


# ex 6

def censorship(text: str):
    """
    :param text: text string
    :return: the given parameter formed of censured words that begin and end with vowels
    """
    low_s = text.group(0).lower()
    if not (low_s[0] in "aeiou" and low_s[-1] in "aeiou"):
        censored = text.group(0)
    else:
        censored = "".join([ch if idx % 2 == 0 else '*' for idx, ch in enumerate(text.group(0))])
    return re.sub("\w+", censored, text)


# ex 7

def valid_CNP(string):
    """
    :param string: unverified CNP
    :return: true if it is a correct CNP. false otherwise
    """
    return re.match(r"[1256]\d\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{6}$", string) != None


# ex 8

def matchy_files(directory, reg):
    """
    :param directory: directory
    :param reg: regular expression
    :return: the files that the directory contains whose names match the given regular expression prefixed with ">>"
    """
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_name = os.path.join(root, file)
            r = re.search(reg, file)
            if r:
                result.append(file)
            try:
                with open(file_name, "r") as d:
                    data = d.read()
                    if re.search(reg, data):
                        if r:
                            result[-1] = ">>" + result[-1]
                        else:
                            result.append(file)
            except Exception as e:
                print(str(e))
    return result
