from functools import wraps


def additional(*args) -> callable:
    def decorator_add(func: callable):
        @wraps(func)
        def wrapper() -> None:
            print(f"decorator is working.", *args)
            print(f"Func Name: {func.__name__} has started")
            print(f"Documentation: {func.__doc__}")
            func()
            print(f"Func Name: {func.__name__} has ended")
            print(f"decorator end work.", *args)
        return wrapper
    return decorator_add


@additional("Anna", "Kirill", 15, True)
def hello() -> None:
    """
    Docstring for hello
    """
    print("Hellooooooo")
    num = 100


print(hello.__name__)
print(hello.__doc__)

print()
hello()