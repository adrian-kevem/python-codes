from operator import truediv


saldo = 1000
saque = float(input("Digite o valor a ser sacado: "))
limite_saque = 200
conta_especial = True

if (((saque <= saldo) and (saque <= limite_saque)) or (conta_especial == True)):
    print("Saque concedido!")
else:
    print("Saque negado!")
