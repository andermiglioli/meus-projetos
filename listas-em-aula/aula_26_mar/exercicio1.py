peso = float(input("informe seu peso (ex: 65.5)"))

altura = float(input("informe sua altura (1.70)"))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    categoria = "magreza"
elif IMC <25:
    categoria = "normal"
elif IMC < 30:
    categoria = "sobrepeso"
else:
    categoria = "obesidade"

print(f"IMC = {IMC:.2f} - {categoria}")
