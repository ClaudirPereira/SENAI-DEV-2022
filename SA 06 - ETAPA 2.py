
def mgst(lista, inicio, fim):

    if(fim - inicio > 1):
        meio = ((fim + inicio) // 2)
        mgst(lista, inicio, meio)
        mgst(lista, meio, fim)
        merge_ordenar_geral(lista,  inicio,  meio, fim)
        print(lista)


def merge_ordenar_geral(lista, inicio, meio, fim):
    lista_esquerda = lista[inicio:meio]
    lista_direita = lista[meio:fim]
    menor_valor_lista_esq = 0
    menor_valor_lista_dir = 0
    for i in range(inicio, fim):
        if menor_valor_lista_esq >= len(lista_esquerda):
            lista[i] = lista_direita[menor_valor_lista_dir]
            menor_valor_lista_dir = menor_valor_lista_dir + 1

        elif menor_valor_lista_dir >= len(lista_direita):
            lista[i] = lista_esquerda[menor_valor_lista_esq]
            menor_valor_lista_esq = menor_valor_lista_esq + 1

        elif lista_esquerda[menor_valor_lista_esq] < lista_direita[menor_valor_lista_dir]:
            lista[1] = lista_esquerda[menor_valor_lista_esq]
            menor_valor_lista_esq = menor_valor_lista_esq + 1

        else:
            lista[1] = lista_direita[menor_valor_lista_dir]
            menor_valor_lista_dir = menor_valor_lista_dir + 1


lista = [2, 14, 13, 12, 9, 8, 7, 6]
print(lista)
print('---------------------------')
inicio = 0
fim = len(lista)
mgst(lista, inicio, fim)
