nomes = ["Kg", "Wk", "Mt" ]
print(nomes)

dados = ["Carol", 0, 1.70, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

lista = ["Cachorro", "Gato"]
print("Original: ", lista)
lista.append("Coelho")
print("Atualizado: ", lista)

lista.insert(1, "Grilo")
print("Atualizado: ", lista)

lista.extend(["Macaco", "Ovelha"])
print("Lista final", lista)
