import json  # we import the json library to work with the JSON format returned by the CoinMarketCap API
import requests  # we use the requests library to make HTTP requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QStyleFactory
from PyQt5.QtCore import pyqtSignal, Qt, QSettings

api_key = "351c3ef8-6ff0-4b6f-9c58-fe2d79644d6d"  # this is our API key from CoinMarketCap

def get_crypto_price(symbol, convert):

    #"""This function makes a GET request to the CoinMarketCap API to retrieve the latest price of a given cryptocurrency."""
    
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"  # endpoint for the API
    params = {"symbol": symbol, "convert": convert}  # parameters for the API request
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": api_key}  # headers for the API request

    with requests.get(url, params=params, headers=headers) as response:  # send the request and store the response
        try:
            data = response.json()["data"][symbol]["quote"][convert]  # extract the price from the JSON response
            price = round(data["price"], 2)  # round the price to two decimal places
            return price
        except (KeyError, TypeError, ValueError):
            return None

class CryptoNotifier(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        
    def initUI(self):

        #"""This function initializes the GUI elements for the CryptoNotifier app."""

        self.setWindowTitle("CryptoNotifier")
        self.setFixedSize(560, 300)

        vbox = QVBoxLayout()

        # Add alert message
        alert_msg = QLabel("Attenzione: questo programma fornisce solo un consiglio generale e non tiene conto delle condizioni personali dell'utente. Si prega di effettuare la propria valutazione prima di prendere qualsiasi decisione di investimento.")
        alert_msg.setWordWrap(True)
        vbox.addWidget(alert_msg)

        # Add welcome message
        welcome_msg = QLabel("Benvenuto in CryptoNotifier, inserisci la sigla della criptovaluta che vuoi osservare: (Ad esempio BTC, XMR, ETH)")
        vbox.addWidget(welcome_msg)

        # Add input box for currency symbol
        self.input_box = QLineEdit(self)
        vbox.addWidget(self.input_box)

        # Add input box for convert currency
        convert_hbox = QHBoxLayout()
        convert_label = QLabel("Valuta Fiat:")
        convert_label.setFixedWidth(100)
        self.convert_box = QComboBox()
        self.convert_box.addItems(["USD", "EUR", "GBP", "JPY"])  # list of supported fiat currencies
        convert_hbox.addWidget(convert_label)
        convert_hbox.addWidget(self.convert_box)
        vbox.addLayout(convert_hbox)

        # Add button to get crypto price
        get_price_button = QPushButton("Invia", self)
        get_price_button.clicked.connect(self.on_get_price)  # connect the button to the function that gets the price
        vbox.addWidget(get_price_button)

        self.setLayout(vbox)

        # Add label to display crypto price
        self.price_label = QLabel(self)
        self.price_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.price_label)

        # Add label to display recommendation
        self.recommendation_label = QLabel(self)
        self.recommendation_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.recommendation_label)

        # Add exit button
        exit_button = QPushButton("Esci", self)
        exit_button.clicked.connect(self.close)
        vbox.addWidget(exit_button)

        # Add credits label
        credits_label = QLabel("Dati forniti da <a href='https://coinmarketcap.com/'>CoinMarketCap</a>")
        credits_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(credits_label)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)

    def on_get_price(self):
        currency_symbol = self.input_box.text().upper()
        convert_currency = self.convert_box.currentText().upper()  # Get selected fiat currency
        price = get_crypto_price(currency_symbol, convert_currency)
        
        if price is not None:
            self.price_label.setText(f"Prezzo di {currency_symbol}: {price} {convert_currency}")
        
            # Check price change in the last 24 hours
            url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
            params = {"symbol": currency_symbol, "convert": "EUR"}
            headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": api_key}

            with requests.get(url, params=params, headers=headers) as response:
                if response.ok:
                    data = response.json()["data"][currency_symbol]["quote"]["EUR"]
                    percent_change_24h = data["percent_change_24h"]
                
                    if percent_change_24h > 0:
                        recommendation = f"{currency_symbol} è aumentata del {round(percent_change_24h, 2)}% nelle ultime 24 ore. Potrebbe non valere la pena acquistare"
                    elif percent_change_24h < 0:
                        recommendation = f"{currency_symbol} è diminuita del {round(percent_change_24h, 2)}% nelle ultime 24 ore. Potrebbe valere la pena acquistare!"
                    else:
                        recommendation = f"{currency_symbol} non ha avuto variazioni di prezzo significative nelle ultime 24 ore."
                
                    # Display recommendation
                    self.recommendation_label.setText(recommendation)

                    # save settings
                    settings = QSettings("CryptoNotifier", "CryptoNotifier")
                    settings.setValue("currency_symbol", currency_symbol)

                else:
                    # display error message
                    QMessageBox.critical(self, "Errore", "Impossibile recuperare i dati dei prezzi")
            
        else:
            # display error message
            QMessageBox.critical(self, "Errore", "Simbolo valuta non valido")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CryptoNotifier()
    window.show()
    sys.exit(app.exec_())
