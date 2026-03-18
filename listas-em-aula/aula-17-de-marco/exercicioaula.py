###aula 17 de março de 2026


frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

#acessando elementos
print("primeira fruta", frutas[0])
print("ultima fruta", frutas[2])

#alterando elementos

frutas[1] = "banana-nanica"
print("após alteração", frutas)

#adicionando elementos
frutas.append("morango") #adiciona no final
frutas.insert(1, "pera")

print("após adicionar", frutas)

frutas.remove ("uva") #remove pelo valor
ultima = frutas.pop() #remove e retorna o ultimo
print("após remover uva e pop():", frutas, "última removida", ultima)


