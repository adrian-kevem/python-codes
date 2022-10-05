opcao = -1
saldo = 1000
limite_saque = 200

print("-------------------")
print("|    BEM VINDO    |")
print("-------------------")

while (opcao != 0):
    print("OPÇÕES")
    print("0 - SAIR")
    print("1 - EXTRATO")
    print("2 - SAQUE")
    opcao = int(input("Escolha uma opção: "))
    if(opcao == 0):
        print("Obrigado por ser nosso cliente! Tenha um bom dia!")
    elif (opcao == 1):
        print(f"Seu saldo é de: {saldo} R$")
    elif (opcao == 2):
        saque = float(input("Digite o valor a ser sacado: "))
        if ((saque <= saldo) and (saque <= limite_saque)):
            print("Saque concedido!")
        else:
            print("Saque negado!")
    else:
        print("Opção inválida!")
    print()