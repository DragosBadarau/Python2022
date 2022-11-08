__doc__ = """
1) 
a) Write a module named utils.py that contains one function called process_item. 
The function will have one parameter, x, and will return the least prime number greater than x.
When run, the module will request an input from the user, convert it to a number and it will display 
 the output of the process_item function.
"""

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

def process_item(x):
    max_size = int(1e6)
    for i in range(x + 1, max_size):
        if is_prime(i):
            return i


if __name__ == "__main__":
    try:
        print(process_item(int(input("Enter the integer: \n"))))
    except Exception as e:
        print(e)
