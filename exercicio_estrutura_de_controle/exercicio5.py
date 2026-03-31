num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if num1 > num2:
    print(f"O primeiro número ({num1}) é o maior.")
elif num2 > num1:
    print(f"O segundo número ({num2}) é o maior.")
else:
    print("Os dois números são iguais.")