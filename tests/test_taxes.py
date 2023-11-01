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


@pytest.mark.parametrize("discount, expected", [(0, 110),
                                                (10, 99),
                                                (100, 0)
                                                ])
def test_calculate_tax_with_discount(discount, expected):
    assert calculate_tax(100, 10, discount=discount) == expected


def test_calculate_tax_no_discount():
    assert calculate_tax(100, 10) == 110.0


@pytest.mark.parametrize("round_digits, expected", [(0, 99),
                                                    (1, 99.4),
                                                    (2, 99.42),
                                                    (3, 99.425)
                                                    ])
def test_calculate_tax_round_digits(round_digits, expected):
    assert calculate_tax(100, 2.5, discount=3, round_digits=round_digits) == expected


def test_calculate_tax_no_round_digits():
    assert calculate_tax(100, 2.5, discount=3) == 99.42


@pytest.mark.parametrize("price, tax_rate, discount, round_digits", [("100", 2.5, 3, 1),
                                                                               (100, "2.5", 3, 1),
                                                                               (100, 2.5, "3", 1),
                                                                               (100, 2.5, 3, "1")
                                                                               ])
def test_calculate_tax_check_int_or_float(price, tax_rate, discount, round_digits):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, round_digits=round_digits)


def test_calculate_tax_only_kwargs():
    with pytest.raises(TypeError):
        calculate_tax(100, 10, 5, 2)
