
import argparse
import pymysql

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

def get_bybit_price(common_symbol, bybit_api_key, bybit_api_secret):
    # Implement your Bybit price fetching logic here
    # Make API request to Bybit and return the response
    # Ensure you handle errors and return a well-structured response

def main():
    parser = argparse.ArgumentParser(description='Fetch API keys and prices for a given coin symbol.')
    parser.add_argument('--symbol', required=True, help='The common symbol of the coin (e.g., BTC, ETH)')

    args = parser.parse_args()

    chosen_common_symbol = args.symbol

    try:
        # Fetch API keys from the database based on the chosen common_symbol
        api_keys = get_api_keys(chosen_common_symbol)

        if api_keys is None:
            print(f"API keys not found for {chosen_common_symbol}. Please check your configuration.")
        else:
            print(f"API keys fetched successfully for {chosen_common_symbol}:")
            print(f"Binance API Key: {api_keys[0]}")
            print(f"Binance API Secret: {api_keys[1]}")
            print(f"Bybit API Key: {api_keys[2]}")
            print(f"Bybit API Secret: {api_keys[3]}")

            # Fetch Bybit price
            bybit_response = get_bybit_price(chosen_common_symbol, api_keys[2], api_keys[3])
            print("Bybit Response:", bybit_response)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
