#API - 3OMNY8AGR9M9QYMT
import requests


def get_quotes(symbol):
    """ Helper function to fetch quotes data from alphavantage api.
    """

    result = {}

    apiUrl = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + symbol + "&apikey=3OMNY8AGR9M9QYMT"

    try:
        r = requests.get(apiUrl)
        response = r.json()

        latestDate = response['Meta Data']['3. Last Refreshed']

        for k,v in response['Time Series (Daily)'].items():
            if k == latestDate:
                result['open'] = v['1. open']
                result['high'] = v['2. high']
                result['low'] = v['3. low']
                result['close'] = v['4. close']

    except Exception as e:
        return str(e)

    return result


if __name__ == '__main__':

    input_symbol = input('Please enter symbol')
    data = get_quotes(input_symbol)

    for k,v in data.items():
        print(k, v)
