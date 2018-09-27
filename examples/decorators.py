import functools


def big_header(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'<h1>{result}</h1>'
    return wrapper


@big_header
def get_display_name(name):
    return f'{name}!'


print(get_display_name('Aleks'))


def get_age(age):
    return age - 5


get_display_age = big_header(get_age)

print(get_display_age(30))


# django login decorator
