print((set([1, 2, 2, 3, 3, 3, 4])))
print(set("abacaxi"))
print(set(("palio", "gol", "celta", "palio",)))

linguagens = {1, 2, 3, 3, 4, 4, 4, 5}
print(linguagens)
linguagens = set(linguagens)
print(linguagens)
linguagens = list({1, 2, 3, 3, 4, 4, 4, 5})
print(linguagens[0])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4}
print(conjunto1.union(conjunto2))

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4}
print(conjunto1.intersection(conjunto2))

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4}
print(conjunto1.difference(conjunto2))

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4}
print(conjunto1.symmetric_difference(conjunto2))

conjunto1 = {1, 2, 3}
conjunto2 = {3}
print(conjunto2.issubset(conjunto1))

conjunto1 = {1, 2, 3}
conjunto2 = {3}
print(conjunto2.issuperset(conjunto1))

conjunto1 = {1, 2, 3}
conjunto2 = {4}
print(conjunto2.isdisjoint(conjunto1))

conjunto2 = {4}
conjunto2.add(5)
print(conjunto2)
conjunto2.discard(4)
print(conjunto2)
conjunto3 = conjunto2.copy()
print(conjunto3)

numeros = {1, 2, 3, 4, 5}
numeros.pop()
print(numeros)