peça = input("Digite a peça desejada: ")
peça_estoque = ["peça1", "peça2", "peça3", "peça4"]
if (peça in peça_estoque):
    print("Peça em estoque!")
else:
    print("Peça fora de estoque!")