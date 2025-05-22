from sqlalchemy import Column, Integer, String
from modelos import Base
from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina



class Turma(Base):
    __tablename__ = 'turmas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    periodo = Column(String, nullable=False)

    def __init__(self, nome, periodo, alunos, disciplina):
        total_alunos = [] # atributo de classe
        self.nome = nome
        self.periodo = periodo
        self.alunos = []
        self.disciplina = disciplina

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        Turma.total_alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.aluno:
            self.alunos.remove(aluno)
            print(f"Aluno {aluno.nome} removido da turma {self.nome}.")
        else:
            print("Erro: aluno não encontrado na turma.")

    @classmethod
    def mostrar_total_alunos(cls):
        return cls.total_alunos
 
