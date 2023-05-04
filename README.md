# Overview

This is a simple python code to calculate best profit one could have made by 1 purchase
and 1 sale of Latitude Financial stock yesterday.

# Considerations

* The indices are the time in minutes past trade opening time (10:00am local time) which
means list[0] is 10:00am and list[1] is 10:01am
* The values are the price in dollars of the Latitude Financial stock at that time
* One needs to buy the stock before selling it
* One cannot buy and sell the stock in adjacent time (at least a minute must have passed
between the purchase and sale)

# Prerequisite

* python 3.10
* pytest

# Installing python

* Download python 3.10 using below link:
https://www.python.org/downloads/release/python-3106/
For e.g. it can be also be downloaded using below commands in the CLI in ubuntu:
* sudo apt-get install python3 
* Or you can specify a particular version using below command:
* sudo apt-get install python3.10

# Installing Dependencies and Running test case

* Download this folder to your local system
* cd to this folder, for e.g. cd ~/path/to/folder/latitude_stock_profit
* Install dependencies `pip install -r requirements.txt`
* Run the test case with the following command:
* `pytest tests_stock_max_profit.py`