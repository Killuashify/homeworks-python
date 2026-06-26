def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    current_value = begin
    for _ in range(end):
        yield current_value
        current_value = func(current_value)


if __name__ == "__main__":
    from inspect import isgenerator

    gen = some_gen(2, 4, pow)
    assert isgenerator(gen) == True, 'Test1'
    assert list(gen) == [2, 4, 16, 256], 'Test2'

    print('OK')