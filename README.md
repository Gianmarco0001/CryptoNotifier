# CryptoVisualizer

CryptoNotifier is a simple desktop application built with PyQt5 that allows users to get the latest price of cryptocurrencies and a recommendation based on the percentage change in the last 24 hours. Please note that the program shows only values in euros and is currently available only in Italian.

# Installation

To use CryptoNotifier, you need to have Python 3 installed on your system. You can download it from the official website: https://www.python.org/downloads/

Next, install the required dependencies by running the following command in your terminal:

`python3 -m pip install pyqt5 requests`

# Usage

To launch CryptoNotifier, navigate to the project directory and run the following command in your terminal:

`python3 CryptoNotifier.py`

Once the application is launched, enter the currency symbol of the cryptocurrency you want to monitor (e.g. BTC, XMR, ETH) and click the "Invia" button to get the latest price and recommendation. The application uses CoinMarketCap API to fetch the latest price and percentage change.

You can also enter your API Token to get 333 requests per day and 10.000 per month. To do this, register on the CoinMarketCap website. It's free!

# Disclaimer

CryptoNotifier provides only a general recommendation and does not take into account your personal circumstances. Please conduct your own research and evaluation before making any investment decision.

# Credits

CryptoNotifier uses the CoinMarketCap API to fetch the latest price and percentage change.
