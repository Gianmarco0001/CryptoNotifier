# CryptoNotifier

CryptoNotifier is a simple desktop application built with PyQt5 that allows users to get the latest price of cryptocurrencies and a recommendation based on the percentage change in the last 24 hours. 

! The software is currently available only in Italian language.

# Installation

To use CryptoNotifier, you need to have Python 3 installed on your system. You can download it from the official website: https://www.python.org/downloads/

Next, install the required dependencies by running the following command in your terminal:

`python3 -m pip install pyqt5 requests`

# Usage

To launch CryptoNotifier, navigate to the project directory and run the following command in your terminal:

`python3 CryptoNotifier.py`

Once the application starts, enter the symbol of the cryptocurrency you want to observe (e.g., BTC, XMR, ETH) in the input box, select the fiat currency you want to convert to, and click the "Invia" button. The application will display the latest price of the cryptocurrency in the selected fiat currency and a recommendation on whether to buy or not based on the price change in the last 24 hours.

You can also enter your API Token to get 333 requests per day and 10.000 per month. To do this, register on the CoinMarketCap website. It's free!

# Disclaimer

This application provides only general advice and does not take into account the user's personal circumstances. Please do your own research before making any investment decisions.

# Credits

CryptoNotifier uses the [CoinMarketCap](https://coinmarketcap.com/) API to fetch the latest price and percentage change.

# License

This project is licensed under the Apache-2.0 license.
