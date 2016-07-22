from currency import Currency

class UnknownCurrencyCodeError(Exception):
    pass

class CurrencyClassCon:
    def __init__(self, rates):
        self.rates = rates

#At first, just make this work with two currency codes and conversation rates, with one rate being 1.0 and the other being the conversation rate. An example would be this: {'USD': 1.0, 'EUR': 0.74}, which implies that a dollar is worth 0.74 euros.
    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    def convert(self, currency, to_code):
        if currency_code == to_code:
            return currency
        else:
            if to_code in self.rates:
                converstion_rates == self.rate[to_code]
                amount = currency_rates * currency_amount
                return Currency(amount, to_code)
            else:
                raise UnknownCurrencyCodeError



#Must be able to take a Currency object and a requested currency code that is the same currency code
#as the Currency object's and return a Currency object equal to the one passed in.
#That is, currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD').

#    def currency_converter(self, other):
#        pass
        #key = input("What currency do you wish to test")

    #def currencyconverter(self, other):

#    def___(self,amount, currency_code):
