import pytest

from src.taxes import calculate_taxes, calculate_tax


@pytest.fixture
def prices():
    return [100, 200, 300]

@pytest.mark.parametrize("tax_rate, expected", [(0, [100.0, 200.0, 300.0]),
                                                (10, [110.0, 220.0, 330.0]),
                                                (15, [115.0, 230.0, 345.0])])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, -1)


def test_calculate_taxes_invalid_price():
    with pytest.raises(ValueError):
        calculate_taxes([-100, 100], 10)


@pytest.mark.parametrize("price, tax_rate, expected", [(100, 10, 110.0),
                                                       (50, 5, 52.5),
                                                       (100, 0, 100.0)
                                                       ])
def test_calculate_tax(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


@pytest.mark.parametrize("price", [-100, 0])
def test_calculate_tax_invalid_price(price):
    with pytest.raises(ValueError):
        calculate_tax(price, 10)


@pytest.mark.parametrize("tax_rate", [-100, 100, 101])
def test_calculate_tax_invalid_price(tax_rate):
    with pytest.raises(ValueError):
        calculate_tax(100, tax_rate)
