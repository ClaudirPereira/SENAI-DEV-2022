avioes_e_assentos = [
    ['Boeing', 400],
    ['Airbus', 250],
    ['Cruzader', 150],
    ['Tecks', 500]
]

ass_avi_ocupados = [[], [], [], []]


def reservar_passagem(nome="", aviao=0):
    if avioes_e_assentos[aviao][1] == len(ass_avi_ocupados[aviao]):
        return 'Avião Indisponíel!'

    else:
        ass_avi_ocupados[aviao].append(nome)
        return 'Passagem Reservada com Sucesso!'


def consultar_aviao(aviao=0):
    print(avioes_e_assentos)
    t1 = ""

    for i in ass_avi_ocupados[aviao]:
        t1 = f'{t1} {i}\n'

    t2 = f'Número do Avião: {aviao}\nNome do Avião: {avioes_e_assentos[aviao][0]}\nCapacidade: {avioes_e_assentos[aviao][1]}\nPassageiro: {t1}'

    return t2


# noinspection PyUnboundLocalVariable
def consultar_passageiro(nome=""):
    busca = False
    for i in range(len(ass_avi_ocupados)):
        for x in range(len(ass_avi_ocupados[i])):
            if ass_avi_ocupados[i][x] == nome:
                busca = True
    if busca:
        return f'Passageiro registrado no avião {i}, posição {x}.'
    else:
        return 'Passageiro Não Encontrado.'


def menu():
    op = 0
    while op != 5:
        print("""
[1] - Registrar Aviões
[2] - Reservar Passagem Aérea
[3] - Realizar Consulta por Avião
[4] - Realizar Consulta por Passageiro
[5] - Encerrar
        """)

        op = int(input('Escolha uma opção do Menu: '))

        if op == 1:
            t1 = input('Insira o nome do novo avião: ')
            t2 = int(input('Insira a capacidade de Passageiros: '))

            avioes_e_assentos.append([t1, t2])
            ass_avi_ocupados.append([])

        elif op == 2:
            t1 = input('Digite o nome do Passageiro: ')
            t2 = int(input('Digite o Número do Avião: '))
            print(reservar_passagem(t1, t2))

        elif op == 3:
            t1 = int(input('Insira o numero do Avião: '))
            print(consultar_aviao(t1))

        elif op == 4:
            t1 = input('Digite o nome do Passageiro: ')
            print(consultar_passageiro(t1))

        elif op == 5:
            print('Programa Finalizado com Sucesso!')
            break

        else:
            print(' ** Digite uma opção válida ** ')


menu()
