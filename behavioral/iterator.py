def count_to(count):
    """Iterator implementation"""

    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]
    iter = zip(range(count), numbers_in_german)

    for position, number in iter:
        yield number


if __name__ == '__main__':
    for num in count_to(3):
        print(f"{num}")