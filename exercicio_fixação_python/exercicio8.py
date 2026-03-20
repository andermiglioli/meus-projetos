#Leia um número como string e imprima o seu tipo antes e depois de converter para int.

valor_string = input("informe o numero")

print(f" antes da conversão, o valor é {valor_string}, e o tipo é {type(valor_string)}")

valor_inteiro = int(valor_string)
print(f"após a conversão, o valor é {valor_inteiro} e o tipo é {type(valor_inteiro)}")



