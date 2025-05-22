from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.nome = nome
        
        
        
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

        