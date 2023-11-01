def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: int | float,
                  tax_rate: int | float,
                  *,
                  discount: int | float = 0,
                  round_digits: int = 2
                  ) -> float:
    for arg in (price, tax_rate, discount, round_digits):
        if not isinstance(arg, (int, float)):
            raise TypeError('Аргументы должны быть типа int или float.')

    if price <= 0:
        raise ValueError('Неверная цена')

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    new_price = price + price * tax_rate / 100
    discounted_price = new_price - new_price * discount / 100
    return round(discounted_price, round_digits)
