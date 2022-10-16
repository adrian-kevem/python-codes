frutas = ["banana", "laranja", "maça"]
print(frutas[0])

print("-------------------------------------------")

nome = list("python")
print(nome[0])

print("-------------------------------------------")

numero = list(range(10))
print(numero[9])

print("-------------------------------------------")

infos = [2001, True, "Adrian", 1.75]
print(infos[0])

print("-------------------------------------------")

carros = ["gol", "pálio", "uno"]
for carro in carros:
    print(carro)

print("-------------------------------------------")

carros = ["gol", "pálio", "uno"]
for index, carro in enumerate(carros):
    print(f"{index+1}:{carro}")

print("-------------------------------------------")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = []
for numero in numeros:
    if (numero % 2 == 0):
        par.append(numero)
print(par[::])

print("-------------------------------------------")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = [numero for numero in numeros if (numero % 2 == 0)]
print(par[::])

print("-------------------------------------------")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = [potencia ** 2 for potencia in numeros]
print(quadrado[::])

print("-------------------------------------------")

numeros.clear()
numeros.append(11)
print(numeros[::])

print("-------------------------------------------")

quadrado2 = quadrado.copy()
print(quadrado2[::])

print("-------------------------------------------")

cores = ["vermelho", "verde", "azul", "verde"]
quantidade_verde = cores.count("verde")
print(quantidade_verde)

print("-------------------------------------------")

cores = ["vermelho", "verde", "azul", "verde"]
cores.extend(["laranja", "roxo", "preto"])
print(cores[::])


print("-------------------------------------------")

cores = ["vermelho", "verde", "azul", "verde"]
ocorrencia_azul = cores.index("azul")
print(ocorrencia_azul)


print("-------------------------------------------")

numeros = [9, 8, 7, 6, 5]
numeros.sort()
print(numeros[::])

print("-------------------------------------------")

nome = "Adrian"
tamanho = len(nome)
print(tamanho)