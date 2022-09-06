print('.: : Iniciando Programa : :.')
print('.: [1] - Cadastrar Usuário :.')
print('.: [2] - Lista Usuários Cadastrados :.')
print('.: [3] -  Finalizar  :.')

op = 0
lista = []
while op != 5:
    op = int(input('Escolha uma opção: '))
    if op == 1:
        user_vol = int(input("Digite quantos usuários serão cadastrados: "))
        for i in range(0, user_vol):
            n1 = str(input("Digite seu Nome: "))
            n2 = str(input('Digite sua Idade: '))
            lista.append([n1, n2])
    elif op == 2:
        print(f'Usuários Cadastrados: {lista} ')
    elif op == 3:
        print('=' * 40)
        print("Programa Finalizado com Sucesso!")
        print('=' * 40)
    else:
        print("Escolha invalida")
