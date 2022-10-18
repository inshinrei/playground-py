def apply_discount(price, discount):
    price_with_discount = int(price * (1.0 - discount))
    assert 0 <= price_with_discount <= price
    return price_with_discount


if __name__ == '__main__':
    print(apply_discount(149, 0.25))
    print(apply_discount(149, 2.0))
