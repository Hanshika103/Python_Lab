def deco1(func):
    def wrapper():
         print("&&&&&&&&&&&&&&&&&&&&&&&&&& ")
         func()
         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    return wrapper

def deco2(func):
     def wrapper():
          print("******************************")
          func()
          print("#################################")
     return wrapper

@deco2
@deco1
def greet():
     print("Hello,guys")

greet()