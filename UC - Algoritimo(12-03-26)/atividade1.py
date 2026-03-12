# Gere uma função que mostre a soma e o produto de dois números
numero = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))

def numeros(numero, numero2):
    plus = numero + numero2
    multiplication = numero * numero2
    return plus, multiplication

resultado = numeros(numero, numero2)
print(f"A soma e o produto é igual a: {resultado}")