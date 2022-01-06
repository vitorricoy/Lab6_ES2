from calculadora import Calculadora

calculadora = Calculadora()
while True:
    print("1- Adicionar")
    print("2- Subtrair")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Elevar")
    print("6- Equação de Segundo Grau (ax² + bx + c = 0)")
    print("7- Equação de Primeiro Grau (ax + b = 0)")
    print("8- Sair")
    print("Digite a opção desejada: ", end="")
    opcao = int(input())
    if opcao == 1:
        print("Digite o primeiro valor: ", end="")
        valor1 = input()
        print("Digite o segundo valor: ", end="")
        valor2 = input()
        print("Resultado =", str(calculadora.adicionar(valor1, valor2)))
    elif opcao == 2:
        print("Digite o primeiro valor: ", end="")
        valor1 = input()
        print("Digite o segundo valor: ", end="")
        valor2 = input()
        print("Resultado =", str(calculadora.subtrair(valor1, valor2)))
    elif opcao == 3:
        print("Digite o primeiro valor: ", end="")
        valor1 = input()
        print("Digite o segundo valor: ", end="")
        valor2 = input()
        print("Resultado =", str(calculadora.multiplicar(valor1, valor2)))
    elif opcao == 4:
        print("Digite o primeiro valor: ", end="")
        valor1 = input()
        print("Digite o segundo valor: ", end="")
        valor2 = input()
        print("Resultado =", str(calculadora.dividir(valor1, valor2)))
    elif opcao == 5:
        print("Digite o primeiro valor: ", end="")
        valor1 = input()
        print("Digite o segundo valor: ", end="")
        valor2 = input()
        print("Resultado =", str(calculadora.elevar(valor1, valor2)))
    elif opcao == 6:
        print("Digite o valor de a: ", end="")
        a = input()
        print("Digite o valor de b: ", end="")
        b = input()
        print("Digite o valor de c: ", end="")
        c = input()
        print("Resultado =", str(calculadora.resolverEquacaoSegundoGrau(a, b, c)))
    elif opcao == 7:
        print("Digite o valor de a: ", end="")
        a = input()
        print("Digite o valor de b: ", end="")
        b = input()
        print("Resultado =", str(calculadora.resolverEquacaoPrimeiroGrau(a, b)))
    else:
        break
