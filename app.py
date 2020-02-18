# started 9:30am

from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import Flask, render_template, request, flash
7: 30 so far

app = Flask(__name__)
app.secret_key = "123"


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/convert')
def convert():
    rates = CurrencyRates()
    codes = CurrencyCodes()
    TEST_DICT = rates.get_rates('USD')

    if request.args.get("from").upper() != "" and request.args.get("from").upper() in TEST_DICT:
        user_from = request.args.get("from").upper()
    else:
        flash(
            f"Enter a valid 'FROM' currency; '{request.args.get('from')}' is not a valid currency code.")

    if request.args.get("to").upper() != "" and request.args.get("to").upper() in TEST_DICT:
        user_to = request.args.get("to").upper()
        curr_symbol = codes.get_symbol(user_to)
    else:
        flash(
            f"Enter a valid 'TO' currency; '{request.args.get('to')}' is not a valid currency code.")
    try:
        if (type(float(request.args.get("amount")))) == float:
            user_amount = float(request.args.get("amount"))
            # strip off dollar sign if exists
    except:
        flash("Enter a valid number.")

    try:
        result = f'{curr_symbol} {round(rates.convert(user_from, user_to, user_amount), 2)}'
    except:
        result = "not valid"

    return render_template("convert.html", result=result)

# bug catching for different empty or wrong cases

# {
#     'GBP': 0.7682325796,
#     'HKD': 7.7674203969,
#     'IDR': 13652.496538994,
#     'ILS': 3.4269497,
#     'DKK': 6.8944162437,
#     'INR': 71.3816335948,
#     'CHF': 0.9820950623,
#     'MXN': 18.5734194739,
#     'CZK': 22.882325796,
#     'SGD': 1.3887401938,
#     'THB': 31.1748961698,
#     'HRK': 6.8726349792,
#     'EUR': 0.9229349331,
#     'MYR': 4.144993078,
#     'NOK': 9.2637748039,
#     'CNY': 6.9815413013,
#     'BGN': 1.8050761421,
#     'PHP': 50.564836179,
#     'PLN': 3.9335486848,
#     'ZAR': 14.9603137979,
#     'CAD': 1.3229349331,
#     'ISK': 127.0881402861,
#     'BRL': 4.3137055838,
#     'RON': 4.4086755884,
#     'NZD': 1.5564374712,
#     'TRY': 6.0491001384,
#     'JPY': 109.875403784,
#     'RUB': 63.4567604984,
#     'KRW': 1183.848638671,
#     'USD': 1.0,
#     'AUD': 1.4886017536,
#     'HUF': 308.8509460083,
#     'SEK': 9.7206275958
# }
