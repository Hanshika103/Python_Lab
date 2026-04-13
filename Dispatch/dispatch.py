from functools import singledispatch

# Base function
@singledispatch
def process(data):
    print("Default handler: Unsupported type ->", type(data).__name__)


# ---------------------------
# Different registered types
# ---------------------------

@process.register(int)
def _(data):
    print("Integer handler:", data * 2)

@process.register(float)
def _(data):
    print("Float handler:", data / 2)

@process.register(str)
def _(data):
    print("String handler:", data.upper())

@process.register(list)
def _(data):
    print("List handler:", [x for x in data])

@process.register(tuple)
def _(data):
    print("Tuple handler:", tuple(data))

@process.register(set)
def _(data):
    print("Set handler:", data)

@process.register(dict)
def _(data):
    print("Dictionary handler:", {k: v for k, v in data.items()})

@process.register(bool)
def _(data):
    print("Boolean handler:", not data)


# ---------------------------
# Custom class
# ---------------------------
class Student:
    def __init__(self, name):
        self.name = name

@process.register(Student)
def _(data):
    print("Custom Class handler: Student name ->", data.name)


# ---------------------------
# Testing all types
# ---------------------------
process(10)
process(3.14)
process("hello")
process([1, 2, 3])
process((4, 5, 6))
process({1, 2, 3})
process({"a": 1, "b": 2})
process(True)
process(Student("Mukati"))
process(None)   # default handler
