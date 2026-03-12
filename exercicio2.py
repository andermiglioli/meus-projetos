# Solicite ao usuário que informe um orçamento (float) e um gasto (float). 
#Utilize atribuição -= para descontar o gasto do orçamento.

orcamento = (float(input("informe seu orçamento")))
gasto = (float(input("informe o valor do seu gasto")))

orcamento -= gasto

print(f"seu novo orçamento é de: R$ {orcamento:.2f}")