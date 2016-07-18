class DifferentCurrencyCodeError(Exception):
    pass

class Currency:

    def __init__(self, amount = None, currency_code):
        if amount:
            self.amount = amount
            self.currency_code = currency_code
        else:
            self.amount = amount(float)


    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    def __add__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError()
        else:
            return Currency(self.amount + other.amount, self.currency_code)

    def __sub__(self, other):
        return Currency(self.amount - other.amount, self.currency_code)

    def __mul__(self, other):
        return Currency(self.amount * other.amount, self.currency_code)

    def __init__(self, currency_code, amount = None):
        if amount:
            self.amount = amount
            self.currency_code = currency_code
        else:
            self.amount = amount(float)

    currency_dictionary = {'USD':'$','ZAR':'R','EUR':'€','GBP':'£'}
