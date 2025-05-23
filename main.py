from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina
from modelos.nota import Nota
from modelos.turma import Turma


def exibir_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Cadastrar aluno")
    print("2. Cadastrar professor")
    print("3. Criar turma")
    print("4. Adicionar aluno à turma")
    print("5. Adicionar disciplina à turma")
    print("6. Matricular aluno em disciplina")
    print("7. Adicionar nota ao aluno")
    print("8. Consultar notas do aluno")
    print("9. Listar turmas")
    print("10. Exibir turma")
    print("11. Listar notas da disciplina")
    print("0. Sair")

# Objetos globais de exemplo (em produção, isso seria persistido num banco)
alunos = []
professores = []
turmas = []

def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            cpf = input("CPF (11 dígitos): ")
            try:
                aluno = Aluno(nome, cpf)
                alunos.append(aluno)
                print(f"Aluno {nome} cadastrado com sucesso.")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            nome = input("Nome do professor: ")
            cpf = input("CPF (11 dígitos): ")
            try:
                professor = Professor(nome, cpf)
                professores.append(professor)
                print(f"Professor {nome} cadastrado com sucesso.")
            except ValueError as e:
                print(e)

        elif opcao == "3":
            nome = input("Nome da turma: ")
            periodo = input("Período: ")
            turma = Turma(nome, periodo)
            turmas.append(turma)
            print(f"Turma {nome} criada com sucesso.")

        elif opcao == "4":
            if not alunos or not turmas:
                print("Cadastre alunos e turmas antes.")
                continue
            for i, t in enumerate(turmas):
                print(f"{i} - {t.nome}")
            turma_idx = int(input("Selecione a turma: "))
            for i, a in enumerate(alunos):
                print(f"{i} - {a.nome}")
            aluno_idx = int(input("Selecione o aluno: "))
            turmas[turma_idx].adicionar_aluno(alunos[aluno_idx])
            print(f"Aluno adicionado à turma.")

        elif opcao == "5":
            nome = input("Nome da disciplina: ")
            disciplina = Disciplina(nome)
            for i, t in enumerate(turmas):
                print(f"{i} - {t.nome}")
            turma_idx = int(input("Selecione a turma: "))
            turmas[turma_idx].adicionar_disciplina(disciplina)
            print("Disciplina adicionada à turma.")

        elif opcao == "6":
            for i, a in enumerate(alunos):
                print(f"{i} - {a.nome}")
            aluno_idx = int(input("Selecione o aluno: "))
            for i, t in enumerate(turmas):
                print(f"{i} - {t.nome}")
            turma_idx = int(input("Selecione a turma: "))
            for i, d in enumerate(turmas[turma_idx].disciplinas):
                print(f"{i} - {d.nome}")
            disc_idx = int(input("Selecione a disciplina: "))
            try:
                alunos[aluno_idx].matricular(turmas[turma_idx].disciplinas[disc_idx])
                print("Aluno matriculado na disciplina.")
            except Exception as e:
                print(e)

        elif opcao == "7":
            for i, a in enumerate(alunos):
                print(f"{i} - {a.nome}")
            aluno_idx = int(input("Selecione o aluno: "))
            for i, d in enumerate(alunos[aluno_idx].disciplinas_matriculadas):
                print(f"{i} - {d.nome}")
            disc_idx = int(input("Selecione a disciplina: "))
            av1 = float(input("Nota AV1: "))
            av2 = float(input("Nota AV2: "))
            nota = Nota(alunos[aluno_idx], alunos[aluno_idx].disciplinas_matriculadas[disc_idx], av1, av2)
            alunos[aluno_idx].adicionar_nota(nota)
            alunos[aluno_idx].disciplinas_matriculadas[disc_idx].adicionar_nota(nota)
            print("Nota adicionada com sucesso.")

        elif opcao == "8":
            for i, a in enumerate(alunos):
                print(f"{i} - {a.nome}")
            aluno_idx = int(input("Selecione o aluno: "))
            try:
                alunos[aluno_idx].consultar_notas()
            except ValueError as e:
                print(e)

        elif opcao == "9":
            Turma.listar_turmas()

        elif opcao == "10":
            for i, t in enumerate(turmas):
                print(f"{i} - {t.nome}")
            turma_idx = int(input("Selecione a turma: "))
            turmas[turma_idx].exibir()

        elif opcao == "11":
            for i, t in enumerate(turmas):
                print(f"{i} - {t.nome}")
            turma_idx = int(input("Selecione a turma: "))
            for i, d in enumerate(turmas[turma_idx].disciplinas):
                print(f"{i} - {d.nome}")
            disc_idx = int(input("Selecione a disciplina: "))
            turmas[turma_idx].disciplinas[disc_idx].listar_notas()

        elif opcao == "0":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida.")

def main():
    menu()


if __name__ == "__main__":
    main()

# Criar aluno 
'''
aluno1 = Aluno("12345678900", "Lucas Silva")
aluno2 = Aluno("12345678901", "Mariana Costa")
aluno3 = Aluno("12345678902", "João Pereira")
aluno4 = Aluno("12345678903", "Ana Souza")
aluno5 = Aluno("12345678904", "Pedro Oliveira")
aluno6 = Aluno("12345678905", "Julia Rocha")
aluno7 = Aluno("12345678906", "Carlos Lima")
aluno8 = Aluno("12345678907", "Beatriz Mendes")
aluno9 = Aluno("12345678908", "Rafael Martins")
aluno10 = Aluno("12345678909", "Fernanda Almeida")


#Criar Disciplina
disciplina1 = Disciplina("Matemática", 101)
disciplina2 = Disciplina("Portugues", 102)
disciplina3 = Disciplina("Geografia", 103)
disciplina4 = Disciplina("Historia", 104)
disciplina5 = Disciplina("Matemática", 105)


#Criar Professor
professor1 = Professor('123456789', 'Julio', disciplina1)
professor2 = Professor('123456788', 'Antonio', disciplina2)
professor3 = Professor('123456787', 'Carlos', disciplina3)
professor4 = Professor('123456786', 'Gabriela', disciplina4)
professor5 = Professor('123456785', 'Marcos', disciplina5)



#Criando a turma e adicionando os alunos e disciplina dela
turma1 = Turma('1 serie', 'Matutino')

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]
for aluno in lista_alunos:
    turma1.adicionar_aluno(aluno)

lista_disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]
for disciplina in lista_disciplinas:
    turma1.adicionar_disciplina(disciplina)

turma1.exibir()



# Criar e registrar nota
nota1 = Nota(aluno1, disciplina1, 8.0, 7.0)
nota2 = Nota(aluno1, disciplina2, 7.0, 6.0)
nota3 = Nota(aluno1, disciplina3, 7.0, 6.0)
nota4 = Nota(aluno1, disciplina4, 7.0, 6.0)
nota5 = Nota(aluno1, disciplina5, 7.0, 6.0)

professor1.adicionar_nota1(aluno1, disciplina1, 10, 10)
professor2.adicionar_nota1(aluno1, disciplina2, 7.0, 6.0)
professor3.adicionar_nota1(aluno1, disciplina3, 7.0, 6.0)
professor4.adicionar_nota1(aluno1, disciplina4, 7.0, 6.0)
professor5.adicionar_nota1(aluno1, disciplina5, 7.0, 6.0)

# Consultar as notas do aluno
aluno1.consultar_notas()'''