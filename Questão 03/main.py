# Opções do Menu. #
def menu_info():
    print('\n\t0 - Sair\n\t1 - Cadastrar\n\t2 - Imprimir Dicionario Principal')
    print('\t3 - Imprimir Dicionario de Backup\n')


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
dicionario_principal = {}
dicionario_de_backup = {}


# Cadastra as Informações de uma Pessoa no Dicionário. #
def cadastrar_pessoa(dicionario, id_p, nome, idade, cpf):
    dicionario[id_p] = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
    }


# Ler os Dados de uma Pessoa e Adiciona no Dicionário. #
def ler_dados_e_adicionar(dic_principal, dic_backup, id_p):
    nome = input('\n\tInforme o Nome: ')
    idade = int(input('\tInforme a Idade: '))
    cpf = input('\tInforme o CPF: ')

    cadastrar_pessoa(dic_principal, id_p, nome, idade, cpf)
    cadastrar_pessoa(dic_backup, id_p, nome, idade, cpf)

    print('\n\tCadastro Realizado com Sucesso.')


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

            if len(dicionario_principal) >= 5:
                dicionario_principal.clear()

            id_p += 1
            ler_dados_e_adicionar(dicionario_principal, dicionario_de_backup, id_p)

        elif op == 2:

            if not dicionario_principal:
                print(f'\n\tDicionario Vazio!')
                continue

            print(f'\n\t---------- TOTAL DE PESSOAS: {len(dicionario_principal)} ----------')
            imprimir_dados(dicionario_principal)
            print(f'\t-----------------------------------------')

        elif op == 3:

            if not dicionario_de_backup:
                print(f'\n\tDicionario Vazio!')
                continue

            print(f'\n\t---------- TOTAL DE PESSOAS: {len(dicionario_de_backup)} ----------')
            imprimir_dados(dicionario_de_backup)
            print(f'\t-----------------------------------------')

        else:
            print('\n\tOpção Invalida!')


menu()
