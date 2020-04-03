class Example:
    n = 899076

    def __init__(self):
        super().__init__()

    def hello(self):
        print("Hello world")


if __name__ == "__main__":
    c = Example()
    c.hello()
    print(c.n)