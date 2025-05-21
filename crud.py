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

    


class turma:
    def __init__(self, nome, id, periodo):
        self.nome = nome
        self.id = id
        self.periodo = periodo


class disciplina:
    def __init__(self, nome, id, av1, av2, notafinal):
        self.nome = nome
        self.id = id
        self.av1 = av1
        self.av2 = av2
        self.notafinal = (av1 + av2) / 2
        self.set_notafinal()
        self.get_notafinal()
    
    def set_notafinal(self):
        if self.notafinal >= 5:
            print(f'aluno {self.nome} Aprovado')
        elif notafinal == 4:
            print(f'aluno {self.nome} em Recuperação ')
        else:
            print(f'aluno {self.nome} Reprovado')

    def get_notafinal(self):
        return self.notafinal
            

        
        

