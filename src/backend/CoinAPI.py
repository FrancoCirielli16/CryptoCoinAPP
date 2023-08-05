from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from keys import COIN_API_TEST,COIN_API


url = COIN_API_TEST
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '16d3ed91-1857-492a-9903-ce8be1c08596',
}


def get_cryptos():
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters, headers= headers)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        
if __name__ == "__main__":
    get_cryptos()




