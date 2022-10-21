cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**(1/2)

print("A hipotenusa é: {0}".format(hipotenusa))