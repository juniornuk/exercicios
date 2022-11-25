import datetime

#retorno = while_menu.menu()
retorno = 0
#while  retorno != 0:
ano = int(input("Informe seu ano de nascimento: "))

currentDateTime = datetime.datetime.now()
date = datetime.date.today()
print(f"Você têm {date.year - ano} anos")
