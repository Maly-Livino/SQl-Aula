import bd

while True:
    print('--Bem vindo ao Menu--')
    print(' 1 - Adicionar Aluno')
    print(' 2 - Editar Aluno')
    print(' 3 - Deletar Aluno')
    print(' 4 - Listar todos os alunos')
    print(' 5 - Sair')
    opcao = input('Selecione uma Opção: ')
    if opcao == '1':
        nome = input('Digite o nome do Aluno:')
        idade = int(input('Digite a idade do Aluno:'))
        nota = float(input('Digite a nota do Aluno:'))
        bd.insert(nome,idade,nota)

    elif opcao == '2':
        nome = input('Digite o nome do Aluno:')
        idade = int(input('Digite a idade do Aluno:'))
        nota = float(input('Digite a nota do Aluno:'))
        matricula = int(input('Digite a Matricula do Aluno:'))
        bd.update(nome,idade,nota,matricula)

    elif opcao == '3':
        matricula = int(input('Digite a matricula do Aluno:'))
        bd.delete(matricula)

    elif opcao == '4':
        print('Essa é a lista de Alunos \n')
        bd.select()

    elif opcao == '5':
        break