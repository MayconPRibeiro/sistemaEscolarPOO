from modelos.pessoa import Pessoa
from modelos.disciplina import Disciplina
from modelos.nota import Nota

class Professor(Pessoa):
    def __init__(self, cpf, nome, disciplina):
        super().__init__(cpf, nome)
        self.disciplina = disciplina


    def adicionar_nota1(self, aluno, disciplina, av1, av2):
        nova_nota = Nota(aluno, disciplina, av1, av2)
        aluno.adicionar_nota(nova_nota)


    def adicionar_nota2(self, aluno, disciplina, av1, av2):
        nova_nota = Nota(aluno, self.disciplina, av1, av2)
        aluno.adicionar_nota(nova_nota)

    def consultar_notas():
        pass


