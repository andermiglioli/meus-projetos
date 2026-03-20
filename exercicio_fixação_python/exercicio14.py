#14.Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)

min_totais = int(input("informe os minutos a converter"))
horas = min_totais // 60
minutos = min_totais % 60

print(f"após a conversão, o resultado é {horas}h{minutos}m")