import os
import random

def menu(p1, c1):
    os.system("clear")
    print("============================================")
    print("Bem vindo ao jogo de Pedra, Papel ou Tesoura")
    print("============================================")
    print("")
    print("PLACAR")
    print(f"Você: {p1}")
    print(f"Computador: {c1}")
    print("")

    if p1 > c1:
        print("Você eatá ganhando...")
    elif p1 < c1:
        print("Computador está ganhando...")
    elif p1 == c1:
        print("Empate tecnico...") 

    print("")
    print("")
    print("Escolha seu lance:")
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")
    opcao = int(input())

    return(opcao)

def jogada(jh, jc):
    ppt = ["Papel", "Pedra", "Tesoura"]
    print(f"Humano {ppt[jh]} X {ppt[jc]} Computador ")

p = 0
c = 0


jogar = 0
while jogar in [0]:
    eh = menu(p, c)
    ec = random.randint(0, 2)

    jogada(eh, ec)
    if eh == ec:
        print("Empate...")
        pass 
    elif (eh == 0 and ec == 1) or (eh == 1 and ec == 2) or (eh == 2 and ec == 0):
        print("Você ganhou...")
        p += 1
        pass
    elif (eh == 1 and ec == 0) or (eh == 2 and ec == 1) or (eh == 0 and ec == 2):
        print("Computador ganhou...")
        c += 1
        pass

    print("Deseja jogar novamente:")
    print("0 - Sim | 1 - Não")
    jogar = int(input())

    if jogar == 1:    
        break
            