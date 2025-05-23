from modelos.nota import Nota

class Disciplina:

    disciplinas = []  ## Atributo de classe
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.notas = []

        Disciplina.disciplinas.append(self)

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def listar_notas(self):
        for nota in self.notas:
            print(f'Aluno: {nota.aluno.nome} ||  AV1: {nota.av1} || AV2: {nota.av2} || Media: {nota.media}')
        
