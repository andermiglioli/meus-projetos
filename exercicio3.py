#Solicite ao usuário que informe o estoque no início do dia (int) e a quantidade 
# vendida ao final do dia (int). 
# Atualize a quantidade utilizando atribuição -= para mostrar o estoque final. 

estoque = (int(input("informe o estoque inicial")))
vendas = (int(input("informe numero de itens vendidos")))

estoque -= vendas

print("o estoque final é de", estoque)