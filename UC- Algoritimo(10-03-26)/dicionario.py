#sem dicionario
matricula1 = 2026001
nome1 = "kawan gayo"
telefone1 = "0000-7171"

#com dicionário
aluno = {
    "matricula": 2026001,
    "nome": "Kawan gayo",
    "telefone": "0000-7171"

}

print(aluno)

contato = {
    "@camilaqueiroz": "Camila Queiroz",
    "@Brunamarquezine": "Bruna M.",
    "@sheronmenezes": "Sheron M.",
    "@paolaoliveira": "Paola O."

}

print(contato)
print(type(contato))

# Acesso direto
print(contato["@camilaqueiroz"])

# Acesso seguro com get()
print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))

#add novo elemento
contato["@giovanna"] = "Giovanna"
print("Após add: ", contato)

#atualiza elemento existente
contato["@paolaoliveira"] = "Paola Oliveira"
print("Após add: ", contato)

contato.update({
    "@brunamarquezine": "Bruna Marquezine",
    "@camilaqueiroz": "Camila Q."
})

print("Após atualização: ", contato)



