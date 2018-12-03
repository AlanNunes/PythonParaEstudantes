class Calculadora:
    def add(self, x, y):
        return x + y
    def mpy(self, x, y):
        return x * y
    def sub(self, x, y):
        return x - y

class CalculadoraCientifica(Calculadora):
    def fib(self, x):
        y = 1
        z = 1
        lst = [1]
        for i in range(x):
            a = z
            z = y + z
            y = a
            lst.append(z)
        return lst
calc = CalculadoraCientifica()
print(calc.mpy(7, 7))
print(calc.fib(4))
