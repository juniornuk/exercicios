class animal:
    def __init__(self):
        self.pelagem = "pena"
        self.patas = 2
        self.cor = "branco"

class dog(animal):
    def __init__(self):
        self.faz = "late"        



especie = animal()
cachorro = dog()
print(especie.pelagem)
print(especie.patas)
print(especie.cor)


cachorro.pelagem = "pelo"
cachorro.patas = 4
cachorro.cor = "preto"
print("\n")
print(cachorro.pelagem)
print(cachorro.patas)
print(cachorro.cor)
print(cachorro.faz)