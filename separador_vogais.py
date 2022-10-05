palavra = input("Digite uma palavra: ")
vogais = "AEIOU"

for letra in palavra:
    if (letra.upper() in vogais):
        print(letra)
