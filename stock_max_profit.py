class NoneError(Exception):  # Custom exception to raise the None value error in get_max_profit function
    pass


def get_max_profit(stock_prices_yesterday):
    try:
        if stock_prices_yesterday == []:
            raise NoneError("No stock price list from yesterday")

        buy_price = min(stock_prices_yesterday)  # Gets the lowest price from yesterday's stock price
        # Provide a starting value for next_available_price_index variable, so it can be used in the for loop
        next_available_price_index = 0
        for i, price in enumerate(stock_prices_yesterday):
            if price == buy_price:
                next_available_price_index = i + 2  # Skipping an index as next transaction cannot be performed until
                # a minute has passed
        sell_price = max(stock_prices_yesterday[next_available_price_index:])   # Picks the highest sellable
        # price after the one-minute mark of buying the stock
        profit = sell_price - buy_price
        return profit

    except (TypeError, ValueError, Exception) as e:
        print(f'Error: {e}')
