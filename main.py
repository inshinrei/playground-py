def apply_discount(price, discount):
    price_with_discount = int(price * (1.0 - discount))
    assert 0 <= price_with_discount <= price
    return price_with_discount


if __name__ == '__main__':
    def repeater(text, repeats):
        for _ in range(repeats):
            yield text


    for text in repeater('text', 5):
        print(text)