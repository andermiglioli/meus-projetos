

#calcular imc e classificar de forma simples

nome = input("nome: ")
peso = float(input("peso (kg): "))
altura = float(input("altura (m): "))

imc = peso / (altura ** 2)           #aritiméticos
print(f"IMC de {nome}: {imc: 2f}")

#comparação = lógicos (faixa simplificada)

baixo_peso = imc < 18.5
normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc>= 25) and (imc< 30)
obesidade = imc>=30

print("baixo peso", baixo_peso)
print("normal", normal)
print("sobrepeso", sobrepeso)
print("obesidade", obesidade)


# exercicio teams

saldo = (float(input("informe seu saldo")))
deposito = (float(input("informe o valor do seu depósito")))

saldo += deposito

print(f"seu novo saldo é de: R$ {saldo:.2f}")
