def bbst(a_lista):
    for pass_numero in range(len(a_lista) - 1, 0, -1):
        for i in range(pass_numero):
            if a_lista[i] > a_lista[i + 1]:
                temp = a_lista[i]
                a_lista[i] = a_lista[i + 1]
                a_lista[i + 1] = temp


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]


bbst(lista)

print(lista)
