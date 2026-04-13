def show_name(func):
    def wrapper():
        print("Function name:", func.__name__)
        func()
    return wrapper

@show_name
def hello():
    print("Hello!")

hello()
