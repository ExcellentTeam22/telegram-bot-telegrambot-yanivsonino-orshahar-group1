import math


def is_prime(number):
    """
    Check if the given number is prime or not.
    :param number: The given number.
    :return: True if number is prime or False if number is not prime.
    """
    if number > 1:
        for i in range(2, number // 2):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False


def is_factorial(number):
    """
    Check if a given number is a factorial of any given number.
    :param number: The given number.
    :return: True if number is factorial or False if not.
    """
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
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True


def is_perfect_square(number):
    """
    Check if a given number have an integer square root.
    :param number: The given number.
    :return: True if the number has an integer square root or False if not.
    """
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False
