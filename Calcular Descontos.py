precos = [120, 80, 40, 200]
final = 0
for desconto in precos:
    if desconto > 100:
        final = desconto - desconto  / 100 * 20
        desconto = desconto / 100 * 20
        
    elif desconto > 50:
        final = desconto - desconto / 100 * 10
        desconto = desconto / 100 * 10

    else:
        final = desconto - desconto / 100 * 5
        desconto = desconto / 100 * 5

    print(f"\n O desconto total foi de {desconto} \nO preço final sera de {final}. ")


