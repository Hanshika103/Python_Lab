def my_decorator(func):
    def wrapper(a,b):
        print("Before execution")
        result=func(a,b)
        print("Sum is : ",result)
        print("After function execution")
    return wrapper

@my_decorator
def add(a,b):
    return a+b

add(1,2)
