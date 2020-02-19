# 7:30 so far started at 2pm

from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import Flask, render_template, request, flash, redirect
from utils import testArgument, getCurrencySymbol

app = Flask(__name__)
app.secret_key = "123"
rates = CurrencyRates()
codes = CurrencyCodes()
TEST_DICT = rates.get_rates('USD')


@app.route('/')
def main():
    """Returns HTML for initial page load"""
    return render_template("main.html")


@app.route('/convert')
def convert():
    """"""

    # handles FROM argument

    if testArgument(request.args.get("user_from"), TEST_DICT):
        user_from = request.args.get("user_from").upper()
    else:
        flash(
            f"Enter a valid 'FROM' currency; '{request.args.get('user_from')}' is not a valid currency code.")

    # handles TO argument
    if testArgument(request.args.get("user_to"), TEST_DICT):
        user_to = request.args.get("user_to").upper()
        curr_symbol = codes.get_symbol(user_to)
    else:
        flash(
            f"Enter a valid 'TO' currency; '{request.args.get('user_to')}' is not a valid currency code.")

    # tests and handles number in amount field
    try:
        if (type(float(request.args.get("user_amount")))) == float:
            user_amount = float(request.args.get("user_amount"))
    except:
        flash("Enter a valid number.")

    # ensures some info is displayed to user regardless of error state
    try:
        currency_symbol = getCurrencySymbol(codes, user_to)
        result = f'{currency_symbol} {round(rates.convert(user_from, user_to, user_amount), 2)}'
    except:
        result = "not valid"

    return render_template("convert.html", result=result)
