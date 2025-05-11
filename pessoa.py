from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, cpf, nome, idade, escolaridade):
        self.__cpf = cpf
        self.nome = nome
        self.idade = idade
        self.escolaridade = escolaridade
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) == 11 and cpf.isdigit():
            self.__cpf = cpf
        else:
            raise ValueError("CPF inválido.")
    
    @abstractmethod
    def consultar_notas(self):
        pass

class Aluno(Pessoa):
    def __init__(self, cpf, nome, idade, escolaridade):
        super().__init__(cpf, nome, idade, escolaridade)

    def consultar_notas(self):
        pass


class Professor(Pessoa):
    def __init__(self, cpf, nome, idade, escolaridade, disciplina):
        super().__init__(cpf, nome, idade, escolaridade)
        self.disciplina = disciplina

    def adicionar_nota(self, aluno, nota, turma):
        pass
