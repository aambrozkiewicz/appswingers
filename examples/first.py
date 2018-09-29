import random


def get_random_phone_number(length, prefix=None):
    if prefix is None:
        prefix = ''

    numbers = []
    for i in range(length):
        numbers.append(
            random.randint(0, 9)
        )
    phone_number = ''.join((str(n) for n in numbers))
    return f'{prefix}{phone_number}'


if __name__ == '__main__':
    print(
        get_random_phone_number(5, prefix='+48-')
    )
