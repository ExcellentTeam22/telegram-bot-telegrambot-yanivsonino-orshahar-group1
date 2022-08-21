import math


def is_prime(number):
    """
    Check if the given number is prime or not.
    :param number: The given number.
    :return: 'Prime' if number is prime or 'Not prime', or custom message if number is odd.
    """
    number = int(number)
    if number > 1:
        if number % 2 == 0:
            return "Come on dude, you know even numbers are not prime!"
        for i in range(2, number // 2):
            if (number % i) == 0:
                return "Not prime"
        else:
            return "Prime"
    else:
        return "Not prime"


def is_factorial(number):
    """
    Check if a given number is a factorial of any given number.
    :param number: The given number.
    :return: True if number is factorial or False if not.
    """
    number = int(number)
    i = 1
    while True:
        if number % i == 0:
            number //= i
        else:
            break
        i += 1
    if number == 1:
        return True
    else:
        return False


def is_palindrome(string):
    """
    Check if a given string is a palindrome.
    :param string: The given string.
    :return: True if string is palindrome or False if not.
    """
    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def is_perfect_square(number):
    """
    Check if a given number have an integer square root.
    :param number: The given number.
    :return: True if the number has an integer square root or False if not.
    """
    number = int(number)
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

# def check_args(dic:dict):
#     if len(dic.keys()) == 1:


def help(*args):
    """
    help commands
    :param args: none
    :return str: Help menu.
    """
    return """Use the following commands
    /help - Show commands
    /add {COIN NAME} - To add coin
    /check {COIN NAME} - Check coin 
    """


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values[0]
