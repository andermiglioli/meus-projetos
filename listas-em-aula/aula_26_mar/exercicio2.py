temperatura = int(input("informe a temperatura atual"))

if temperatura < 10:
    classificacao = "muito frio"
elif  10 <= temperatura <= 24:
    classificacao = "agradavel"
elif 25 <= temperatura <= 30:
    classificacao = "quente"
else:
    classificacao = "muito quente"

print(f"a temperatura informada,{temperatura} graus celsius, é considerada {classificacao}") 
