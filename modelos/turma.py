from sqlalchemy import Column, Integer, String
from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina

class Turma():
    
    
    def __init__(self, nome, periodo, alunos=None, disciplinas=None):
        
        self.nome = nome
        self.periodo = periodo
        self.alunos = alunos if alunos is not None else []
        self.disciplinas = disciplinas if disciplinas is not None else []
        
    
    
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
        

    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)


    def remover_aluno(self, aluno):
        if aluno in self.aluno:
            self.alunos.remove(aluno)
            print(f"Aluno {aluno.nome} removido da turma {self.nome}.")
        else:
            print("Erro: aluno não encontrado na turma.")

    def exibir(self):
        print(f'Turma: {self.nome} - Periodo: {self.periodo}')
        print('Disciplinas:')
        for disciplina in self.disciplinas:
            print(f' - {disciplina.nome}')
        print('Alunos:')
        for aluno in self.alunos:
            print(f'  - {aluno.nome}')
            
            
 
