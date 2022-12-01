class area:
    def __init__(self):
        self.cor = ""
        self.base = 0 
        self.altura = 0

    def calcula(b, a):
        return b * a        



quadrado = area

quadrado.base = 6
quadrado.altura = 3
quadrado.cor = "amarelo"

print(quadrado.calcula(quadrado.base , quadrado.altura))
print(quadrado.cor)
