def entrada(tipo):
    if tipo == "nome":
        return input("Inorme seu nome ")

    if tipo == "idade": 
        return int(input("Informe sua idade: "))

    if tipo == "salario":
        return float(input("Informe seu salario"))

    if tipo == "sexo": 
        return input("Informe seu sexo: ")

    if tipo == "ecivil":
        return input("Informe seu estado civil: ")



