class DifferentCurrencyCodeError(Exception):
    pass

class UnsupportedOtherType(Exception):
    pass

class Currency:

    def __init__(self, amount, currency_code = ''):
        if isinstance(amount, (int, float)):
            self.amount = amount
            self.currency_code = currency_code
        elif isinstance(amount, str):
            self.amount = parse_amount(amount)
            self.currency_code = self.parse_currency_code(amount)
        else:
            raise TypeError(amount)
            #self.amount = amount(float)

    def parse_amount(self, amount):
        return float(amount[1:])

    def parse_currency_code(self, amount):
        currency_code = amount[0]
        currency_code_dictionary = {'$':'USD','R':'ZAR','€':'EUR','£':'GBP'}
        return currency_code_dictionary[currency_code]

#Must be created with an amount and a currency code.
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

    # def __init__(self, currency_code, amount = None):
    #     if amount:
    #         self.amount = amount
    #         self.currency_code = currency_code
    #     else:
    #         self.amount = amount(float)
