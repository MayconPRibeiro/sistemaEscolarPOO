from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina
from modelos.nota import Nota


# Criar aluno e disciplina
aluno1 = Aluno("12345678900", "Lucas Silva")
disciplina1 = Disciplina("Matemática", 101)

# Criar e registrar nota
nota1 = Nota(aluno1, disciplina1, 8.0, 7.0)
#Criar Professor
professor1 = Professor('123456789', 'Julio', disciplina1)
professor1.adicionar_nota1(aluno1, disciplina1, 10, 10)

# Consultar as notas do aluno
aluno1.consultar_notas()