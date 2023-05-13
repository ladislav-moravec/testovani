class Calculator:

    def to_the_power_of(self, a, b):
        return a ** b

    def add(self, a, b):
        return a + b

    def reduce(self, a, b):
        return a - b

    """
    def div(self, a, b):

        try:
            if b == 0:
                print("You can't devide by zero")
            else:
                return a / b
    """

    def div(self, a, b):

        if b == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return a / b


