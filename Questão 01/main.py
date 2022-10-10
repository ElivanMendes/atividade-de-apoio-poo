# Função que Mostra as Opções do Menu. #
def menu_info():
    print('\n\t0 - Sair\n\t1 - Adicionar\n\t2 - Imprimir\n')


# Função que Ler a Opção do Menu. #
def ler_opcao():
    while True:
        op = input('\tInforme a Opção: ')

        if not op.isnumeric():
            print('\n\tOpção Invalida!')
            menu_info()
            continue

        return int(op)


# Dicionario. #
agenda = {}


# Função que Adiciona os Dados no Dicionário. #
def adicionar_na_agenda(**kwargs):
    kwargs['agend'][kwargs['cpf']] = {
        'nome': kwargs['nome'],
        'idade': kwargs['idade'],
        'telefone': kwargs['telefone'],
    }


# Função que Ler os Dados a Serem Adicionados no Dicionário. #
def ler_dados_e_adicionar_na_agenda():
    cpf = input('\n\tInforme o CPF: ')
    nome = input('\tInforme o Nome: ')
    idade = int(input('\tInforme a Idade: '))
    telefone = input('\tInforme o Telefone: ')

    adicionar_na_agenda(agend=agenda, cpf=cpf, nome=nome, idade=idade, telefone=telefone)

    print('\n\tAdicionado na Agenda com Sucesso.')


# Função que Imprimir os Dados. #
def imprimir_dados(cpf_k, cpf_v):
    print('\t-----------------------------------')

    print(f'\tCPF: {cpf_k}')
    for k, v in cpf_v.items():
        print(f'\t\t{k.capitalize()}: {v}')

    print('\t-----------------------------------')


# Função que Imprimir o Dicionário. #
def imprimir_dicionario():
    for k, v in agenda.items():
        imprimir_dados(k, v)


# Menu das Opções. #
def menu():
    while True:
        menu_info()
        op = ler_opcao()

        if op == 0:
            print('\n\tSAINDO...')
            break
        elif op == 1:

            ler_dados_e_adicionar_na_agenda()

        elif op == 2:

            if not agenda:
                print('\n\tAgenda Vazia!')

            imprimir_dicionario()

        else:
            print('\n\tOpção Invalida!')


menu()
