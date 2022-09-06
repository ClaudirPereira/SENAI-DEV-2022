pilha = []


def empilhar(numero):
    print('....................')
    print('.: EMPILHAMENTO :.')
    for i in range(numero):
        pilha.append(i)
    print(pilha)
    print(f'Elemento no top da pilha é: {pilha[-1]}')


empilhar(20)


def desempilhar():
    print('....................')
    print('.: DESEMPILHANDO :.')
    topo = pilha.pop()
    print(f'Elemento excluído do topo foi: {topo}. Segue a nova pilha: {pilha}')
    print(f'Elemento do topo da pilha é: {pilha[-1]}')


desempilhar()


def limpar_pilha():
    print('....................')
    print('.: LIMPANDO PILHA :.')
    pilha.clear()
    print(f'Segue pilha com todos elementos removidos: {pilha}.')


limpar_pilha()


def l_e_v():  # false vazia \\ true com ítens
    print('....................')
    print('.: LISTANDO PILHA :.')
    print(len(pilha) == 0)


l_e_v()


def l_e_v():  # false vazia \\ true com ítens
    print('....................')
    print('.: STATUS DA PILHA :.')
    print(len(pilha) != 0)


l_e_v()
