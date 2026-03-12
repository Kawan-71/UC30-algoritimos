#Sem função
print("Python é fácil")
print("Python é fácil")
print("Python é fácil")

#Com função
def exibirMenssagem():
    print("Olá, mundo!")

exibirMenssagem()

#Função com parâmetro
def saudar(nome):
    print(f"Olá, { nome}!")

saudar("Ana")
saudar("Bruno") 


def exibirMenssagem(nome, menssagem):
    print(f"{menssagem}, {nome}")

exibirMenssagem("Ana", "Bom dia")

#Parâmetros nomeados
exibirMenssagem(nome = "Bruno", menssagem = "Boa noite")

#Função que retorna média
def calcularMedia(nota1, nota2):
    media = (nota1, nota2) / 2
    return media

resultado = calcularMedia(8.0, 9.0)
print(f"Média: {resultado}")

