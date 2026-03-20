#12.Leia 3 notas (float) e imprima a média com duas casas decimais.

nota1 = float(input("informe a primeira nota"))
nota2 = float(input("informe a segunda nota"))
nota3 = float(input("informe a terceira nota"))

media = (nota1 + nota2 + nota3) / 3

print(f" a media das tres notas é {media:.2f}")