class academia():
    def __init__(self):
        self.halteres = [(x) for x in range(10, 32) if x % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()



    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [ i for i in self.porta_halteres.values() if i != 0]
        

    def pegar_halteres(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(14)
        key_halter = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halter] = 0
        return (peso)

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcula_caos(self):
        num_caos =  [i for i, j in self.porta_halteres.items() if 1!= j]




teste = academia()

print(teste.listar_halteres())