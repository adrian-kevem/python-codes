class Bicicleta:
    def __init__(self, modelo, cor, ano, valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("buzinando")

    def correr(self):
        print("correndo")
   
    def parar(self):
        print("parando")

    def get_cor(self):
        return self.cor

    def __str__(self):
        return f"Bicicleta: modelo={self.modelo}, cor={self.cor}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.itens()])}"
    
modelo = input("Informa o modelo da bicicleta: ")
cor = input("Informe a cor da bicicleta: ")
ano = int(input("Informa o ano da bicicleta: "))
valor = int(input("Informa o valor da bicicleta: "))

bicicleta_01 = Bicicleta(modelo, cor, ano, valor)

bicicleta_01.parar()

print(bicicleta_01.cor)

print(bicicleta_01.get_cor())

print(bicicleta_01)