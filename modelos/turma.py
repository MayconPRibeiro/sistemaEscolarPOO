from sqlalchemy import Column, Integer, String
from modelos import Base

class Turma(Base):
    __tablename__ = 'turmas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    periodo = Column(String, nullable=False)

    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo