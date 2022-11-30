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
        
        case _:
            print("Fim")
            exit(1)

    return resultado, operacao, nome


print("##### Calculadora #####")
print("Escolha uma opção:")
print("(1) soma")
print("(2) subtração")
print("(3) miltiplicação")
print("(4) divisão")
print("(5) potencia")
print("(9) fim")
print("\n")
operando = int(input("opção : "))

val1 = float(input("insira o valor 1 : "))
val2 = float(input("insira o valor 2 : "))

resultado, opcao, nome = calcular(val1, val2, operando)
print(f"{nome} de {val1} {opcao} {val2} é = {resultado}")
