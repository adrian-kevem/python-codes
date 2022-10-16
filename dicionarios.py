pessoa = {"nome": "Adrian", "idade": 21}

pessoa2 = dict(nome = "Guilherme", idade = 28)

print(pessoa["nome"])
print(pessoa2["nome"])

contatos = {
    "adrianveven@gmail.com": {"nome": "Adrian", "telefone": "988770936"},
    "alexiasms15@gmail.com": {"nome": "Alexia", "telefone": "XXXXXXXXX"}
}

print(contatos["adrianveven@gmail.com"]["nome"])

for chave in contatos:
    print(chave, contatos[chave])

contatos2 = contatos.copy()

contatos2.clear()

print(contatos.get("idade", "valor não encontrado"))

print(contatos.items())

print(contatos.keys())

print(contatos.pop("adrianveven2@gmail.com", "chave não existente"))

contatos.popitem()

print(contatos)

contatos["adrianveven@gmail.com"].setdefault("idade", "21")

print(contatos)

contatos.update({"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "XXXXX-XXXX"}})

print(contatos)

print("guilherme@gmail.com" in contatos)