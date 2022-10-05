
idade = int(input("Digite sua idade: "))
acompanhado = int(input("Digite '1' para acompanhado e '2' para não acompanhado: "))

if (idade >= 18):
    print("Você pode entrar!") 
elif ((idade >= 16) and (acompanhado == 1)):
    print("Você pode entrar!")
else:
    print("Você não pode entrar!")