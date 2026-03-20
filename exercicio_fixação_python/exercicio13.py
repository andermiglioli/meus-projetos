#Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário

salario = float(input("informe seu salario: R$ "))
percentual = float(input("informe o percentual de aumento"))
aumento = salario * (percentual/100)
novo_salario = salario + aumento

print(f" o salario com o aumento é de R$ {novo_salario:.2f}")
