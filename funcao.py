def exibir_mensagem(nome):
    print(f"Seja vem vindo, {nome}!")
nome = "Adrian"
exibir_mensagem(nome)

print("------------------------------------------------------------")

def exibir_mensagem_2(nome_2):
    print(f"Seja vem vindo, {nome_2}!")
exibir_mensagem("ADRIAN")

print("------------------------------------------------------------")

def soma(numeros):
    return sum(numeros)
numeros = [1, 2, 3, 4, 5]
print(soma(numeros))


print("------------------------------------------------------------")

def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor 
numero = 1
print(antecessor_sucessor(numero))

print("------------------------------------------------------------")

def carro(marca, modelo, ano):
    print(f"O carro é um {marca} {modelo} {ano}")
carro(**{"marca": "fiat", "modelo": "uno", "ano": "2011"})

print("------------------------------------------------------------")

def carro(marca, modelo, /, ano):
    print(f"O carro é um {marca} {modelo} {ano}")
print(carro("fiat", "uno", ano = 2011))

print("------------------------------------------------------------")

def carro(*, marca, modelo, ano):
    print(f"O carro é um {marca} {modelo} {ano}")
print(carro(marca = "fiat", modelo = "uno", ano = "2011"))

print("------------------------------------------------------------")

def carro(marca, /, modelo, *, ano):
    print(f"O carro é um {marca} {modelo} {ano}")
print(carro("fiat", "uno", ano = "2011"))

print("------------------------------------------------------------")

def somar(a, b):
    return (a + b)

def exibir_resultado(a, b):
    resultado = somar(a, b)
    print(f"O resultado da operação é: {a} + {b} = {resultado}!")

print(exibir_resultado(a = 2, b = 3))

print("------------------------------------------------------------")

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))

print("------------------------------------------------------------")