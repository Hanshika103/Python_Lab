def deco(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
    return wrapper

class Demo:
    @deco
    def show(self):
        print("Inside class method")

obj = Demo()
obj.show()
