def testArgument(arg, dict):
    """Tests is argument is present and a valid currency code"""
    if arg.upper() != "" and arg.upper() in dict:
        return True
    return False


def getCurrencySymbol(codes, validCurrency):
    """Gets the currency symbol for a valid currency"""
    return codes.get_symbol(validCurrency)
