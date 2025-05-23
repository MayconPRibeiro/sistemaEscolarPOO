from modelos.aluno import Aluno


class Nota:
    def __init__(self, aluno, disciplina, av1=0, av2=0):
        
        if not (av1 >= 0 and av1 <= 10):
            raise ValueError("Notas devem estar entre 0 e 10.")
        if not isinstance(av1, (int, float)):
            raise TypeError(F'Nota AV1 dever ser um número')
        if not isinstance(av2, (int, float)):
            raise TypeError(F'Nota AV2 dever ser um número')
        self.aluno = aluno  # objeto Aluno
        self.disciplina = disciplina  # objeto Disciplina
        self.av1 = av1
        self.av2 = av2

    @property
    def obter_notas(self):
        return f'Disciplina {self.disciplina.nome} || Aluno {self.aluno.nome}. Nota: Av1 = {self.av1}. Av2 = {self.av2}. Média: {self.media()}. Situação: {self.situacao()}.'

    def media(self):
        return((self.av1 + self.av2) / 2)
    
    def situacao(self):
        media = self.media()
        if media >= 5:
            return "Aprovado"
        
        elif media == 4:
            return "Recuperação"
        
        else:
            return "Reprovado"


