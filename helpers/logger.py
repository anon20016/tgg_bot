def logger(func):
    def wrap(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrap


def log_warning(message):
    print(f"Warning. {message}")


def log_error(message):
    print(f"Error. {message}")
    raise Exception(message)
