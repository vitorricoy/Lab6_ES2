import unittest
from calculadora import Calculadora, CalculadoraException


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_string_invalida_adicionar(self):
        self.assertRaises(
            CalculadoraException, lambda: self.calculadora.adicionar("a", "1")
        )

    def test_string_valida_adicionar(self):
        self.assertEqual(3.0, self.calculadora.adicionar("2", "1"))

    def test_string_invalida_subtrair(self):
        self.assertRaises(
            CalculadoraException, lambda: self.calculadora.subtrair("a", "1")
        )

    def test_string_valida_subtrair(self):
        self.assertEqual(1.0, self.calculadora.subtrair("2", "1"))

    def test_string_invalida_multiplicar(self):
        self.assertRaises(
            CalculadoraException, lambda: self.calculadora.multiplicar("-", "1")
        )

    def test_string_valida_multiplicar(self):
        self.assertEqual(-2.0, self.calculadora.multiplicar("2", "-1"))

    def test_string_invalida_dividir(self):
        self.assertRaises(
            CalculadoraException, lambda: self.calculadora.dividir("1", "b")
        )

    def test_string_valida_dividir(self):
        self.assertEqual(2.0, self.calculadora.dividir("2", "1"))

    def test_string_invalida_elevar(self):
        self.assertRaises(
            CalculadoraException, lambda: self.calculadora.elevar("h", "b")
        )

    def test_string_valida_elevar(self):
        self.assertEqual(4.0, self.calculadora.elevar("2", "2"))

    def test_string_invalida_resolver_equacao_segundo_grau(self):
        self.assertRaises(
            CalculadoraException,
            lambda: self.calculadora.resolverEquacaoSegundoGrau("a", "b", "c"),
        )

    def test_string_valida_resolver_equacao_segundo_grau(self):
        self.assertEqual(
            (0.0, 0.0), self.calculadora.resolverEquacaoSegundoGrau("1", "0", "0")
        )

    def test_string_invalida_resolver_equacao_primeiro_grau(self):
        self.assertRaises(
            CalculadoraException,
            lambda: self.calculadora.resolverEquacaoPrimeiroGrau("a", "b"),
        )

    def test_string_valida_resolver_equacao_primeiro_grau(self):
        self.assertEqual(0.0, self.calculadora.resolverEquacaoPrimeiroGrau("1", "0"))

    def test_soma_positivos(self):
        self.assertEqual(25, self.calculadora.adicionar(10, 15))

    def test_soma_negativos(self):
        self.assertEqual(-25, self.calculadora.adicionar(-10, -15))

    def test_soma_positivo_negativo(self):
        self.assertEqual(-5, self.calculadora.adicionar(10, -15))

    def test_subtracao_positivos(self):
        self.assertEqual(-5, self.calculadora.subtrair(10, 15))

    def test_subtracao_negativos(self):
        self.assertEqual(5, self.calculadora.subtrair(-10, -15))

    def test_subtracao_positivo_negativo(self):
        self.assertEqual(25, self.calculadora.subtrair(10, -15))

    def test_multiplicacao_positivos(self):
        self.assertEqual(150, self.calculadora.multiplicar(10, 15))

    def test_multiplicacao_negativos(self):
        self.assertEqual(150, self.calculadora.multiplicar(-10, -15))

    def test_multiplicacao_positivo_negativo(self):
        self.assertEqual(-150, self.calculadora.multiplicar(10, -15))

    def test_divisao_positivos(self):
        self.assertEqual(0.5, self.calculadora.dividir(10, 20))

    def test_divisao_negativos(self):
        self.assertEqual(0.5, self.calculadora.dividir(-10, -20))

    def test_divisao_zero(self):
        self.assertRaises(CalculadoraException, lambda: self.calculadora.dividir(10, 0))

    def test_divisao_positivo_negativo(self):
        self.assertEqual(-0.5, self.calculadora.dividir(10, -20))

    def test_exponenciacao_positivos(self):
        self.assertEqual(144, self.calculadora.elevar(12, 2))

    def test_exponenciacao_negativos(self):
        self.assertEqual(1.0 / 144.0, self.calculadora.elevar(12, -2))

    def test_exponenciacao_positivo_negativo(self):
        self.assertEqual(1.0 / 144.0, self.calculadora.elevar(-12, -2))

    def test_equacao_primeiro_grau_positivos(self):
        self.assertEqual(-5.0, self.calculadora.resolverEquacaoPrimeiroGrau(2, 10))

    def test_equacao_primeiro_grau_negativos(self):
        self.assertEqual(-4.0, self.calculadora.resolverEquacaoPrimeiroGrau(-4, -16))

    def test_equacao_primeiro_grau_positivo_negativo(self):
        self.assertEqual(5.0, self.calculadora.resolverEquacaoPrimeiroGrau(2, -10))

    def test_equacao_segundo_grau_delta_positivo(self):
        self.assertEqual((0, -2), self.calculadora.resolverEquacaoSegundoGrau(1, 2, 0))

    def test_equacao_segundo_grau_delta_negativo(self):
        self.assertRaises(
            CalculadoraException,
            lambda: self.calculadora.resolverEquacaoSegundoGrau(1, 1, 1),
        )

    def test_equacao_segundo_grau_delta_zero(self):
        self.assertEqual((0, 0), self.calculadora.resolverEquacaoSegundoGrau(1, 0, 0))


if __name__ == "__main__":
    unittest.main()
