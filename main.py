def apply_discount(price, discount):
    price_with_discount = int(price * (1.0 - discount))
    assert 0 <= price_with_discount <= price
    return price_with_discount


if __name__ == '__main__':
    iterator = ("second text" for _ in range(5))
    for text in iterator:
        print(text)
