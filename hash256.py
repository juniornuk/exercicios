import time
from hashlib import sha256

senha_armazenada = sha256(input("Digite uma senha armazenada: ").encode()).hexdigest()
bool = True
while bool == True:
    login = sha256(input("Login: ").encode()).hexdigest()

    print(senha_armazenada)
    print(login)
    if senha_armazenada == login:
        print("Senha confirmada...")
        bool = False
    else:
        print("Semha errada.")
        print("Tente novamente...")
        time.sleep(3)

print("Fim do programa...")