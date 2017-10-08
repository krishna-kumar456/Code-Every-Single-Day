from bs4 import BeautifulSoup
import requests
import re


URL = 'https://www.whois.com/whois/'

if __name__ == '__main__':

    lookup = input('Please enter input ')
    urlLookup = URL + lookup

    r = requests.get(urlLookup)

    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.prettify())

    result = soup.find_all(attrs={"class": "df-value"})

    print(result[0])

    
