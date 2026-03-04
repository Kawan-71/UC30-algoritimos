#construa um programa que leia 2 numeros reais informados pelo usuario. ao fim, o programa deve caucular e imprimir:
    #a. a soma dos dois valores
    #b.

numero1 = float(input("Digite o 1º número"))
numero2 = float(input("Digite o 2º número"))

soma = numero1 + numero2
produto = numero1 * numero2

print("soma: ", soma)
print("produto: ", produto)



numero = int(input("Digite um número: "))

if (numero % 2 == 0):
    resultado = numero ** 2
else:
    resultado = numero ** 3

print("Resultado ", resultado)   


usuario = input("Digite seu user: ")
senha = input("Digite sua senha: ")

if (usuario == "procopio" and senha == "12345") or usuario == "paiva" and senha == "54321":
    print("Seja bem-vindo!")
else:
    print("Usuario e senha não coferem.")


nome = input("Digite seu nome: ")
senhaCorreta = "123456"

tentativa = 3

while tentativa > 0:
    senha = input("Digite sua senha: ")

    if senha == senhaCorreta:
        print("Olá, {nome}! Seja bem-vindo!")
        break
    else:
        tentativa -= 1 

        if tentativa == 2:
            print("Senha errada! Você tem 2 tentativas.")
        elif tentativa == 1:
            print("Senha errada! Você tem 1 tentativa.")
        else: 
            print("Senha bloqueada!")        





