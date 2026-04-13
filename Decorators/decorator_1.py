def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("******************************************************")
        func()
        print("After execution")
    return wrapper

@my_decorator
def greet():
    print("Hello, there")

greet()