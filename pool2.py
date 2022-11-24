class Cachorro:
    def __init__(self, nome, cor, latindo):
        print("Inicializando a instância da clase")
        self.nome = nome
        self.cor = cor
        self.latindo = latindo

    def __del__(self):
        print("Removendo a instância da classe")

    def latir(self):
        print("AUAUAU")
    
c1 = Cachorro("Chappie", "Branco", True)
c1.latir()