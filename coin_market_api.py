from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from functions import json_extract


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


# Driver code
print(get_coin_price("bitcoin"))
