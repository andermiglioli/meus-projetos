#18.Leia um nome e uma nota (float), com uma casa decimal, e imprima:
#Aluno <nome> ficou com nota <nota> 

aluno = input("informe nome do aluno ")
nota = float(input("informe a nota do aluno "))

print(f"Aluno {aluno} ficou com a nota {nota:.1f}")