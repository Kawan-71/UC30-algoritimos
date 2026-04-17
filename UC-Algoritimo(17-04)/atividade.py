# 1° Questão
print ("Hello, World!")

# 2° Questão
idade = int(input("Digite a idade do aluno: "))

if idade >= 16:
    print("Pode votar!")
else:
    print("Ainda não pode votar.")

# 3° Questão
total = 0.0

while True:
    valor = float(input("Digite o valor do item (0 para encerrar): "))
    
    if valor == 0:
        break
    
    total += valor

print(f"Total da compra: R$ {total:.2f}")

# 4° Questão
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Magro"
    elif imc <= 24.9:
        return f"IMC: {imc:.2f} - Normal"
    elif imc <= 29.9:
        return f"IMC: {imc:.2f} - Acima do peso"
    else:
        return f"IMC: {imc:.2f} - Obeso"

try:
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))
    
    if peso <= 0 or altura <= 0:
        print("Valores devem ser positivos!")
    else:
        resultado = calcular_imc(peso, altura)
        print(resultado)

except ValueError:
    print("Entrada inválida! Digite números válidos.")

    # 5° Questão
amigos = ["Matheus", "wk", "Clara", "Rivia", "Gaby"]

quantidade = len(amigos)

print(f"Quantidade de amigos: {quantidade}")

if quantidade % 2 == 0:
    print("O número de amigos é par.")
else:
    print("O número de amigos é ímpar.")

# 6° Questão
temperaturas = []

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

soma = 0
for t in temperaturas:
    soma += t

media = soma / len(temperaturas)

print(f"Média das temperaturas: {media:.2f}°C")

# 7° Questão
vendas = [10, 15, 22, 7, 30, 9, 18]

soma = 0

for valor in vendas:
    if valor % 2 == 0:
        soma += valor

print(f"Soma dos valores pares: {soma}")

# 8° Questão
try:
    valor = float(input("Digite o valor da compra: R$ "))

    if valor > 500:
        desconto = 0.20
    elif valor >= 200:
        desconto = 0.10
    else:
        desconto = 0.0

    preco_final = valor * (1 - desconto)

    print(f"Preço final: R$ {preco_final:.2f}")

except ValueError:
    print("Entrada inválida! Digite um número válido.")

# 9° Questâo
notas = [6, 8, 7.5, 9, 5, 10, 4, 7.2]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print(f"Quantidade de notas acima de 7: {contador}") 

# 10° Questão
frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)

# 11° Questão
idades = []

for i in range(5):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)

idades.sort()

print("Idades em ordem crescente:", idades)

# 12° Questão
while True:
    print("Calculadora")
    print("1 Soma")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("5 Sair")

    opcao = input("Escolha: ")

    if opcao == "5":
        print("Encerrando")
        break

    try:
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))

        if opcao == "1":
            print("Resultado:", n1 + n2)
        elif opcao == "2":
            print("Resultado:", n1 - n2)
        elif opcao == "3":
            print("Resultado:", n1 * n2)
        elif opcao == "4":
            if n2 == 0:
                print("Não pode dividir por zero")
            else:
                print("Resultado:", n1 / n2)
        else:
            print("Opção inválida")

    except:
        print("Digite números válidos")