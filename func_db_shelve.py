import shelve
from time import sleep
import main as lk


def shelve_salvar(dados):
    with shelve.open('database.db', writeback=True) as db:
        try:
            db['inf'].append(dados)
        except KeyError:
            db['inf'] = []
            db['inf'].append(dados)


def shelve_ler():
    with shelve.open('database.db') as db:
        if not len(db['inf']):
            print('\033[35mLista vazia!\033[m')
        for i in range(len(db['inf'])):
            nome = db['inf'][i][0]
            turma = db['inf'][i][1]
            print(f"""
[ {i + 1} ] ---------------------------------------------
Nome: \033[34m{nome}\033[m
Turma: \033[34m{turma}\033[m""")
        print('\n')


def shelve_procurar(proc, modo):
    lista = []
    with shelve.open('database.db') as db:
        if modo == 'i':
            x = 'Nome'
            xx = 'o'
            for i, l in db['inf']:
                if proc in i:
                    lista.append([i, l])
        elif modo == 'l':
            x = 'Turma'
            xx = 'a'
            for i, l in db['inf']:
                if proc in l:
                    lista.append([i, l])
    return [x, xx, proc, lista]


def procurar_continuacao(l):
    lk.logo()
    lk.menu1()
    print(f'\n{l[0]} a ser procurad{l[1]}: \033[34m{l[2]}\033[m')
    for i in range(len(l[3])):
        print(f"""
[ {i + 1} ] ---------------------------------------------
Nome: \033[34m{l[3][i][0]}\033[m
Turma: \033[34m{l[3][i][1]}\033[m""")
    if len(l[3]) > 1:
        y = 'es'
        yy = 's'
    else:
        y = yy = ''
    print(f'\n\033[35m{len(l[3])} valor{y} encontrado{yy}.\033[m')
    if len(l[3]) > 0:
        print('\nDigite o número do cadastro para selecionar: ')
    print('\n')
    return l[3]


def shelve_atualizar(novo_valor, lista, n):
    with shelve.open('database.db', writeback=True) as db:
        ii = lista[n][0]
        ll = lista[n][1]
        c = cc = 0
        for i, l in db['inf']:
            c += 1
            if i == ii and l == ll:
                cc = c
        db['inf'][cc - 1] = novo_valor
        print(f'{ii} | {ll} >> {novo_valor[0]} | {novo_valor[1]}')


def shelve_deletar(lista, n):
    with shelve.open('database.db', writeback=True) as db:
        c = 0
        for i, l in db['inf']:
            if i == lista[n][0] and l == lista[n][1]:
                del db['inf'][c]
                print('\n\033[35mDeletado com sucesso!!\033[m')
            c += 1
    sleep(1)


def shelve_reset():
    with shelve.open('database.db') as db:
        del db['inf']
        db['inf'] = []
    print('\033[35mBanco de dados resetado com sucesso!\033[m')
    sleep(1)
