from nose.tools import raises
from currency import Currency, DifferentCurrencyCodeError
#from currencyconverter import CurrencyClassCon

def test_create_currency_with_amount_and_code():
    one_dollar = Currency(1, 'USD')

    assert one_dollar.amount == 1
    assert one_dollar.currency_code == 'USD'

def test_create_US_currency_and_value():
    one_dollar = Currency('$1.20')

    assert one_dollar_twenty.amount == 1.2
    assert one_dollar.currency_code == 'USD'

def test_create_Euro_currency_and_value():
    one_euro = Currency('€7.00')
    #one_dollar = Currency('€7.00')

    assert seven_euro.amount == 7.0
    assert one_euro.currency_code == 'EUR'
    #assert one_euro.currency_code == 'EUR'

def test_currencys_can_be_equal():
    curr1 = Currency(99, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 == curr2

def test_currencys_with_different_amounts_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 != curr2

def test_currencys_with_different_currency_codes_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')

    assert curr1 != curr2

def test_currency_adding_with_same_code():
    addsamecode = Currency(1, 'USD') + Currency(1, 'USD')
    assert addsamecode == Currency(2, 'USD')

def test_currency_subtracting_with_same_code():
    subsamecode = Currency(8, 'USD') - Currency(4, 'USD')
    assert subsamecode == Currency(4, 'USD')

def test_currency_multipying_with_same_code():
    mulsamecode = Currency(8, 'USD') * Currency(2, 'USD')
    assert mulsamecode == Currency(16, 'USD')

@raises(DifferentCurrencyCodeError)
def test_currency_adding_with_different():
    Currency(1, 'EUR') + Currency(1, 'USD')

def test_currencyconverter_with_two_codes_and_rates():
    curr1 = Currency(1.0, 'USD')
    curr2 = Currency(.74, 'EUR')

    assert curr1 != curr2
