import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'trace: call {func.__name__}() with {args}, {kwargs}')
        func_result = func(*args, **kwargs)
        print(f'trace: {func.__name__}() resulted with {func_result!r}')

        return func_result

    return wrapper
