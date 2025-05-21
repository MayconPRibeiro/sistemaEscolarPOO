from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, cpf, nome, idade, escolaridade):
        super().__init__(cpf, nome, idade, escolaridade)

    def consultar_notas(self):
        pass