## Remova um número se ele existir
# Tarefa: Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois.
#Use: int(), input(), in, remove(), len(), print()
 #Tipos: int, list.
 #Conceitos: teste de pertencimento, tratamento simples de remoção, função len().

num1 = int(input("informe o primeiro numero"))
num2 = int(input("informe o segundo numero"))
num3 = int(input("informe o terceiro numero"))
num4 = int(input("informe o quarto numero"))
valor_alvo = int(input("informe o valor a ser removido"))

numeros = [num1, num2, num3, num4]

print(numeros)

len(numeros)