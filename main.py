from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina
from modelos.nota import Nota
from modelos.turma import Turma

def menu_principal():
    print('1. Professor\n 2. Aluno \n 3. Sair')

# Criar aluno 

aluno1 = Aluno("12345678900", "Lucas Silva")
aluno2 = Aluno("12345678901", "Mariana Costa")
aluno3 = Aluno("12345678902", "João Pereira")
aluno4 = Aluno("12345678903", "Ana Souza")
aluno5 = Aluno("12345678904", "Pedro Oliveira")
aluno6 = Aluno("12345678905", "Julia Rocha")
aluno7 = Aluno("12345678906", "Carlos Lima")
aluno8 = Aluno("12345678907", "Beatriz Mendes")
aluno9 = Aluno("12345678908", "Rafael Martins")
aluno10 = Aluno("12345678909", "Fernanda Almeida")


#Criar Disciplina
disciplina1 = Disciplina("Matemática", 101)
disciplina2 = Disciplina("Portugues", 102)
disciplina3 = Disciplina("Geografia", 103)
disciplina4 = Disciplina("Historia", 104)
disciplina5 = Disciplina("Matemática", 105)


#Criar Professor
professor1 = Professor('123456789', 'Julio', disciplina1)
professor2 = Professor('123456788', 'Antonio', disciplina2)
professor3 = Professor('123456787', 'Carlos', disciplina3)
professor4 = Professor('123456786', 'Gabriela', disciplina4)
professor5 = Professor('123456785', 'Marcos', disciplina5)



#Criando a turma e adicionando os alunos e disciplina dela
turma1 = Turma('1 serie', 'Matutino')

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]
for aluno in lista_alunos:
    turma1.adicionar_aluno(aluno)

lista_disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]
for disciplina in lista_disciplinas:
    turma1.adicionar_disciplina(disciplina)

turma1.exibir()



# Criar e registrar nota
nota1 = Nota(aluno1, disciplina1, 8.0, 7.0)
nota2 = Nota(aluno1, disciplina2, 7.0, 6.0)
nota3 = Nota(aluno1, disciplina3, 7.0, 6.0)
nota4 = Nota(aluno1, disciplina4, 7.0, 6.0)
nota5 = Nota(aluno1, disciplina5, 7.0, 6.0)

professor1.adicionar_nota1(aluno1, disciplina1, 10, 10)
professor2.adicionar_nota1(aluno1, disciplina2, 7.0, 6.0)
professor3.adicionar_nota1(aluno1, disciplina3, 7.0, 6.0)
professor4.adicionar_nota1(aluno1, disciplina4, 7.0, 6.0)
professor5.adicionar_nota1(aluno1, disciplina5, 7.0, 6.0)

# Consultar as notas do aluno
aluno1.consultar_notas()