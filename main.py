#!/usr/bin/env python3
# Python 3.6.2
from os import system
from time import sleep
import func_db_shelve as sdb


def logo(op='clear'):
    system(op)
    print("""\033[34m
|||||||||||||||||||||||||||||||||||||||||||||||||||
 _    _   _ _  _______     ____   ___  _____ _____
| |  | | | | |/ / ____|   / ___| / _ \|  ___|_   _|
| |  | | | | ' /|  _|     \___ \| | | | |_    | |
| |__| |_| | . \| |___     ___) | |_| |  _|   | |
|_____\___/|_|\_\_____|___|____/ \___/|_|     |_|
                     |_____|
|||||||||||||||||||||||||||||||||||||||||||||||||||
\033[m""")


def menu0():
    print('=-=' * 17)
    print('Sair: q')
    print('=-=' * 17)


def menu1():
    print('=-=' * 17)
    print('Voltar: <  | Sair: q')
    print('=-=' * 17)


def inicio0():
    while True:
        logo('reset')
        menu0()
        print("""
1) Criar
2) Ver
3) Atualizar/Deletar

0) Configurar

        """)
        opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
        if opcao0 == '1':
            criar()
        elif opcao0 == '2':
            ver()
        elif opcao0 == '3':
            atualizar()
        elif opcao0 == '0':
            configurar()
        elif opcao0 == 'q':
            raise KeyboardInterrupt
        else:
            print('\n\033[35mValor Inválido!!\033[m')
            sleep(1)
            continue


def criar():
    while True:
        while True:
            logo()
            print('=-=' * 17)
            print('Novo cadastro:\n\n')
            nome = str(input('Informe o nome: ')).strip().upper()
            turma = str(input('Informe a turma: ')).strip().upper()
            print(f"""
-----------------------------------------------------
Nome: {nome}
Turma: {turma}
-----------------------------------------------------
            """)
            op = str(input('Está correto (s/n)? ')).strip().lower()
            if op == 's':
                break
        print()
        print('-' * 53)
        print('Salvo com sucesso!')
        print('-' * 53)
        print()
        dados = [nome, turma]
        sdb.shelve_salvar(dados)
        op = str(input('Deseja fazer outro cadastro (s/n)? ')).strip().lower()
        if op == 'n':
            break
            # sleep(0.5)


def ver():
    while True:
        logo()
        menu1()
        print('\nLista de Cadastros:\n')
        sdb.shelve_ler()
        opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
        if opcao0 == '<' or opcao0 == ',':
            inicio0()
        elif opcao0 == 'q':
            raise KeyboardInterrupt
        else:
            print('\n\033[35mValor Inválido!!\033[m')
            sleep(1)
            continue
            # sleep(1)


def atualizar():
    while True:
        logo()
        menu1()
        print("""
Deseja procurar por:

[ n ] Nome
[ t ] Turma

        """)
        try:
            opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()[0]
        except IndexError:
            atualizar()
        if opcao0 == 'n':
            logo()
            print('\nInforme o nome a ser procurado:\n\n')
            n_proc = str(input('\033[34mNome >>\033[m ')).strip().upper()
            l = sdb.shelve_procurar(n_proc, 'i')
            lista = sdb.procurar_continuacao(l)
        elif opcao0 == 't':
            logo()
            print('=-=' * 17)
            print('\nInforme a turma a ser procurada:\n\n')
            n_turm = str(input('\033[34mTurma >>\033[m ')).strip().upper()
            l = sdb.shelve_procurar(n_turm, 'l')
            lista = sdb.procurar_continuacao(l)
        elif opcao0 == '<' or opcao0 == ',':
            inicio0()
        elif opcao0 == 'q':
            raise KeyboardInterrupt
        else:
            print('\n\033[35mValor Inválido!!\033[m')
            sleep(1)
            continue
        opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
        if opcao0.isnumeric():
            n_escolhido = int(opcao0) - 1
            if len(l[3]) < int(opcao0):
                print('\n\033[35mValor Não Identificado!!\033[m')
                sleep(2)
                atualizar()
        if opcao0 == '<' or opcao0 == ',':
            atualizar()
        elif opcao0 == 'q':
            raise KeyboardInterrupt
        elif opcao0.isnumeric():
            logo()
            menu1()
            print(f'\nSelecionado{lista[n_escolhido]}\n')
            print('=-=' * 17)
            print("""
Opções:

[ a ] Atualizar
[ d ] Deletar

            """)
            opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
            if opcao0 == 'a':
                while True:
                    while True:
                        logo()
                        # print(lista, n_escolhido)
                        print('=-=' * 17)
                        print('Atualizando cadastro:\n\n')
                        nome = str(input('Informe o novo nome: ')).strip().upper()
                        turma = str(input('Informe a nova turma: ')).strip().upper()
                        print(f"""
-----------------------------------------------------
Nome: {nome}
Turma: {turma}
-----------------------------------------------------
                        """)
                        op = str(input('Está correto (s/n)? ')).strip().lower()
                        if op == 's':
                            break
                    print()
                    print('-' * 53)
                    print('Salvo com suceso!')
                    print('-' * 53)
                    print()
                    sdb.shelve_atualizar([nome, turma], lista, n_escolhido)
                    op = str(input('Deseja fazer outra alteração (s/n)? ')).strip().lower()
                    if op == 's':
                        break
                    else:
                        inicio0()
                        # sleep(1)
            elif opcao0 == 'd':
                deletar(lista, n_escolhido)
            elif opcao0 == 'q':
                raise KeyboardInterrupt
            elif opcao0 != ',' or opcao0 != '<':
                print('\n\033[35mValor Inválido!!\033[m')
                sleep(1)
        else:
            print('\n\033[35mValor Inválido!!\033[m')
            sleep(1)
            continue


def deletar(lista, n_escolhido):
    while True:
        logo()
        print('=-=' * 17)
        print(f"""
Deseja excluir {lista[n_escolhido]}?

[ s ] Sim
[ n ] Não

        """)
        opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
        if opcao0 == 's':
            logo()
            print('=-=' * 17)
            print("""
\033[35mTem certeza?

[ s ] Sim
[ n ] Não\033[m

            """)
            opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
            if opcao0 == 's':
                break
        else:
            atualizar()
    sdb.shelve_deletar(lista, n_escolhido)
    inicio0()


def configurar():
    while True:
        while True:
            logo()
            menu1()
            print("""
Opções:

[ r ] Resetar banco de dados

            """)
            opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
            if opcao0 == ',' or opcao0 == '<':
                inicio0()
            elif opcao0 == 'q':
                raise KeyboardInterrupt
            elif opcao0 == 'r':
                break
            else:
                continue
        logo()
        print('=-=' * 17)
        print("""
\033[35mTem certeza?

[ s ] Sim
[ n ] Não\033[m

        """)
        opcao0 = str(input('\033[34mOpção >>\033[m ')).strip().lower()
        if opcao0 == 's':
            break
        else:
            configurar()
    sdb.shelve_reset()
    inicio0()


def main():
    """
    :return:
    """
    try:
        inicio0()
    except KeyboardInterrupt:
        system('clear')
        print(r"""\033[34m
 _____ ___ _   _    _    _     ___ _____   _    _   _ ____   ___       
|  ___|_ _| \ | |  / \  | |   |_ _|__  /  / \  | \ | |  _ \ / _ \      
| |_   | ||  \| | / _ \ | |    | |  / /  / _ \ |  \| | | | | | | |     
|  _|  | || |\  |/ ___ \| |___ | | / /_ / ___ \| |\  | |_| | |_| | _ _ 
|_|   |___|_| \_/_/   \_\_____|___/____/_/   \_\_| \_|____/ \___(_|_|_)
        \033[m""")
        sleep(1)
        system('reset')
    else:
        print('Erro não identificado!!')


if __name__ == '__main__':
    main()
