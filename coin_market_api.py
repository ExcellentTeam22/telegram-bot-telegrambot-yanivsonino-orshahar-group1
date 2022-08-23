from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def get_coin_price(coin_name):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'slug': coin_name.lower(),
        'convert': 'USD',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'be3cdc10-1d65-42c2-ad95-75c7d64a2738',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        return json_extract(response.json(), 'price')
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_gain_loss_value(coin_name, initial_value, investment):
    """
    Calculate the gain or loss value for the investment.
    :param coin_name: The coin that was initially invested in.
    :param initial_value: The initial value of the crypto.
    :param investment: The amount of USD invested in the coin.
    :return: The current gain or loss for the investment.
    """
    current_price = get_coin_price(coin_name)
    print("current price is {}".format(current_price))
    return investment * ((float(current_price) - initial_value) / initial_value) / 100


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


# Driver code
invest = 100
previous_price = 21389.47
gain_loss = get_gain_loss_value("bitcoin", previous_price, invest)
print("You earned: " if gain_loss > 0 else "You lost: ")
print("{0} ({0:.1%})".format(gain_loss, gain_loss))
print("You had {0} and now you have {1}".format(invest, (gain_loss + invest)))
