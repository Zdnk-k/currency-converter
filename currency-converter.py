import requests
import json
import argparse
import sys

# list of available countries
AVAILABLE_CURRENCIES = ["EUR", "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK",\
                        "GBP", "HKD","HRK", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", \
                        "MXN", "MYR", "NOK", "NZD", "PHP", "PLN", "RON", "RUB", "SEK", \
                        "SGD", "THB", "TRY", "USD", "ZAR"
                        ]

# dictionary of symbols
CURRENCY_SYMBOLS = {"EUR":"€", "AUD":"A$", "BGN":"лв", "BRL":"R$", "CAD":"C$", "CHF":"Fr.",\
                    "CNY":"¥", "CZK":"Kč", "GBP":"£", "HKD":"HK$", "HRK":"kn", "HUF":"Ft", \
                    "IDR":"Rp", "ILS":"₪", "INR":"₹", "KRW":"₩", "MXN":"Mex$", "MYR":"RM", \
                    "NOK":"kr", "NZD":"NZ$", "PHP":"₱", "PLN":"zł", "RON":"L", "RUB":"₽", \
                    "SGD":"S$", "THB":"฿", "TRY":"₺", "USD":"$", "ZAR":"R"
                    }

# prepared output format
OUTPUT_DICT = {
                'input':{
                    'amount': 0,
                    'currency': ''
                },
                'output':{

                }
            }


def is_available_code(code):
    """Checks if given currency code is available"""
    return code in AVAILABLE_CURRENCIES


def is_available_symbol(symbol):
    """check if given symbol is available"""
    return symbol in CURRENCY_SYMBOLS.values()


def retrieve_symb_code(symbol):
    """retrieves symbols country code"""
    for c, s in CURRENCY_SYMBOLS.items():
        if symbol == s:
            return c


def currency_type(string):
    """represents currency type for correct input check.
        if passed argumunet is a available symbol, replaces it by code
    """
    if is_available_code(string):   # if is available code return it
       return string
    else:
        if is_available_symbol(string):  # if is in available symbols return symbols code
           return retrieve_symb_code(string)
        else:                   
           raise argparse.ArgumentTypeError("Unknown currency code/symbol") # unknown symbol/code raise error


def convert(amount, in_curr, out_curr):
    """converts given amount of money 
        from input currency to output currency
    """
    if in_curr == out_curr:  # if input == output
        OUTPUT_DICT['output'][in_curr] = format(amount, '.2f')
    else:
        rates = get_rates(in_curr, out_curr)
        for curr, rate in rates.items():
            OUTPUT_DICT['output'][curr] = format(amount * float(rate), '.2f')


def get_rates(in_curr, out_curr):
    """ Rretrieve conversion rates for given input and output currency"""
    try:
        if out_curr == None:    # if no output argument
            r = requests.get("http://api.fixer.io/latest?base={}".format(in_curr))  # retireve for all 
        else:   # retrieve only for output curency
            r = requests.get("http://api.fixer.io/latest?base={}&symbols={}".format(in_curr, out_curr)) 
        r.raise_for_status()
        rates = json.loads(r.text)['rates']
        return rates
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit()


def print_output():
    """prints output in json format"""
    print(json.dumps(OUTPUT_DICT, indent=4))


def main():
    # program arguments
    parser = argparse.ArgumentParser()
    # amount argument
    parser.add_argument("--amount", "-a", help="The amount of money to be converted",\
                            type=float, required=True)  
    # input_currency argument
    parser.add_argument("--input_currency", "-i",  help="The currency to convert from", \
                            type=currency_type, required=True)  
    # output currency argument (optional)
    parser.add_argument("--output_currency", "-o", help="The currency to convert to",\
                            type=currency_type, required=False)
    # parse arguments   
    args = parser.parse_args()


    OUTPUT_DICT['input']['amount'] = args.amount    # assign amount value to output
    OUTPUT_DICT['input']['currency'] = args.input_currency  # assign currency code to output
    # convert 
    convert(args.amount, args.input_currency, args.output_currency)
    # print output
    print_output()


if __name__ == "__main__":
    main()







