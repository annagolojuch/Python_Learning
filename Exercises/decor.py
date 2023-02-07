def decor(func):
    def wrapper():
        print("-------------------------")
        func()
        print("-------------------------")
    return wrapper

def hello():
    print("Hello World")

print("Wywołanie hello:")
hello()

x = decor(hello)

print("\nWywołanie hello z decor:")
x()
