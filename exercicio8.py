#Solicite um número (int), aplique n %= 2 e exiba o valor
#  na tela. Se o resultado for 0, o número é par; se o resultado for 1, o número é ímpar.


numero = (int(input(f"informe o número ")))


if numero % 2 == 0:
    print(f" o numero {numero} é um número par")

else:
    print(f"o número {numero} é um número ímpar")