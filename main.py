from func_connections import connect_dydx
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_private import abort_all_open_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results

if __name__ == "__main__":
    # print("Hello bot!")
    # Connet to client
    try:
        print("connecting to client...")
        client = connect_dydx()
    except Exception as e:
        print(e)
        print("Error connecting to client: ", e)
        exit(1)

# Abort all open positions
if ABORT_ALL_POSITIONS:
    try:
        print("closing all positions...")
        close_orders = abort_all_open_positions(client)
    except Exception as e:
        print("Error closing all positions: ", e)
        exit(1)


# Find cointegrated pairs
if FIND_COINTEGRATED:
    # Construct market prices
    try:
        print("Fetching market prices, please allow 3 minutes...")
        df_market_prices = construct_market_prices(client)
    except Exception as e:
        print("Error constructing market prices: ", e)
        exit(1)

    # Store cointegrated pairs
    try:
        print("Storing cointegrated pairs...")
        stores_result = store_cointegration_results(df_market_prices)
        if stores_result != "saved":
            print("Error saving cointegrated pairs")
            exit(1)
    except Exception as e:
        print("Error saving cointegrated pairs: ", e)
        exit(1)