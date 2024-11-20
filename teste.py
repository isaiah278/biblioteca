from teste_funcao import menu, add_livro, add_autor, listar_livros, listar_autores, remover_livro, remover_autor, cadastrar_aluno, remover_aluno, listar_alunos, fazer_emprestimo, mostrar_emprestimos, devolver_livro

while True:
    
    opcao = menu()
    #livro 1 - adicionar livro
    #livro 2 - remover livro
    #livro 3 - listar livros
    if opcao == 'livro1':
        add_livro()
    if opcao == 'livro2':
        remover_livro()
    if opcao == 'livro3':
        listar_livros()
    
    #autor 1 - adicionar autor
    #autor 2 - remover autor
    #autor 3 - listar autor
    if opcao == 'autor1':
        add_autor()
    if opcao == 'autor2':
        remover_autor()
    if opcao == 'autor3':
        listar_autores()
    
    #alunos 1 - adicionar aluno
    #alunos 2 - remover aluno
    #alunos 3 - listar aluno
    if opcao == 'alunos1':
        cadastrar_aluno()
    if opcao == 'alunos2':
        remover_aluno()
    if opcao == 'alunos3':
        listar_alunos()
  
    #emprestimos 1 - Fazer empréstimo
    #emprestimos 2 - Devolver livro 
    #emprestimos 3 - Consultar empréstimos
    if opcao == 'emprestimos1':
        fazer_emprestimo()
    if opcao == 'emprestimos2':
        devolver_livro()
    if opcao == 'emprestimos3':
        mostrar_emprestimos()
    print('ola mundo')
    # sair do programa
    if opcao == 0:
        break