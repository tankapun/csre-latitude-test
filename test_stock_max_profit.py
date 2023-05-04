import unittest
from stock_max_profit import get_max_profit

class TestGetMaxProfit(unittest.TestCase):
    def test_valid_input(self):
        stock_prices_yesterday = [30, 28, 26, 17, 11, 3, 23, 8, 12, 11, 15, 6, 16, 14]
        expected_result = 13
        self.assertEqual(get_max_profit(stock_prices_yesterday), expected_result)

    def test_negative_input(self):
        stock_prices_yesterday = [-10, -5, -3, -4, -2]
        expected_result = 8
        self.assertEqual(get_max_profit(stock_prices_yesterday), expected_result)

    def test_empty_input(self):
        stock_prices_yesterday = []
        expected_result = None
        self.assertEqual(get_max_profit(stock_prices_yesterday), expected_result)

    def test_alph_numeric_input(self):
        stock_prices_yesterday = ['a', 'b', 'c', 2, 4, 6]
        expected_result = None
        self.assertEqual(get_max_profit(stock_prices_yesterday), expected_result)

    if __name__ == '__main__':
        unittest.main()
