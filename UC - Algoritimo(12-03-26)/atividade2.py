#crie uma função chamada calcularSalario que receba valor por hora e horas trabalhadas, e retorne o salário total
# Crie uma função chamada calcularSalario que receba o valor por hora e horas trabalhadas, e retorne o salário total

horas = float(input("Quantas horas você trabalha? "))
valor = float(input("Quantos você recebe por hora? "))

def calcularSalario(horas, valor): 
    salario = horas * valor
    return salario

salarioTotal = calcularSalario(horas, valor)
print(f"Seu salário total é de: {salarioTotal}")