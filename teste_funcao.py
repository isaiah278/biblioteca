import os
from datetime import datetime, timedelta
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# lista e bibliotecas usadas nas funcoes
livros = []
autores = []
alunos = []
biblioteca = {
    'livros': [],
    'autores': [],
    'emprestimos': []
}
# variavel para mostrar datas
data = datetime.now()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def menu():
    print('''=-=-=-=-= MENU =-=-=-=-= 
Livros [1]
Autores [2]
Alunos [3]
Emprestimos [4]
Sair do sistema [0]
=-=-=-=-= MENU =-=-=-=-= ''')
    escolha = int(input('escolha: '))
    # limpar tela
    limpar_tela()
    #-------------
    #livros
    if escolha == 1:
        print('''=-=-=-=-= LIVROS =-=-=-=-= 
Adicionar livro [1]
Remover livro [2]
Listar livros [3]
=-=-=-=-= LIVROS =-=-=-=-=''')
        decisao = int(input('escolha: '))
        # limpar tela
        limpar_tela()
        #-------------
        if decisao == 1:
            return 'livro1'
        if decisao == 2:
            return 'livro2'
        if decisao == 3:
            return 'livro3'
    #autores
    elif escolha == 2:
        print('''=-=-=-=-= AUTORES =-=-=-=-=
Adicionar autor [1]
Remover autor [2]
Listar autores [3]              
=-=-=-=-= AUTORES =-=-=-=-=''')
        decisao = int(input('escolha: '))
        # limpar tela
        limpar_tela()
        #-------------
        if decisao == 1:
            return 'autor1'
        if decisao == 2:
            return 'autor2'
        if decisao == 3:
            return 'autor3'
    #alunos
    elif escolha == 3:
        print('''=-=-=-=-= ALUNOS =-=-=-=-=
Cadastrar aluno [1]
Remover aluno [2]
Listar alunos [3]      
=-=-=-=-= ALUNOS =-=-=-=-=''')
        decisao = int(input('escolha: '))
        # limpar tela
        limpar_tela()
        #-------------
        if decisao == 1:
            return 'alunos1'
        if decisao == 2:
            return 'alunos2'
        if decisao == 3:
            return 'alunos3'
        
    # emprestimos
    elif escolha == 4:
        print('''=-=-=-=-= EMPRESTIMOS =-=-=-=-=
Fazer empréstimo [1]
Devolver livro [2]
Consultar empréstimos [3]        
=-=-=-=-= EMPRESTIMOS =-=-=-=-=''')
        decisao = int(input('escolha: '))
        # limpar tela
        limpar_tela()
        #-------------
        if decisao == 1:
            return 'emprestimos1'
        if decisao == 2:
            return 'emprestimos2'
        if decisao == 3:
            return 'emprestimos3'
    else:
        return 0
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def limpar_tela():
    limpar = os.system('cls')
    return limpar
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def add_livro():
    # gerando o Id do livro automaticamente
    if livros == []:
        ident = 0
    else:
        ident = livros.index(livros[-1])+1
    titulo = input('titulo: ')
    autor = input('autor: ')
    # limpar tela
    limpar_tela()
    #-------------
    dataCadastro = data.strftime('%d/%m/%Y')
    dataAtualizacao = dataCadastro
    # guandando os dados do livro em um dicionario e adicionando ele na lista livros
    informacoes = {'id':ident, 'titulo': titulo, 'autor': autor, 'disponivel': True, 'dataCadastro': dataCadastro, 'dataAtualizacao': dataAtualizacao }
    livros.append(informacoes)
    # adicionar livro a biblioteca
    biblioteca['livros'].append(titulo)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def add_autor():
    # gerando o Id do livro automaticamente
    if autores == []:
        ident = 0
    else:
        ident = autores.index(autores[-1])+1
    nome = input('nome: ')
    dataNascimento = 0
    # limpar tela
    limpar_tela()
    #-------------
    # guandando os dados do autor em um dicionario e adicionando ele na lista autores
    informacoes = {'id': ident, 'nome': nome, 'dataNascimento': dataNascimento}
    autores.append(informacoes)
    # adicionar autor a biblioteca
    biblioteca['autores'].append(nome)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def remover_livro():
    if livros != []:
        escolha = input('titulo: ')
        # Caso em que o livro se encontra na biblioteca 
        if escolha in biblioteca['livros']:
            # verificando se o livro nao foi emprestado
            # se o livro nao for emprestado
            if escolha not in biblioteca['emprestimos']:
                # removendo o livro da lista livros e da biblioteca
                for x in livros:
                    if x['titulo'] == escolha:
                        livros.remove(x)
                biblioteca['livros'].remove(escolha)
                print(f'Livro "{escolha}" foi removido com sucesso')
            # se o livro for emprestado    
            else:
                print('O livro não pode ser removido porque foi emprestado')
        # Caso em que o livro não se encontra na biblioteca
        else:
            print('Livro inexistente')
    else:
        print('Nenhum livro adicionado')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def remover_autor():
    if autores != []:
        escolha = input('titulo: ')
        # caso em que o autor se encontra na biblioteca
        if escolha in biblioteca['autores']:
            for x in autores:
                if x['nome'] == escolha:
                    autores.remove(x)
            biblioteca['autores'].remove(escolha)
            print(f'Autor "{escolha}" foi removido com sucesso')
        # Caso em que o autor nao se encontra na biblioteca
        else:
            print('Livro inexistente')
    else:
        print('Nenhum livro adicionado')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_livros():
    print('=-'*10)
    for x in livros:
        print('"', x['titulo'], '"', 'data de cadastro/atualização: ', x['dataCadastro'], '|', x['dataAtualizacao'])
    print('=-'*10)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_autores():
    print('=-'*10)
    for x in biblioteca['autores']:
        print(x)
    print('=-'*10)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def cadastrar_aluno():
    # colocando o id altomaticamente
    if autores == []:
        ident = 0
    else:
        ident = alunos.index(alunos[-1])+1
    nome = input('nome: ')
    dataNascimento = 0
    email = input('email: ')
    # adicionando as informações na lista alunos
    informacoes = {'id': ident, 'nome': nome, 'dataNascimento': dataNascimento, 'email': email, 'emprestimos': []}
    alunos.append(informacoes)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def remover_aluno():
    # se algum aluno ja adicionado
    if alunos != []:
        # criando lista auxiliar
        lista_alunos = []
        for x in alunos:
            lista_alunos.append(x['nome'])
        escolha = input('nome: ')
        # se aluno existir
        if escolha in lista_alunos:
            # se aluno tiver emprestimos
            # criando uma lista auxiliar pro alunos com emprestimo
            livros_emprestados = []
            # se o aluno tiver livros emprestados eles serao adicionados a lista auxiliar
            for x in alunos:
                if x['nome'] == escolha:
                    for y in x['emprestimos']:
                        livros_emprestados.append(y)
            # só sera removido se não tiver nenhum emprestimo
            if livros_emprestados == []:            
                for x in alunos:
                    if x['nome'] == escolha:
                        alunos.remove(x)
                print(f'Aluno "{escolha}" foi removido com sucesso')
            else:
                print('Esse aluno nao pode ser removido pois ainda tem emprestimos pendentes')
        # se aluno nao existir
        else:
            print('Aluno inexistente')
    # nenhum aluno adicionado
    else:
        print('Nenhum aluno cadastrado')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_alunos():
    print('=-'*10)
    for x in alunos:
        print(x['nome'])
    print('=-'*10)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def fazer_emprestimo():
    # verificar se o aluno esta cadastrado
    # crio uma lista com o nome de todos os alunos
    lista_alunos = []
    for x in alunos:
        lista_alunos.append(x['nome'])
    # condicao para emprestimo caso aluno seja cadastrado
    aluno = input('aluno(a): ')
    if aluno in lista_alunos:
        # crio uma lista para mostrar os livros disponiveis
        livros_disp = []
        for x in livros:
            if x['disponivel'] == True:
                livros_disp.append(x['titulo'])
        # caso tenha algum livro disponivel
        if livros_disp != []:
            print('livros disponiveis: ')
            print('=-'*10)
            for x in livros_disp:
                print(x)
            print('=-'*10)
            # condicao para saber se o livro escolhido tem na biblioteca
            escolha = input('titulo: ')
            # livro existe
            if escolha in livros_disp:
                # relacionando emprestimo com aluno e adicionando o emprestimo ao dicionario biblioteca e deixando o livro 
                # indisponivel para emprestimo
                for x in alunos:
                    if x['nome'] == aluno:
                        x['emprestimos'].append(escolha)
                # adicionando a biblioteca
                biblioteca['emprestimos'].append(escolha)
                # mudando o estado de disponivel do livro
                for x in livros:
                    if x['titulo'] == escolha:
                        x['disponivel'] = False

                print(f'O livro "{escolha}" foi emprestado com sucesso')
                data_emprestimo = data.strftime('%d/%m/%Y')
                data_devolucao = (data+timedelta(days=7)).strftime('%d/%m/%Y')
                print(f'Data do emprestimo: {data_emprestimo}. Data da devolução: {data_devolucao}')
            #livro nao existe ou ja foi emprestado
            else:
                print('livro ja emprestado ou inexistente')
        # caso ainda não tenha livros disponiveis
        else:
            print('ainda não ha livros disponiveis para emprestimo')
    # caso o aluno nao seja cadastrado
    else:
        print(f'{aluno} não esta cadastrado')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def mostrar_emprestimos():
    # verificando se há algum emprestimo
    # caso tenha
    if biblioteca['emprestimos'] != []:
        # mostrar os alunos e seus emprestimos
        for x in alunos:
            # so mostra os alunos que tem emprestimos
            if x['emprestimos'] != []:
                print('=-'*10)
                print('emprestimos do aluno', x['nome'], ':')
                for y in x['emprestimos']:
                    print(y)
                print('=-'*10)
    # caso nao tenha
    else:
        print('ainda não foram feitos emprestimos')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def devolver_livro():
    # criando uma lista para verificar os alunos que possuem emprestimos
    aluno_emprestimo = []
    for x in alunos:
        if x['emprestimos'] != []:
            aluno_emprestimo.append(x['nome'])
    aluno = input('aluno(a): ')
    # caso aluno tenha livros emprestados
    if aluno in aluno_emprestimo:
        # mostrando os livros emprestados
        print('livros emprestados: ')
        for x in alunos:
            if x['nome'] == aluno:
                for y in x['emprestimos']:
                    print(y)
        # escolhendo qual livro vai devolver
        escolha = input('titulo: ')
        # removendo da biblioteca
        biblioteca['emprestimos'].remove(escolha)
        # removendo da lista alunos
        for x in alunos:
            if x['nome'] == aluno:
                x['emprestimos'].remove(escolha)
        # reestabelecendo o estado de disponivel do livro
        for x in livros:
            if x['titulo'] == escolha:
                x['disponivel'] == True
        print(f'o livro "{escolha}" foi devolvido')
        # atualizando a data de atualizacao do livro
        for x in livros:
            if x['titulo'] == escolha:
                x['dataAtualização'] = data.strftime('%d/%m/%Y')
    # caso aluno nao tenha livros emprestados ou nõa seja cadastrado
    else:
        print('alunos não cadastrado ou nao possui emprestimos')
    
    
    
    

        
    
    


