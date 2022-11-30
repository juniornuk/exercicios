import os
import time


def calcular(val1, val2, operacao):
    match operacao:
        case 1:
            nome = "soma"
            operacao = "+"
            resultado = val1 + val2

        case 2:
            nome = "subtracao"
            operacao = "-"
            resultado = val1 - val2

        case 3:
            nome = "multiplicacao"
            operacao = "*"
            resultado = val1 * val2

        case 4:
            nome = "divisao"
            operacao = "/"
            resultado = val1 / val2
        
        case 5:
            nome = "potencia"
            operacao = "**"
            resultado = val1 ** val2
        
    return resultado, operacao, nome

opcao = ""
while opcao != "n":
    print("##### Calculadora #####")
    print("Escolha uma opção:")
    print("(1) soma")
    print("(2) subtração")
    print("(3) multiplicação")
    print("(4) divisão")
    print("(5) potencia")
    print("(9) fim")
    print("\n")
    operando = int(input("opção : "))

    if operando == 9:
        print("Fim")
        exit(1)


    val1 = float(input("insira o valor 1 : "))
    val2 = float(input("insira o valor 2 : "))

    resultado, opcao, nome = calcular(val1, val2, operando)
    print(f"valor de {val1} {opcao} {val2} é = {resultado}")

    print("\n")
    opcao = input("Desejafazer outra operacao (s) para sim e (n) para não:")
    if opcao == "n":
        print("Fechando calculadora...")
        time.sleep(3)
        #limpa = lambda: os.system('clear')
        #limpa()
        os.system('clear')
