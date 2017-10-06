import re
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/'


if __name__ == '__main__':

    ip = input('Please enter ip ')

    response = urlopen(url+ip)
    data = json.load(response)

    city = data['city']

    print('City ': city)
