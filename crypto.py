
import argparse
import requests
import pymysql

def get_prices(common_symbol):
    try:
        # Fetch API keys from the database based on common_symbol
        api_keys = get_api_keys(common_symbol)

        if api_keys is None:
            print(f"API keys not found for {common_symbol}. Please check your configuration.")
            return None

        # Extract API keys from the tuple
        binance_api_key, binance_api_secret, bybit_api_key, bybit_api_secret = api_keys

        # Fetch prices from Binance and Bybit
        binance_price = fetch_binance_price(common_symbol, binance_api_key, binance_api_secret)
        bybit_price = fetch_bybit_price(common_symbol, bybit_api_key, bybit_api_secret)

        return binance_price, bybit_price

    except Exception as e:
        print(f"Error: {e}")
        return None

import requests

def fetch_binance_price(common_symbol, api_key, api_secret):
    base_url = "https://api.binance.com/api/v3/ticker/price"
    symbol = common_symbol + "USDT"
    params = {"symbol": symbol}

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'price' in data:
        return float(data['price'])
    else:
        return None





import requests

def fetch_bybit_price(common_symbol, api_key, api_secret):
    base_url = "https://api.bybit.com/v2/public/tickers"
    symbol = common_symbol + "USD"
    params = {"symbol": symbol}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()

        if 'result' in data and data['result'] is not None and isinstance(data['result'], list):
            result_list = data['result']
            
            if result_list:
                return float(result_list[0].get('last_price', 0))
            else:
                print(f"No data found for {symbol} in the Bybit response.")
                return None
        else:
            print(f"Unexpected response format from Bybit API: {data}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Bybit API: {e}")
        return None






def get_api_keys(common_symbol):
    try:
        # Establish a connection to the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Newpassword18702#',
            database='crypto_data'
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Fetch API keys from the database based on common_symbol
        cursor.execute(f"SELECT binance_api_key, binance_api_secret, bybit_api_key, bybit_api_secret FROM symbol_mapping WHERE common_symbol = '{common_symbol}'")
        api_keys = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return api_keys

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Fetch prices for a given coin symbol from Binance and Bybit.')
    parser.add_argument('--symbol', required=True, help='The common symbol of the coin (e.g., BTC, ETH, etc.)')

    args = parser.parse_args()

    chosen_common_symbol = args.symbol

    try:
        # Fetch prices from Binance and Bybit based on the chosen common_symbol
        prices = get_prices(chosen_common_symbol)

        if prices is not None:
            binance_price, bybit_price = prices
            print(f"Prices fetched successfully for {chosen_common_symbol}:")
            print(f"Binance Price: {binance_price}")
            print(f"Bybit Price: {bybit_price}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
