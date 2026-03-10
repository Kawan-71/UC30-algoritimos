paciente = {}

paciente["nome"] = input("Qual o seu nome: ")
paciente["idade"] = int(input("Quantos anos você tem: "))
paciente["peso"] = float(input("Digite seu peso(Kg): "))
paciente["altura"] = float(input("Digite sua altura: "))

imc = paciente["peso"] / (paciente["altura"] ** 2)

paciente["imc"] = imc

print("\n dados")
print("nome: ", paciente["nome"])
print("idade: ", paciente["idade"])
print("peso: ", paciente["peso"])
print("altura: ", paciente["altura"])
print("IMC: ", round(paciente["altura"], 2))