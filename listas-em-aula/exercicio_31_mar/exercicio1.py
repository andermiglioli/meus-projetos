lista_numeros = []

print("Digite 10 números inteiros:")
for i in range(10):
    num = int(input(f"Informe um numero: "))
    lista_numeros.append(num)

for numero in lista_numeros:
    if numero > 10:
        status = "maior que 10"
    elif numero == 10:
        status = "igual a 10"
    else:
        status = "menor que 10"
    
    print(f"O número {numero} é {status}.")