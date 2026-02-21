# Par ou Ímpar
def par_impar():

    print("Verficador de números pares o impares")
    print(" " * 25)

    numero = int(input("Digite o número: "))

    if numero % 2 == 0:
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é ÍMPAR!")

# Maior Número
def maior_numero():

    print("Indica qual número é maior")
    print(" " * 25)

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    if num1 > num2:
        print(f"O número {num1} é maior!")
    elif num1 < num2:
        print(f"O número {num2} é maior!")
    else:
        print("Os dois números são iguais!")

# Calculadora Simples
def calculadora_simples():

    print(" " * 25)
    print("Calculadora simples")
    print(" " * 25)

    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisao")
    print("5- Sair")

    op = int(input("Digite a operação de dejera realizar: "))

    if op == 5:
        print("Encerrando programa...")

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    if op == 1:
        print("Resultado: ", num1 + num2)
    elif op == 2:
        print("Resultado: ", num1 - num2)
    elif op == 3:
        print("Resultado: ", num1 * num2)
    elif op == 4:
        if num1 or num2 == 0:
            print("ERRO... não podemos realizar a divisão por 0")
        elif num1 / num2:
            print("Resultado: ", num1 / num2)

# Contador
def contador():

    print(" " * 25)
    print("Contador de números")
    print(" " * 25)

    while True:
        print("Deseja listar de quantos números?")
        qntd_num1 = int(input("De: "))
        qntd_num2 = int(input("Até : "))


        print("1- Listar somente números pares")
        print("2- Listar somente números impar")
        print("3- Listar todos\n")

        opcao = int(input("Digite a opcao: "))
        if opcao > 3 or opcao < 1:
            print("Escolha uma opcao valida!\n")
            continue
        elif opcao == 1:
            for i in range(qntd_num1, qntd_num2):
                if i % 2 == 0:
                    print(i)
        elif opcao == 2:
            for i in range(qntd_num1, qntd_num2):
                if i % 2 == 1:
                    print(i)
        else:
            for i in range(qntd_num1, qntd_num2):
                print(i)
        break

# Tabuada
def tabuada():

    print("Tabuada")
    print(" " * 25)

    num_tab = int(input("Digite um número para ver a tabuada: "))

    for i in range(1, 11):
        resultado = num_tab * i
        print(f"{num_tab} x {i} = {resultado}")

# Função de Média
def media():

    print(" " * 25)
    print("Calculadora simples")
    print(" " * 25)
    print("Bem vindo ao programa que calcula sua média")

    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    print("Sua media é: ",media)

# MENU
def menu():

    print(" " * 25)
    print("1- Verficador de números pares o impares.")
    print("2- Indica qual número é maior")
    print("3- Calculadora simples")
    print("4- Contador")
    print("5- Tabuada")
    print("6- Media")
    print("7- Sair")
    print(" " * 25)

    opcao = int(input("Digite a opção: "))

    if opcao == 7:
        print("Encerrando programa...")

    if opcao == 1:
        return par_impar()
    elif opcao == 2:
        return maior_numero()
    elif opcao == 3:
        return calculadora_simples()
    elif opcao == 4:
        return contador()
    elif opcao == 5:
        return tabuada()
    elif opcao == 6:
        return media()

menu()