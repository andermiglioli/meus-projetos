#Solicite um valor de estoque (int), subtraia as vendas utilizando -= e depois a reposição do estoque utilizando +=, por fim, aplique %= 6

estoque = (int(input("informe seu estoque inicial ")))
vendas = (int(input("informe a quantidade vendida ")))
reposicao = (int(input("informe quantidade reposta no estoque")))

estoque -= vendas
print(f"a quantidade em estoque após as vendas é de {estoque}")

estoque += reposicao
print(f"o estoque após a reposição é de {estoque}")


estoque %= 6
print(f"após a divisão do estoque em conjunto de 6 unidades, sobraram  {estoque} itens")




