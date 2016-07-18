Class CurrencyClassCon():


currency_dictionary = {'USD':'$','ZAR':'R','EUR':'€','GBP':'£'}

    def __init__(self, amount = None, currency_code):
        if amount:
            self.amount = amount
            self.currency_code = currency_code
