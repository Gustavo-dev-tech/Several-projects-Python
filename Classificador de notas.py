notas = [8.5, 6.0, 4.2, 9.1, 5.5]
nome = ["Gustavo", "Julho", "Biel", "Luan","Rodrigo"]
i = 0
for nota in notas :
    if nota >= 7:
        print (f"{nome[i]} Foi APROVADO com a nota {nota}. \n ")
    elif nota >= 5 and nota < 7 :
        print (f"{nome[i]} Ficou de RECUPERAÇÂO com a nota {nota} \n")
    else:
        print (f"{nome[i]} Foi REPROVADO com a nota {nota} \n")
    i+=1