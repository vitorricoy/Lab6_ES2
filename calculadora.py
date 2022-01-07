class CalculadoraException(Exception):
    pass


class Calculadora:
    def adicionar(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return a + b

    def subtrair(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return a - b

    def multiplicar(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return a * b

    def dividir(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        """if b == 0:
            raise CalculadoraException("Divisão por zero!")"""
        return a / b

    def elevar(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return a ** b

    def resolverEquacaoSegundoGrau(self, a, b, c):
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        delta = b * b - 4 * a * c
        if delta < 0:
            raise CalculadoraException("Delta negativo")
        x1 = (-b + (delta) ** (0.5)) / (2 * a)
        x2 = (-b - (delta) ** (0.5)) / (2 * a)
        return x1, x2

    def resolverEquacaoPrimeiroGrau(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return -b / a
