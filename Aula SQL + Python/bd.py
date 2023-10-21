import pymysql.cursors
try:
    conexao = pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='escola',
                              cursorclass = pymysql.cursors.DictCursor)

    print('Conexão estabelcida com sucesso')
except Exception as erro:
    print(f"Erro ao conectar com o banco:{erro}")

#Cursor
cursor = conexao.cursor()

def select():
    try:
        sql = 'SELECT * FROM alunos'
        cursor.execute(sql)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(f"Nome: {aluno['nome']} -Nota:{aluno['nota']}")
    except Exception as error:
        print(f'Erro ao buscar:{error}')

def insert(nome,idade,nota):
    try:
        sql = f"insert into alunos(nome,idade,nota)"\
              f"values(%s,%s,%s)"
        cursor.execute(sql,(nome,idade,nota))
        conexao.commit()
        print('Dados cadastrados com sucesso')
    except Exception as error:
        print(f'Erro ao cadastrar:{error}')

def update(nome,idade,nota,matricula):
    try:
        sql = 'update alunos set nome = %s,idade = %s,'\
               'nota = %s where matricula = %s'
        cursor.execute(sql,(nome,idade,nota,matricula))
        conexao.commit()
        print("Dados alterados com sucesso")
    except Exception as error:
        print(f'Erro ao atualizar os dados:{error}')


#update('Leticia Mota',25,9.7,1)
#select()

def delete(matricula):
    try:
      if alunoExiste(matricula):
        sql = 'delete from alunos where matricula = %s'
        cursor.execute(sql,matricula)
        conexao.commit()
        print('Aluno deletado com sucesso')
      else:
          print('Aluno não encontrado')
    except Exception as error:
        print(f'Erro ao deletar aluno:{error}')

#delete(1)
#select()

def alunoExiste(matricula):
    try:
        sql = 'select * from alunos where matricula = %s'
        cursor.execute(sql,matricula)
        if cursor.fetchall() == 1:
            return True
        else:
            return False
    except Exception as error:
        print(f'Erro ao consultar dados:{error}')



#delete(1)
#delete(2)
#select()

