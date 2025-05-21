from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, cpf, nome, idade, escolaridade, disciplina):
        super().__init__(cpf, nome, idade, escolaridade)
        self.disciplina = disciplina

    def adicionar_nota(self, aluno, nota, turma):
        pass