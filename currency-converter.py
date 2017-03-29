import requests
import json
import argparse
import sys
from forex_python import CurrencyCodes, CurrencyConverter


AVAILABLE_CURRENCIES = ["EUR", "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "GBP",                             "HKD","HRK", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR",                              "NOK", "NZD", "PHP", "PLN", "RON", "RUB", "SEK", "SGD", "THB", "TRY",                             "USD", "ZAR"
                        ]
CURRENCY_SYMBOLS = { 
"€":"EUR",
"A$":"AUD",
"лв":"BGN", 
 "R$":"BRL", 
 "C$":"CAD", 
 "Fr.":"CHF", 
 "\u00a5":"CNY", 
 "K\u010d":"CZK", 
 "\u00a3":"GBP",                          
 "HK$":"HKD",
 "kn":"HRK", 
 "Ft":"HUF", 
 "Rp":"IDR", 
 "\u20aa":"ILS", 
 "\u20b9":"INR", 
 "\u20a9":KRW", 
 "Mex$":"MXN", 
 "RM":"MYR",                              
 "kr":"NOK", 
 "NZ$":"NZD", 
 "\u20b1":"PHP", 
 "z\u0142":"PLN", 
 "L":RON",
 "\u20bd":"RUB", 
 "S$":"SGD", 
 "\u0e3f":"THB", 
 "\u20ba":"TRY",                          
 "$":"USD", 
 "R":"ZAR"
}

OUTPUT_DIR = {
                'input':{
                    'amount': , 
                    'currency': 
                },
                'output':{

                }
            }



def is_available_currency(code):
    """Checks if given currency code is available"""
    return code in AVAILABLE_CURRENCIES


def currency_type(string):
    if not is_available_symbol(string):
        if is_available_code(string):
            return string
        elif     
    else:



def convert(amount, input, output):
    pass


def main():
    # program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--amount", "-a", help="The amount of money to be converted",  type=float)  # amount argument
    parser.add_argument("--input_currency", "-i",  help="The currency to convert from", type=currency_type)  # input_currency argument
    parser.add_argument("--output_currency", "-o", help="The currency to convert to", type=currency_type, required=False)   # output currency argument (optional)
    args = parser.parse_args()







if __name__ == "__main__":
    main()