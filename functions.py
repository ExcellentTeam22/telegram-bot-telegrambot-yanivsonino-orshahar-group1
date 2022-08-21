import math

from Database import CoinsTable
import pandas as pd

#print(CoinsTable().print_coins('name-1891496051'))
def is_prime(message: dict):
    """
    Check if the given number is prime or not.
    :param message: The given number.
    :return: 'Prime' if number is prime or 'Not prime', or custom message if number is odd.
    """
    number = int(message['text'].split()[1])
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


def is_factorial(message):
    """
    Check if a given number is a factorial of any given number.
    :param message: The given number.
    :return: True if number is factorial or False if not.
    """
    number = int(message['text'].split()[1])
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


def is_palindrome(message):
    """
    Check if a given string is a palindrome.
    :param message: The given string.
    :return: True if string is palindrome or False if not.
    """
    string = message['text'].split()[1]

    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

def show_coins(message):
    return CoinsTable().print_coins(message['name'])

def is_perfect_square(message):
    """
    Check if a given number have an integer square root.
    :param message: The given number.
    :return: True if the number has an integer square root or False if not.
    """
    number = int(message['text'].split()[1])
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False


def add(message: dict):
    coin_name = message['text'].split()[1]
    invest_value = message['text'].split()[2]
    if len(message['text'].split()) < 2:
        curr_value = get_coin_curr_value(message['text'].split()[1])
    else:
        curr_value = int(message['text'].split()[3])
    coins = float(curr_value) / float(invest_value)
    current_data_frame = pd.DataFrame([[coin_name, invest_value, curr_value, coins]],
                                      columns=["Coin Name", "Invest", "First Value", 'Coins'])
    res ={0: 'Not Added', 1: 'Added Successfully'}
    return res[CoinsTable().add_coin(current_data_frame, message['name'])]


def get_coin_curr_value(coin_name: str):
    return 100


def help(message):
    """
    help commands
    :param message:
    :return str: Help menu.
    """
    return """Use the following commands
    /help - Show commands
    /add *{COIN NAME} *{INVEST VALUE} {COIN VALUE} - To add coin
    /check *{COIN NAME} - Check coin 
    notes:
    * is must argument
    """
