# currency-converter
Currency-converter written in Python 3. Uses data from http://fixer.io.

## Parameters
- --amount - amount of money which we want to convert <float>
- --input_currency - input currency - 3 letters name or currency symbol
- --output_currency - requested/output currency - 3 letters name or currency symbol (optional)

If `--output_currency` is missing, input_currency is converted to all available currencies

## available currencies
32 currencies are supported.

AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, GBP, HKD, HRK, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PLN, RON, RUB, SEK, SGD, THB, TRY, USD, ZAR

### currency symbols
Since some currencies use the same symbol, not all available currencies are accessible by their symbol.
$ symbol is used for USD, $C for CAD, $A for AUD etc. kr is used only for NOK, ¥ only for CNY.

#### available currency symbols
€, A$, лв, R$, C$, Fr., ¥, Kč, £, HK$, kn, Ft, Rp, ₪, ₹, ₩, Mex$, RM, kr, NZ$, ₱, zł, L,₽, S$, ฿, ₺, $, R