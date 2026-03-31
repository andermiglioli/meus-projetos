nota = float(input("informe a nota"))

if 0 <= nota <5:
    resultado = "reprovado"
elif 5 <= nota <= 6.9:
    resultado = " em recuperação"
elif 7 <= nota <= 8.9:
    resultado = "aprovado"
elif 9 <= nota <= 10:
    resultado = "aprovado com excelencia"
else:
    resultado = None
if resultado is not None:
    print(f"após a prova, sua nota foi de {nota}, e voce está {resultado}")

else:
    print("ERRO, a nota informada deve estar entre 0 e 10")