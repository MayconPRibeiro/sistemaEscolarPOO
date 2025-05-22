from modelos.pessoa import Pessoa

class Aluno_duplicado_error(Exception):
    pass

class Aluno(Pessoa):

    contador_alunos = 0;

    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)
        self.notas = []
        
        Aluno.contador_alunos += 1
       

    def matricular(self, disciplina):
        if disciplina not in self.disciplinas_matriculadas:
            self.disciplinas_matriculadas.append(disciplina)

        else:
            raise Aluno_duplicado_error(f'Aluno {self.nome} já matriculado')

    def consultar_notas(self):
        if not self.notas:
            raise ValueError(f'O aluno {self.nome} não possui notas')
        
        for nota in self.notas:
            print(nota.obter_notas)

    def adicionar_nota(self, nota):
        self.notas.append(nota)
            
        



