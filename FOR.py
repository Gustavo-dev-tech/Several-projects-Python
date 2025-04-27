for repetição in range (3): # Pode ser lido como: "para cada x dentro de y"
#Range é uma função que gera sequencia de numeros

#for i in range(2, 6): print(i) 👉 Vai imprimir: 2, 3, 4, 5
#range(início, fim, passo) for i in range(1, 10, 2):  Vai imprimir: 1, 3, 5, 7, 9

    nome = input("Ola Digite seu nome: ")
    idade = int(input("Isso ai... \n Agora digite sua idade: "))
    sexo = int(input("Selecione seu Sexo.\n 1 - Masculino \n 2 - Feminino \n"))
    if sexo == 1:
        sexo = "Masculino"
    else:
        sexo = "Feminino"
    print(f"Ola {nome} como vai ? \n você ja tem {idade} anos de idade INCRIVEL !!! \n você é do sexo {sexo}")
