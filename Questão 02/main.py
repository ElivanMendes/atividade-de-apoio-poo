# Opções do Menu. #
def menu_info():
    print('\n\t0 - Sair\n\t1 - Cadastrar\n\t2 - Remover Menores de 18 Anos')
    print('\t3 - Imprimir\n\t4 - Imprimir Menores de 18 Anos\n')


# Ler e Verifica Opção Escolhida pelo Usuario. #
def ler_opcao():
    while True:
        op = input('\tInforme a Opção: ')
        if not op.isnumeric():
            print('\n\tOpção Invalida!')
            menu_info()
            continue
        return int(op)


# Dicionarios. #
dict_pessoas = {}
dict_p_menores = {}


# Cadastra as Informações de uma Pessoa no Dicionário. #
def cadastrar_pessoa(id_p, nome, idade, cpf):
    dict_pessoas[id_p] = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
    }


# Ler os Dados de uma Pessoa e Adiciona no Dicionário. #
def ler_dados_e_adicionar(id_p):
    nome = input('\n\tInforme o Nome: ')
    idade = int(input('\tInforme a Idade: '))
    cpf = input('\tInforme o CPF: ')

    cadastrar_pessoa(id_p, nome, idade, cpf)

    print('\n\tCadastro Realizado com Sucesso.')


# Busca Menores de 18 Anos e Adiciona na Lista de Menores de 18 Anos.
# Retorna a Lista com o ID dos Menores de 18 Anos. #
def buscar_menores():
    lista = []
    for d_k, d_v in dict_pessoas.items():
        if d_v['idade'] < 18:
            dict_p_menores.update({d_k: d_v})
            lista.append(d_k)
    return lista


# Remove as Pessoas Menores de 18 Anos do Dicionário. #
def remover_menores(lista_id):
    for id_p in lista_id:
        del(dict_pessoas[id_p])


# Imprimi os Dados do Dicionario. #
def imprimir_dados(dict_p):
    for p_k, p_v in dict_p.items():
        print(f'\tID: {p_k}:')
        for d_k, d_v in p_v.items():
            print(f'\t\t{d_k.capitalize()}: {d_v}')


def menu():
    id_p = 0

    while True:
        menu_info()
        op = ler_opcao()

        if op == 0:
            print('\n\tSAINDO...')
            break
        elif op == 1:

            id_p += 1
            ler_dados_e_adicionar(id_p)

        elif op == 2:

            if not dict_pessoas:
                print(f'\n\tDicionario Vazio!')
                continue

            if not buscar_menores():
                print('\n\tNão há Menores de 18 Anos para Remover!')
                continue

            remover_menores(buscar_menores())

            print('\n\tMenores de 18 Anos Removidos com Sucesso.')

        elif op == 3:

            if not dict_pessoas:
                print(f'\n\tDicionario Vazio!')
                continue

            print(f'\n\t---------- TOTAL DE PESSOAS: {len(dict_pessoas)} ----------')
            imprimir_dados(dict_pessoas)
            print(f'\t-----------------------------------------')

        elif op == 4:

            if not dict_p_menores:
                print(f'\n\tDicionario Vazio!')
                continue

            print(f'\n\t---------- TOTAL DE PESSOAS: {len(dict_p_menores)} ----------')
            imprimir_dados(dict_p_menores)
            print(f'\t-----------------------------------------')

        else:
            print('\n\tOpção Invalida!')


menu()
