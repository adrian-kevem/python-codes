nome = "guilherme"
idade = 18

print(nome.upper())
print(nome.capitalize())
print(nome.lower())
print(nome.center(11, "#"))
print("-".join(nome))
print("-".center(40, "-"))
print("Olá meu nome é %s, tenho %d anos e trabalho com Python" % (nome, idade))

print("Olá meu nome é {0}, tenho {1} anos e trabalho com Python".format(nome, idade))

print("Olá meu nome é {name}, tenho {age} anos e trabalho com Python".format(name=nome, age=idade))

print("-".center(40, "-"))

pi = 3.14159
print(f"O valor de PI é: {pi: 10.2f}")

print("-".center(40, "-"))

nome_completo = "Adrian Kevem Gomes Rares"
print(nome_completo[0])
print(nome_completo[0:6])
print(nome_completo[:: -1])

print("-".center(40, "-"))

mensagem = """ Bom dia!
Favor cancelar o pedido.
Atenciosamente, """
print(mensagem)
